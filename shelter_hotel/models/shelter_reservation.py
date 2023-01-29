from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class ShelterReservation(models.Model):
    _name = 'shelter.reservation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Room reservations for pets'

    pet_id  = fields.Many2one('product.product', string='Pet', store=True,
                              domain=[('pet_ok','=',True),('stage_pp_id.code','not in',['preadoption','done'])])
    product_tmpl_id = fields.Many2one('product.template', store=True, related='pet_id.product_tmpl_id')
    room_id     = fields.Many2one('shelter.room', string='Room', store=True)
    home_id     = fields.Many2one('res.partner', string='Home', store=True, related='room_id.home_id')
    location_id = fields.Many2one('stock.location', string='Location', store=True, related='room_id.location_id')
    city        = fields.Char('City', store=True, related='home_id.city')
    type        = fields.Selection([('dog','Dogs'),('cat','Cats')], related='room_id.type')
    date_begin  = fields.Date('Begin', store=True)
    date_end    = fields.Date('End', store=True)
    comment     = fields.Text('Notes')
    done        = fields.Boolean('Done', default=False, store=True)

    @api.depends('room_id', 'date_begin', 'date_end', 'type')
    def get_room_name(self):
        name = ""
        if self.pet_id.id       name = self.pet_id.name
        if self.room_id.id:     name += "(" + self.room_id.home_id.name + ")"
        self.name = name
    name = fields.Char('Name', store=True, compute='get_room_name', readonly=True)