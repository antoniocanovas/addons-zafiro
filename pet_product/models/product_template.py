# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    PET_STATE = [
        ('new', 'New'),
        ('adopt', '2Adopt'),
        ('reserved', 'Reserved'),
        ('preadopt', 'Pre adopted'),
        ('done', 'Adoption'),
    ]
    state = fields.Selection(selection=PET_STATE, string="Status")
    task_ids = fields.One2many('project.task', 'product_id', string='Tasks')