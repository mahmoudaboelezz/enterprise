# -*- coding: utf-8 -*-
{
    'name': "ProjoMania Create Portal Tasks",

    'summary': """Enable Portal Users to create tasks""",

    'description': """
        Long description of module's purpose
    """,

    'author': "ProjoMania",
    'website': "http://www.projomania.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Operations/Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'portal', 'hr_timesheet', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/assets.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'website.assets_frontend': [
            '/projomania_portal_create_task/static/src/js/projomania_task_feedback.js',
        ],
    },
}
