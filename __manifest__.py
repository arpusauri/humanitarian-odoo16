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
            'views/config/megamenu.action.views.xml',
            'views/config/cluster.action.views.xml',
            'views/config/mitra.action.views.xml',
            'views/config/pic.action.views.xml',
            'views/config/province.action.views.xml',
            'views/config/city.action.views.xml',
            'views/config/district.action.views.xml',
            'views/config/subdistrict.action.views.xml',
            'views/config/jenis_kejadian.action.views.xml',
            'views/distrep/distrep.action.views.xml',
            'views/sitrep/sitrep.action.views.xml',
            'views/config/lokasi_terdampak.action.views.xml',
            'views/config/jml_korbanjiwa.action.views.xml',
            'views/config/pengungsi.action.views.xml',
            'views/config/kebutuhan_mendesak.action.views.xml',
            'views/config/sitrep_documentation.action.views.xml',
            'views/config/distrep_documentation.action.views.xml'
        ],

    'installable': True,
    'application': True,
    'auto_install': False

}