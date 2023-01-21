from odoo import _, api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    lead_ids = fields.Many2many(comodel_name='crm.lead',
                                relation='product_lead_rel',
                                column1='product_id',
                                column2='lead_id',
                                string="Leads",
                                )

    @api.depends('create_date')
    def get_product_product_self(self):
        for record in self:
            pp = self.env['product.product'].search([('id','=',record.id)])
            record.self = pp.id
    self = fields.Many2one('product.product', string="Self", store=True, compute="get_product_template_self")
