from odoo import _, api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _get_pet_reservations_count(self):
        results = self.env['shelter.reservation'].search([('product_id', '=', self.id)])
        self.pet_reservation_count = len(results)
    pet_reservation_count = fields.Integer('Reservations', compute=_get_pet_reservations_count, store=False)



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_pet_pt_reservations_count(self):
        results = self.env['shelter.reservation'].search([('product_tmpl_id', '=', self.id)])
        self.pet_pt_reservation_count = len(results)
    pet_pt_reservation_count = fields.Integer('Reservations', compute=_get_pet_pt_reservations_count, store=False)
