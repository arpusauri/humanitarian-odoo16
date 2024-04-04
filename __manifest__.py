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
            'views/menu_root.views.xml',
            'views/config/menu_config.views.xml',
            'views/config/menuitem_location.views.xml',
            'views/config/menuitem_distrep.views.xml',
            'views/config/menuitem_sitrep.views.xml',
            'views/humanitarian_user.views.xml',
            'views/humanitarian_distrep.views.xml',
            'views/humanitarian_sitrep.views.xml',
            'views/config/distrep/distrep_cluster.views.xml',
            'views/config/distrep/distrep_dokumentasi.views.xml',
            'views/config/distrep/distrep_mitra.views.xml',
            'views/config/sitrep/sitrep_dampaksarpras.views.xml',
            'views/config/sitrep/sitrep_dokumentasi.views.xml',
            'views/config/sitrep/sitrep_jmlkorban.views.xml',
            'views/config/sitrep/sitrep_kebutuhan_mendesak.views.xml',
            'views/config/sitrep/sitrep_lokasi_terdampak.views.xml',
            'views/config/sitrep/sitrep_pengungsi.views.xml',
            'views/config/humanitarian_kel.views.xml',
            'views/config/humanitarian_jenis_kejadian.views.xml',
            'views/config/humanitarian_kec.views.xml',
            'views/config/humanitarian_kota.views.xml',
            'views/config/humanitarian_pic.views.xml',
            'views/config/humanitarian_provinsi.views.xml'
        ],

    'installable': True,
    'application': True,
    'auto_install': False

}