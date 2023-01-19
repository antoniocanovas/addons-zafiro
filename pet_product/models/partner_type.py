# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _


class PartnerType(models.Model):
    _name = 'partner.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Partner Type'

    name = fields.Char('Name', store=True, required=True, readonly=True)
    code = fields.Char('Code', store=True, required=True, readonly=True)
    color = fields.Integer('Color', store=True)