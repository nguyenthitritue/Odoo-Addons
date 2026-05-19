# X2Many Excel Export

Show an **Export Excel** button on one2many and many2many embedded list fields in Odoo 19 form views.

This module is useful when users need to export relational lines such as order lines, invoice lines,
employee lines, grant batches, product variants, project lines, or any x2many list shown inside a form.

## Usage

Set `export_xlsx="1"` on the nested `<list>` tag of a x2many field:

```xml
<field name="forfeit_line_ids" nolabel="1">
    <list editable="bottom" export_xlsx="1">
        <field name="name"/>
        <field name="forfeit_qty"/>
    </list>
</field>
```

## Notes

- `Export Excel` is shown when `export_xlsx="1"` (or legacy `export="1"`).
- Export uses Odoo standard endpoint `/web/export/xlsx`.
- Only safe scalar field types are exported to avoid access issues on related records.
