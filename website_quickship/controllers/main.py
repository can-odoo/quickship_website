# -*- coding: utf-8 -*-
from odoo import http

class Controllers(http.Controller):

    @http.route(['/dropdown/nationwide-services'], auth='public', website=True, type='http')
    def render_nationwide_services(self, **kw):
        return http.request.render('website_quickship.nationwide_services')

    @http.route(['/dropdown/international-services'], auth='public', website=True, type='http')
    def render_international_services(self, **kw):
        return http.request.render('website_quickship.international_services')
