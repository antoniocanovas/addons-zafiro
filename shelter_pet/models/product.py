# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    pet_ok   = fields.Boolean('Pet')
    pet_origin = fields.Char('Alias')
    task_pt_ids = fields.One2many('project.task', 'product_tmpl_id', string='Tasks')
    veterinary_id = fields.Many2one('res.partner', string='Veterinary', store=True)
    home_id = fields.Many2one('res.partner', string='Home', store=True)
    location_id = fields.Many2one('stock.location', related='home_id.location_id')
    volunteer_id = fields.Many2one('res.partner', string='Volunteer', store=True)
    rescuer_id = fields.Many2one('res.partner', string='Rescuer', store=True)

    sex = fields.Selection([('male', 'Male'), ('female', 'Female')], store=True, string='Sex')
    birthdate = fields.Date('Birthdate')
    pet_color = fields.Char('Color')
    hair = fields.Char('Hair')
    date_start = fields.Date('Date start')
    date_finish = fields.Date('Date finish')

#    Especie: Felina (son las categorías)
#    Raza: Común Europeo

    def _default_stage(self):
        return self.env['product.stage'].search([('name', '=', 'New')], limit=1).id
    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['product.stage'].search([])
        return stage_ids
    stage_id = fields.Many2one('product.stage', string='Stage', store=True, readonly=False,
                               tracking=True, copy=False, default=_default_stage,
                               group_expand='_read_group_stage_ids')

class ProductProduct(models.Model):
    _inherit = "product.product"

    pet_breed = fields.Char('Breed')
    stage_pp_id = fields.Many2one('product.stage', string='Stage Product', store=True,
                                readonly=False, related='product_tmpl_id.stage_id',)
    task_pp_ids = fields.One2many('project.task', 'product_id', string='Tasks', store=True)
    responsible_id = fields.Many2one('res.users', string='Responsible (staff)', store=True,
                                     related='product_tmpl_id.responsible_id', readonly=False)
    stage_code = fields.Char('Stage code', related='stage_pp_id.code')
    stage_sequence = fields.Integer('Stage sequence', related='stage_pp_id.sequence', store=True)
    stage_tree_sequence = fields.Integer('Stage tree sequence', related='stage_pp_id.tree_sequence', store=True)
