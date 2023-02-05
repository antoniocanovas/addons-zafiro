# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.depends('pet_ok','default_code')
    def create_pet_analytic_account(self):
        # Automatic analytic account creation for pets:
        if (self.default_code != "") \
                and (self.pet_ok == True) \
                and not (self.income_analytic_account_id.id) \
                and not (self.expense_analytic_account_id.id):
            aa = self.env['account.analytic.account'].search([('code', '=', self.default_code)])
            plan = self.user.company_id.shelter_analytic_plan
            if not plan.id:
                raise ValidationError('Please review Company default Shelter Analytic Plan in this company settings.')
            if (not aa.id) and (plan_id.id):
                aa = self.env['account.analytic.account'].create({'code': self.default_code, 'name': self.name, 'plan_id': plan.id})
                self.write({'income_analytic_account_id': aa.id, 'expense_analytic_account_id': aa.id})