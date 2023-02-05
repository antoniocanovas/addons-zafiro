from odoo import _, api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    shelter_analytic_plan = fields.Many2one('account.analytic.plan','Shelter Analytic Plan', store=True, default=1)
