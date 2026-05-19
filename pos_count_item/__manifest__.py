# -*- coding: utf-8 -*-
{
    'name': "POS Item Count",
    'license': 'AGPL-3',
    'summary': """Show the total item quantity in the Odoo 19 POS order summary.""",
    'description': """
        Show the total item quantity in the Odoo 19 Point of Sale order summary.
    """,
    'version': "19.0.1.0.0",
    'author': "odoo.solution.vn",
    'support': 'odoo.solution.vn@gmail.com',
    'images': ['static/description/img.png'],
    'category': 'Sales/Point of Sale',
    'price': 9.99,
    'currency': 'USD',
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_count_item/static/src/css/item_count.scss',
            'pos_count_item/static/src/xml/*',
        ]
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
