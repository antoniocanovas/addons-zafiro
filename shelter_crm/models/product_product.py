from odoo import _, api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    lead_ids = fields.Many2many(comodel_name='crm.lead',
                                relation='product_lead_rel',
                                column1='product_id',
                                column2='lead_id',
                                string="Leads",
                                )
