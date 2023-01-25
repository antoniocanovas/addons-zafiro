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
    home_id         = fields.Many2one('res.partner', string='Home', domain="[('type_char','ilike','home')]")
    veterinary_id   = fields.Many2one('res.partner', string='Veterinary', domain="[('type_char','ilike','veterinary')]")
    volunteer_id    = fields.Many2one('res.partner', string='Volunteer', domain="[('type_char','ilike','volunteer')]")
    product_image   = fields.Binary('Image', related='product_id.image_1920', store=False)
