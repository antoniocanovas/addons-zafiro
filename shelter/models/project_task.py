# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = "project.task"

    product_id = fields.Many2one('product.template', string='Pet')
    home_id = fields.Many2one('res.partner', string='Home', domain="[('type_char','ilike','home')]")