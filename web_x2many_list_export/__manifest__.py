# -*- coding: utf-8 -*-
{
    'name': 'One2Many Export (many2many export excel)',
    'summary': 'Export one2many and many2many embedded list fields to Excel XLSX in Odoo 19.',
    'description': """
        X2Many Excel Export adds an Export Excel button to embedded one2many
        and many2many list fields in Odoo 19 forms. Developers can enable XLSX
        export per x2many list by adding export_xlsx="1" on the nested list tag.
        Useful for exporting order lines, invoice lines, grant batches, product
        variants, employee lines, project lines, and any relational list shown
        inside a form view.
    """,
    'version': '19.0.1.0.0',
    'author': 'odoo.solution.vn',
    'support': 'odoo.solution.vn@gmail.com',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'price': 9.99,
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
