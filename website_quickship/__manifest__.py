# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'website_quickship',
    'description': '...',
    'category': 'Website/Theme',
    'version': '1.0.0',
    'author': 'Odoo',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'data/presets.xml',
        'data/menu.xml',

        # pages
        'data/pages/about_us.xml',
        'data/pages/page_not_found.xml',

        # header
        'views/header.xml',

    ],
    'assets': {
        'web._assets_primary_variables': [
            'website_quickship/static/src/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'website_quickship/static/src/scss/bootstrap_overriden.scss'),
        ],
        'web.assets_frontend': [
            #'website_quickship/static/src/scss/theme.scss',
            # Interactivity, js files
            # 'website_quickship/static/src/js/theme.js',
        ],
    },
    'installable': True,
    'application': True,
}
