# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    PARTNER_STATUS = [
        ('new', 'New'),
        ('sent', 'Sent'),
        ('approved', 'Approved'),
        ('fail', 'Failed')]
    shelter_state   = fields.Selection(selection = PARTNER_STATUS, string='Survey status', default='new', store=True)
    shelter_begin   = fields.Date('Date start')
    shelter_end     = fields.Date('Date end')
    shelter_note    = fields.Text('Notes')
    location_id     = fields.Many2one('stock.location', 'WH Location')

    def get_shelter_location(self):
        self.shelter_location_id = self.env.user.company_id.shelter_location_id.id
    shelter_location_id = fields.Many2one('stock.location', 'Default parent location', compute='get_shelter_location')

    type_ids    = fields.Many2many(string="Collaborations",
        comodel_name='partner.type',
        relation='partner_partnertype_rel',
        column1='partner_id',
        column2='type_id',
    )
    @api.depends('type_ids')
    def get_type_char(self):
        typechar = ""
        for li in self.type_ids:
            typechar += li.code
        self.type_char = typechar
    type_char = fields.Char('Collaborations', store=True, compute='get_type_char')

    # Tareas (es casa, veterinario, usuario de la tarea o voluntario):
    def get_partner_tasks(self):
        tasks = self.env['project.task'].search(['|','|',('veterinary_id','=', self.id),
                                                 ('volunteer_id','=', self.id),
                                                 ('user_ids.partner_id','=',self.id)])
        self.task_ids = tasks
    task_ids = fields.Many2many('project.task', store=False, compute='get_partner_tasks')