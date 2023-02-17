# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = "project.task"

    product_id      = fields.Many2one('product.product', string='Pet', store=True)
    product_tmpl_id = fields.Many2one('product.template', string='Pet template', related='product_id.product_tmpl_id', store=True)
    home_id         = fields.Many2one('res.partner', string='Home', store=True)
    location_id     = fields.Many2one('stock.location', string='Location', related='home_id.location_id')
    veterinary_id   = fields.Many2one('res.partner', string='Veterinary', store=True)
    volunteer_id    = fields.Many2one('res.partner', string='Volunteer', store=True)
    product_image   = fields.Binary('Image', related='product_id.image_1920', store=False)

    @api.depends('project_id.type_id')
    def _get_project_type_char(self):
        type_char = ""
        if self.project_id.type_id.id == self.company_id.veterinary_type_id.id: type_char = 'veterinary'
        if self.project_id.type_id.id == self.company_id.network_type_id.id:    type_char = 'network'
        if self.project_id.type_id.id == self.company_id.management_type_id.id: type_char = 'management'
        self.project_type = type_char
    project_type    = fields.Char('Project type', store=True, compute='_get_project_type_char')