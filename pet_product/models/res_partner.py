# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    type_ids = fields.Many2many('partner.type', string="Collaborations")

    @api.depends('type_ids')
    def get_type_char(self):
        typechar = ""
        for li in self.type_ids:
            typechar += li.code
        self.type_char = typechar
    type_char = fields.Char('Collaborations', store=True, compute='get_type_char')

    # Tareas (es casa, veterinario, usuario de la tarea o voluntario):
    def get_partner_tasks(self):
        tasks = self.env['project.task'].search([('home_id','=', record.id),('user_ids.partner_id','=',record.id)])
        self.task_ids = tasks
    task_ids = fields.Many2many('project.task', store=False, compute='get_partner_tasks')