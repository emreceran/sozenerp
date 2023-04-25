# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    toplam_adamsaat = fields.Float("toplam Adam/Saat", compute='_compute_toplam_adamsaat', store=True)
    adamsaat_maliyet = fields.Float("Adam/Saat Fiyat", default="2")
    malzeme_margin =fields.Float("Malzeme Marj", compute='_compute_malzeme_marj', store=True)
    # margin_percent = fields.Float("Margin (%)", compute='_compute_margin', store=True, group_operator="avg")

    @api.depends('margin', 'toplam_adamsaat')
    def _compute_malzeme_marj(self):
        """
        Compute the amounts of the SO line.
        """
        for rec in self:
            rec.malzeme_margin = rec.margin - rec.toplam_adamsaat


    @api.depends('order_line', 'order_line.adamsaat', 'adamsaat_maliyet')
    def _compute_toplam_adamsaat(self):
        """
        Compute the amounts of the SO line.
        """
        for rec in self:
            toplam = 0
            for line in rec.order_line:
                toplam += line.adamsaat_subtotal
            rec.toplam_adamsaat = toplam * rec.adamsaat_maliyet


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    margin = fields.Float("Margin", digits='Product Price', readonly=False, store=True, groups="base.group_user")
    margin_percent = fields.Float("Margin (%)", store=True, readonly=False, groups="base.group_user")
    adamsaat = fields.Float(related='product_id.adamsaat', depends=['product_id'])
    cost_discount = fields.Float("indirim", readonly=False, store=True, groups="base.group_user")


    adamsaat_subtotal = fields.Float(
        string="adamsaat toplam",
        compute='_compute_adamsaat',
        store=True, precompute=True)

    purchase_price = fields.Float(
        string="Cost", compute="_compute_purchase_price",
        digits='Product Price', store=True, readonly=False, precompute=True,
        groups="base.group_user")

    @api.depends('product_id', 'company_id', 'currency_id', 'product_uom')
    def _compute_purchase_price(self):
        for line in self:
            if not line.product_id:
                line.purchase_price = 0.0
                continue
            line = line.with_company(line.company_id)
            product_cost = line.product_id.standard_price
            line.purchase_price = line._convert_price(product_cost, line.product_id.uom_id)

    # @api.depends('price_subtotal', 'product_uom_qty', 'purchase_price')
    # def _compute_margin(self):
    #     for line in self:
    #         line.margin = line.price_subtotal - (line.purchase_price * line.product_uom_qty)
    #         line.margin_percent = line.price_subtotal and line.margin / line.price_subtotal

    def _convert_price(self, product_cost, from_uom):
        self.ensure_one()
        if not product_cost:
            # If the standard_price is 0
            # Avoid unnecessary computations
            # and currency conversions
            if not self.purchase_price:
                return product_cost
        from_currency = self.product_id.cost_currency_id
        to_cur = self.currency_id or self.order_id.currency_id
        to_uom = self.product_uom
        if to_uom and to_uom != from_uom:
            product_cost = from_uom._compute_price(
                product_cost,
                to_uom,
            )
        return from_currency._convert(
            from_amount=product_cost,
            to_currency=to_cur,
            company=self.company_id or self.env.company,
            date=self.order_id.date_order or fields.Date.today(),
            round=False,
        ) if to_cur and product_cost else product_cost
        # The pricelist may not have been set, therefore no conversion
        # is needed because we don't know the target currency..

    @api.depends('product_uom_qty', 'adamsaat')
    def _compute_adamsaat(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            line.adamsaat_subtotal =line.product_uom_qty * line.adamsaat

    @api.onchange('cost_discount')
    def onchange_cost_discount(self):
        # self.purchase_price = (1 - self.cost_discount/100) * self.purchase_price
        # print(self.purchase_price)
        for line in self:
            line = line.with_company(line.company_id)
            product_cost = line.product_id.standard_price
            x = line._convert_price(product_cost, line.product_id.uom_id)
            line.purchase_price = (1 - line.cost_discount/100) * x
            print(line.purchase_price)


    @api.onchange('price_subtotal', 'margin_percent')
    def onchange_margin_percent(self):
        self.margin = self.price_subtotal - (self.purchase_price * self.product_uom_qty)
        if self._context.get('margin_percent'):
            self.margin_percent = self._context.get('margin_percent')
        if self.purchase_price > 0.0 and self.margin_percent and not self._context.get('get_sizes'):
            margin_percent = self.margin_percent
            montant_extras = self.purchase_price * (self.margin_percent)
            self.price_unit = self.purchase_price + montant_extras
            self.margin_percent = margin_percent
            context = dict(self.env.context)
            context.update({'get_sizes': True, 'margin_percent': margin_percent})
            self.env.context = context

    @api.onchange('product_uom_qty', 'purchase_price', 'discount')
    def compute_margin_1(self):
        self.margin = self.price_subtotal - (self.purchase_price * self.product_uom_qty)
        self.margin_percent = self.purchase_price and self.margin / self.purchase_price
        context = dict(self.env.context)
        context.update({'get_sizes': True})
        self.env.context = context

    @api.onchange('price_unit')
    def onchange_price_unit_1(self):
        if self.price_unit and not self._context.get('get_sizes'):
            self.write({'margin_percent': self.purchase_price and self.margin / self.purchase_price})
            context = dict(self.env.context)
            context.update({'get_sizes': True})
            self.env.context = context

    @api.onchange('margin')
    def onchange_margin(self):
        if self.price_unit and not self._context.get('get_sizes') and not self._context.get('margin_percent'):
            self.price_unit = self.purchase_price + self.margin

