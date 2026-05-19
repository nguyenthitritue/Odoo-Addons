/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { NavBar } from "@web/webclient/navbar/navbar";
import { useBus } from "@web/core/utils/hooks";
import { useState } from "@odoo/owl";
import { router, routerBus } from "@web/core/browser/router";

patch(NavBar.prototype, {
    setup() {
        super.setup(...arguments);
        // Reactive state — drives active tab class.
        // Initialized from current URL so hard-reload and direct URL entry work correctly.
        this._navState = useState({ actionId: router.current?.action });

        // ROUTE_CHANGE fires on browser Back/Forward (popstate) and bfcache restore.
        // It does NOT fire for programmatic pushState (menu clicks go through doAction
        // which calls router.pushState without emitting ROUTE_CHANGE), so we also
        // intercept onNavBarDropdownItemSelection below.
        useBus(routerBus, "ROUTE_CHANGE", () => {
            this._navState.actionId = router.current?.action;
        });
    },

    // Called for every menu item click in the navbar (both direct links and dropdown items).
    // Updating _navState here gives instant feedback before doAction finishes loading.
    onNavBarDropdownItemSelection(menu) {
        if (menu?.actionID) {
            this._navState.actionId = menu.actionID;
        }
        super.onNavBarDropdownItemSelection(menu);
    },

    isCurrentSection(section) {
        const currentAction = this._navState.actionId;
        if (!currentAction) return false;
        if (!section.childrenTree?.length) {
            // Loose equality: router.current.action can be string or number after URL parsing
            return section.actionID == currentAction;
        }
        return this._hasActiveChild(section, currentAction);
    },

    isCurrentItem(item) {
        return item.actionID == this._navState.actionId;
    },

    _hasActiveChild(section, currentAction) {
        for (const child of section.childrenTree || []) {
            if (!child.childrenTree?.length) {
                if (child.actionID == currentAction) return true;
            } else if (this._hasActiveChild(child, currentAction)) {
                return true;
            }
        }
        return false;
    },
});
