# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = "product.product"

    PET_STATE = [
        ('new', 'New'),
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('preadopt', 'Pre adopted'),
        ('done', 'Done'),
    ]
    stage_id    = fields.Many2one('product.stage', string="Stage",)
    task_ids = fields.One2many('project.task', 'product_id', string='Tasks')
    pet_ok   = fields.Boolean('Pet', default=True)