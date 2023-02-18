from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class ProductLeadRel(models.Model):
    _name = 'product.lead.rel'
    _description = 'Relational table for product and opportunities'

    product_id = fields.Many2one('product.product', string='Product', store=True)
    product_tmpl_id = fields.Many2one('product.template', string='Product tmpl', store=True, related='product_id.product_tmpl_id')
    lead_id = fields.Many2one('crm.lead', string="Oportunity", store=True)

