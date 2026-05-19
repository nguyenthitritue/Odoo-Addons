# -*- coding: utf-8 -*-
{
    'name': 'X2Many Excel Export',
    'summary': 'Add an Export Excel button to one2many and many2many list fields in Odoo 19.',
    'description': """
        Add an Export Excel button to one2many and many2many list fields when
        export_xlsx="1" is set on the nested list view.
    """,
    'version': '19.0.1.0.0',
    'author': 'odoo.solution.vn',
    'support': 'odoo.solution.vn@gmail.com',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'price': 8.6,
    'currency': 'USD',
    'depends': ['web'],
    'images': ['static/description/main_screenshot.png'],
    'assets': {
        'web.assets_backend': [
            'web_x2many_list_export/static/src/js/x2many_list_export/x2many_list_export.js',
            'web_x2many_list_export/static/src/js/x2many_list_export/x2many_list_export.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
