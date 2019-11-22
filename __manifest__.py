# -*- coding: utf-8 -*-
{
    'name': "EBK Hospital v1.0.0",
    'version': '1.0.1',
    'summary': """
        Hospital module""",

    'description': """
        Long description of module's purpose
    """,

    'author': "EBK",
    'website': "https://ebk.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/data.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
