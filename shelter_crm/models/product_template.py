from odoo import _, api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.template'

    lead_pt_ids = fields.Many2many(comodel_name='crm.lead',
                                relation='product_lead_rel',
                                column1='product_tmpl_id',
                                column2='lead_id',
                                string="Leads",
                                )
