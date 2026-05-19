# -*- coding: utf-8 -*-

{
    'name': "Hide Inbox Chatter",
    'license': 'AGPL-3',
    'summary': """Hide the messaging inbox menu from the Odoo 19 backend navbar.""",
    'description': """
        Hide the messaging inbox menu from the Odoo 19 backend navbar.
    """,
    'version': "19.0.1.0.0",
    'author': "odoo.solution.vn",
    'support': 'odoo.solution.vn@gmail.com',
    'images': ['static/description/img.png'],
    'category': 'Extra Tools',
    'depends': ['mail'],
    'data': [

    ],
    'assets': {
        'web.assets_backend': [
            'hide_inbox_chatter/static/src/xml/*.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,

}
