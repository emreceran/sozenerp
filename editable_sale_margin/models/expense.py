# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _


class projectexpense(models.Model):
    _inherit = "hr.expense"

    project_field = fields.Many2one('project.project', 'name', select=True, website_form_blacklisted=False)