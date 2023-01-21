# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _


class ProjectProject(models.Model):
    _inherit = "project.project"

    type_ids = fields.Many2many(string="Collaborations",
        comodel_name='partner.type',
        relation='project_partnertype_rel',
        column1='project_id',
        column2='type_id',
    )

    @api.depends('type_ids')
    def get_type_char(self):
        typechar = ""
        for li in self.type_ids:
            typechar += li.code
        self.type_char = typechar
    type_char = fields.Char('Collaborations', store=True, compute='get_type_char')