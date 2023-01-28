from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class ShelterReservation(models.Model):
    _name = 'shelter.reservation'
    _description = 'Room reservations for pets'

    room_id     = fields.Many2one('shelter.room', string='Room', store=True)
    home_id     = fields.Many2one('res.partner', string='Home', store=True, related='room_id.home_id')
    location_id = fields.Many2one('stock.location', string='Location', store=True, related='room_id.location_id')
    type        = fields.Selection([('dog','Dogs'),('cat','Cats')], related='room_id.type')
    date_begin  = fields.Date('Begin', store=True)
    date_end    = fields.Date('End', store=True)
    done        = fields.Boolean('Done', default=False, store=True)

    api.depends('room_id', 'date_begin', 'date_end', 'type')
    def get_room_name(self):
        name = ""
        if self.home_id.id:     name = self.home_id.name
        if self.type:           name += " - For: " + str(self.type)
        if self.date_begin:     name += " - From: " + str(self.date_begin)
        if self.date_end:       name += " - To: " + str(self.date_end)
        self.name = name
    name = fields.Char('Name', store=True, compute='get_room_name', readonly=True)