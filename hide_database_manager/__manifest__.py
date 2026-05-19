# -*- coding: utf-8 -*-

{
    'name': "Hide Database Manager",
    'license': 'AGPL-3',
    'summary': """Hide the database manager link on the Odoo 19 login screen.""",
    'description': """
        Hide the database manager link on the Odoo 19 login screen.
    """,
    'version': "19.0.1.0.0",
    'author': "odoo.solution.vn",
    'support': 'odoo.solution.vn@gmail.com',
    'images': ['static/description/img.png'],
    'category': 'Extra Tools',
    'depends': ['web'],
    'price': 9.99,
    'currency': 'USD',
    'data': [
        'views/common_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}
