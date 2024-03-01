# -*- coding: utf-8 -*-
{
    'name': "Humanitarian",

    'summary': """
        Module Aplikasi Humanitarian""",

    'description': """
        Manajemen Humanitarian
    """,

    'author': "cnt",

    'category': 'Uncategorized',
    'version': '0.1',

		# Depencicy
    'depends': ['base'],

    # Include ALL XML Code in Here be mindful of order
        'data': [
            'security/ir.model.access.csv',
            'views/menuitems.views.xml',
            'views/cluster.action.views.xml',
            'views/mitra.action.views.xml',
            'views/pic.action.views.xml',
            'views/jenis_kejadian.action.views.xml',
            'views/distrep.action.views.xml'
        ],

    'installable': True,
    'application': True,
    'auto_install': False

}