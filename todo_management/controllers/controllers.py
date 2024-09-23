# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/odoo17/apps/todoManagement(http.Controller):
#     @http.route('//opt/odoo17/apps/todo_management//opt/odoo17/apps/todo_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo17/apps/todo_management//opt/odoo17/apps/todo_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo17/apps/todo_management.listing', {
#             'root': '//opt/odoo17/apps/todo_management//opt/odoo17/apps/todo_management',
#             'objects': http.request.env['/opt/odoo17/apps/todo_management./opt/odoo17/apps/todo_management'].search([]),
#         })

#     @http.route('//opt/odoo17/apps/todo_management//opt/odoo17/apps/todo_management/objects/<model("/opt/odoo17/apps/todo_management./opt/odoo17/apps/todo_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo17/apps/todo_management.object', {
#             'object': obj
#         })

