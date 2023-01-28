from odoo import _, api, fields, models


class CrmLead(models.Model):
    _inherit = 'res.partner'


    def _get_shelter_reservations_count(self):
        results = self.env['shelter.reservation'].search([('home_id', '=', self.id)])
        self.shelter_reservation_count = len(results)
    shelter_reservation_count = fields.Integer('Reservations', compute=_get_shelter_reservations_count, store=False)

    def _get_shelter_rooms_count(self):
        results = self.env['shelter.room'].search([('home_id', '=', self.id)])
        self.shelter_room_count = len(results)
    shelter_room_count = fields.Integer('Reservations', compute=_get_shelter_rooms_count, store=False)
