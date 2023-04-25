from odoo import fields, models

class inheritpartner(models.Model):
    _inherit = "res.partner"

    vergi_daire = fields.Char(string="Vergi Dairesi")




class inherittransfer(models.Model):
    _inherit = "stock.picking"

    irsaliye_gitti = fields.Boolean(string="İrsaliye gitti")