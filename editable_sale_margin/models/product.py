from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    adamsaat = fields.Float (string = "Adam/Saat", default = 0.0)