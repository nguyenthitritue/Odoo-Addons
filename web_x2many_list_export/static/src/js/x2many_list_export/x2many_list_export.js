/** @odoo-module */

import { _t } from "@web/core/l10n/translation";
import { download } from "@web/core/network/download";
import { evaluateBooleanExpr } from "@web/core/py_js/py";
import { exprToBoolean } from "@web/core/utils/strings";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { X2ManyField } from "@web/views/fields/x2many/x2many_field";

const SAFE_EXPORT_FIELD_TYPES = new Set([
    "boolean",
    "char",
    "date",
    "datetime",
    "float",
    "html",
    "integer",
    "monetary",
    "selection",
    "text",
]);

patch(X2ManyField.prototype, {
    setup() {
        super.setup(...arguments);
        this.notification = useService("notification");
    },

    get showX2ManyExportXlsxButton() {
        return (
            this.props.viewMode === "list" &&
            this._isX2ManyExportEnabled() &&
            Boolean(this.list?.count) &&
            this.archInfo?.activeActions?.exportXlsx !== false
        );
    },

    get x2ManyExportButtonLabel() {
        return _t("Export Excel");
    },

    _isX2ManyExportEnabled() {
        const xmlDoc = this.archInfo?.xmlDoc;
        if (!xmlDoc) {
            return false;
        }

        const exportXlsxAttr = xmlDoc.getAttribute("export_xlsx");
        if (exportXlsxAttr !== null) {
            return exprToBoolean(exportXlsxAttr, false);
        }

        const exportAttr = xmlDoc.getAttribute("export");
        if (exportAttr !== null) {
            return exprToBoolean(exportAttr, false);
        }

        return false;
    },

    _isColumnInvisible(column) {
        if (!column?.column_invisible) {
            return false;
        }
        try {
            return evaluateBooleanExpr(column.column_invisible, this.list.evalContext);
        } catch {
            return false;
        }
    },

    _getX2ManyExportableFields() {
        return (this.archInfo?.columns || [])
            .filter((column) => {
                const fieldType = column.fieldType || this.list.fields?.[column.name]?.type;
                return (
                    column?.type === "field" &&
                    column?.name &&
                    column?.hasLabel !== false &&
                    SAFE_EXPORT_FIELD_TYPES.has(fieldType) &&
                    !this._isColumnInvisible(column)
                );
            })
            .map((column) => {
                const field = this.list.fields?.[column.name] || {};
                return {
                    name: column.name,
                    label: column.label || column.string || column.name,
                    type: column.fieldType || field.type,
                    store: "store" in field ? field.store : true,
                };
            });
    },

    _getX2ManyExportIds() {
        const numericIds = (this.list.resIds || this.list.currentIds || []).filter((id) =>
            Number.isInteger(id)
        );
        if (numericIds.length) {
            return numericIds;
        }
        return (this.list.records || [])
            .map((record) => record.resId)
            .filter((id) => Number.isInteger(id));
    },

    async onClickX2ManyExportXlsx() {
        const fields = this._getX2ManyExportableFields();
        const ids = this._getX2ManyExportIds();

        if (!fields.length || !ids.length) {
            this.notification.add(_t("No data available to export."), {
                type: "warning",
            });
            return;
        }

        await download({
            url: "/web/export/xlsx",
            data: {
                data: JSON.stringify({
                    import_compat: false,
                    context: this.props.context || {},
                    domain: [["id", "in", ids]],
                    fields,
                    groupby: [],
                    ids,
                    model: this.list.resModel,
                }),
            },
        });
    },
});
