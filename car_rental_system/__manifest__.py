# -*- coding: utf-8 -*-
{
    'name': "Car Rental System",

    'summary': """
        Car Rental System""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],
    'application': True,

    # always loaded
    'data': [
        'security/groups.xml',
        'security/car_reservation.xml',
        'security/ir.model.access.csv',
        'views/car.xml',
        'wizard/car_reserve_wizard.xml',
        'views/car_reservation.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'car_rental_system/static/src/xml/custom_rainbow_man.xml',
        ],
    },
}
