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
            'views/menuitem_humanitarian.views.xml',
            'views/distrep/distrep.views.xml',
            'views/sitrep/sitrep.views.xml',
            'views/config/menuitem_config.views.xml',
            'views/config/cluster.views.xml',
            'views/config/mitra.views.xml',
            'views/config/pic.views.xml',
            'views/config/provinsi.views.xml',
            'views/config/kota.views.xml',
            'views/config/kec.views.xml',
            'views/config/desa.views.xml',
            'views/config/jen_kejadian.views.xml',
            'views/config/lok_terdampak.views.xml',
            'views/config/jml_korban.views.xml',
            'views/config/pengungsi.views.xml',
            'views/config/keb_mendesak.views.xml',
            'views/config/sitrep_doc.views.xml',
            'views/config/distrep_doc.views.xml',
            'views/config/dapras.views.xml'
        ],

    'installable': True,
    'application': True,
    'auto_install': False

}