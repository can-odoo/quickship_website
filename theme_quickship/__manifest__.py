# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'theme_quickship',
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
        
    ],
    'assets': {
        'web._assets_primary_variables': [
            'theme_quickship/static/src/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            ('prepend', 'theme_quickship/static/src/scss/bootstrap_overriden.scss'),
        ],
        'web.assests_frontend': [
            #'theme_quickship/static/src/scss/theme.scss',
            # Interactivity, js files
            # 'theme_quickship/static/src/js/theme.js',
        ],
    },
    'installable': True,
    'application': True,
}
