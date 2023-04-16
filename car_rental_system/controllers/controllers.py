# -*- coding: utf-8 -*-
# from odoo import http


# class CarRentalSystem(http.Controller):
#     @http.route('/car_rental_system/car_rental_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_rental_system/car_rental_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_rental_system.listing', {
#             'root': '/car_rental_system/car_rental_system',
#             'objects': http.request.env['car_rental_system.car_rental_system'].search([]),
#         })

#     @http.route('/car_rental_system/car_rental_system/objects/<model("car_rental_system.car_rental_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_rental_system.object', {
#             'object': obj
#         })
