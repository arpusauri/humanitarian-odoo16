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
            'views/humanitarian_menu_root.views.xml',
            'views/config/humanitarian_menu_config.views.xml',
            'views/config/menuitem_location.views.xml',
            'views/config/menuitem_distrep.views.xml',
            'views/config/menuitem_sitrep.views.xml',
            'views/user/user.views.xml',
            'views/distrep/distrep.views.xml',
            'views/sitrep/sitrep.views.xml',
            'views/config/distrep_cluster.views.xml',
            'views/config/humanitarian_mitra.views.xml',
            'views/config/humanitarian_pic.views.xml',
            'views/config/humanitarian_provinsi.views.xml',
            'views/config/humanitarian_kota.views.xml',
            'views/config/humanitarian_kec.views.xml',
            'views/config/humanitarian_desa.views.xml',
            'views/config/humanitarian_jenis_kejadian.views.xml',
            'views/config/sitrep_lokasi_terdampak.views.xml',
            'views/config/sitrep_jumlah_korban_jiwa.views.xml',
            'views/config/sitrep_pengungsi.views.xml',
            'views/config/sitrep_kebutuhan_mendesak.views.xml',
            'views/config/sitrep_dampaksarpras.views.xml',
            'views/config/sitrep_dokumentasi.views.xml',
            'views/config/distrep_dokumentasi.views.xml',
            'views/config/distrep_cluster.views.xml'
        ],

    'installable': True,
    'application': True,
    'auto_install': False

}