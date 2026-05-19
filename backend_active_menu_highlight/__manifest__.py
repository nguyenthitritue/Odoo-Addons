{
    "name": "Active Menu Highlight",
    "version": "19.0.1.0.0",
    "summary": "Highlight the active tab and dropdown item across all Odoo 19 backend menus.",
    "description": """
Active Menu Highlight keeps the selected backend menu visible while users move
between list, form, and dropdown actions. It adds a clear active state to the
current navbar section and dropdown menu item across all backend menus in Odoo 19.
    """,
    "depends": ["web"],
    "author": "HRIS-VNG",
    "license": "LGPL-3",
    "category": "Extra Tools",
    "images": ["static/description/main_screenshot.png"],
    "assets": {
        "web.assets_backend": [
            "backend_active_menu_highlight/static/src/js/navbar/active_nav_tab.js",
            "backend_active_menu_highlight/static/src/xml/active_nav_tab.xml",
            "backend_active_menu_highlight/static/src/scss/active_nav_tab.scss",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
