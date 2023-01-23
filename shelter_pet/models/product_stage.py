# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################
from odoo import api, fields, models, tools, SUPERUSER_ID, _


class ProductStage(models.Model):
    _name = "product.stage"
    _order = 'sequence, id'
    _description = 'Product Stage'

    name = fields.Char(string='Name')
    sequence = fields.Integer(default=1)
    code = fields.Char(string="Code")


