from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class ShelterRoom(models.Model):
    _name = 'shelter.room'
    _description = 'Shelter room for pets'

    home_id = fields.Many2one('res.partner', string='Home', store=True, required=True)
    location_id = fields.Many2one('stock.location', string='Location', store=True, related='home_id.location_id')
    city = fields.Char('City', related='home_id.city', store=True)
    state_id = fields.Many2one('res.state', string='State', store=True)
    country_id = fields.Many2one('res.country', string='Country', store=True)
    phone = fields.Char('Phone', related='home_id.phone', store=False)
    mobile = fields.Char('Mobile', related='home_id.mobile', store=False)
    comment = fields.Text('Notes', related='home.comment', store=False)
    type = fields.Selection([('dog','Dogs'),('cat','Cats')], store=True, string='Pet type')
    active = fields.Boolean('Active', default=True)
    date_begin = fields.Date('Date begin')
    date_end   = fields.Date('Date end')
    reservation_ids = fields.One2many('shelter.reservation', 'room_id', string='Reservations', store=True)


    api.depends('reservation_ids.done')
    def get_room_available(self):
        available = True
        for li in self.reservation_ids:
            if li.done == False:  available = False
        self.available = available
    available = fields.Boolean('Available', compute='get_room_available')

    api.depends('home_id', 'date_begin', 'date_end', 'type')
    def get_room_name(self):
        name = ""
        if self.home_id.id:     name = self.home_id.name
        if self.type:           name += " - For: " + str(self.type)
        if self.date_begin:     name += " - From: " + str(self.date_begin)
        if self.date_end:       name += " - To: " + str(self.date_end)
        self.name = name
    name = fields.Char('Name', store=True, compute='get_room_name', readonly=True)
