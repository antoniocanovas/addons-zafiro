# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    pet_ok   = fields.Boolean('Pet', default=True)


class ProductProduct(models.Model):
    _inherit = "product.product"


    task_ids = fields.One2many('project.task', 'product_id', string='Tasks')

#    def _default_stage(self):
#        return self.env['product.stage'].search([('name', '=', 'New')], limit=1).id

#    @api.model
#    def _read_group_stage_ids(self, stages, domain, order):
#        stage_ids = self.env['product.stage'].search([])
#        return stage_ids

    @api.model
    def _read_group_stage_ids(self):
        stage_ids = self.env['product.stage'].search([],order='sequence asc')
        return stage_ids
    stage_id = fields.Many2one('product.stage', string='Stage', store=True, readonly=False, ondelete='restrict',
                               tracking=True, copy=False, default='New')