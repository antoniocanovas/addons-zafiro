# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
##############################################################################
from odoo import api, fields, models, _

class ResCompany(models.Model):
    _inherit = 'res.company'

    shelter_location_id = fields.Many2one('stock.location', 'Shelter locations', store=True)
