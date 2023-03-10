from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class ShelterRoom(models.Model):
    _name = 'shelter.room'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Shelter room for pets'

    home_id = fields.Many2one('res.partner', string='Home', store=True, required=True)
    location_id = fields.Many2one('stock.location', string='Location', store=True, related='home_id.location_id')
    city = fields.Char('City', related='home_id.city', store=True)
    state_id = fields.Many2one('res.country.state', string='State', store=True, related='home_id.state_id')
    country_id = fields.Many2one('res.country', string='Country', store=True, related='home_id.country_id')
    phone = fields.Char('Phone', related='home_id.phone', store=False)
    mobile = fields.Char('Mobile', related='home_id.mobile', store=False)
    shelter_note = fields.Text('Notes', related='home_id.shelter_note', store=False)
    type = fields.Selection([('dog','Dog'),('cat','Cat')], store=True, string='Pet type')
    active = fields.Boolean('Active', default=True)
    date_begin = fields.Date('Date begin')
    date_end   = fields.Date('Date end')
    reservation_ids = fields.One2many('shelter.reservation', 'room_id', string='Reservations', store=True)

    @api.depends('reservation_ids.done', 'reservation_ids')
    def get_room_available(self):
        available = True
        for li in self.reservation_ids:
            if li.done == False:    available = False
        if self.active == False:    available = False
        self.available = available
    available = fields.Boolean('Available', store=True, compute='get_room_available')

    @api.depends('home_id', 'date_begin', 'date_end', 'type')
    def get_room_name(self):
        name = ""
        if self.home_id.id:     name = self.home_id.name
        if self.type:           name += " - " + str(self.type)
        if self.date_begin:     name += " (" + str(self.date_begin) + ")"
        self.name = name
    name = fields.Char('Name', store=True, compute='get_room_name', readonly=True)

    def _get_reservations_count(self):
        results = self.env['shelter.reservation'].search([('room_id', '=', self.id)])
        self.reservation_count = len(results)
    reservation_count = fields.Integer('Reservations', compute=_get_reservations_count, store=False)