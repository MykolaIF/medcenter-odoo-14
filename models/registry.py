from odoo import models, fields, api


class MedicalRegistry(models.Model):
    _name = 'medcenter.registry'
    _description = 'Реєстрація клієнтів'

    partner_id = fields.Many2one("res.partner", string='Клієнт', required=True)
    partner_phone = fields.Char(string="Телефон", related="partner_id.phone")
    date_time = fields.Datetime(string='Дата та час')
    comment = fields.Char(string='Коментар')
    doctor = fields.Many2one(
        'medcenter.doctor',
        string='Лікар',
        required=True
    )
    services = fields.Many2many('medcenter.service', string='Послуги')
    company_id = fields.Many2one(
        'res.company',
        'Company',
        default=lambda self: self.env.user.company_id.id,
        index=1
    )
    currency_id = fields.Many2one(
        'res.currency',
        'Currency',
        default=lambda self: self.env.user.company_id.currency_id.id,
        required=True
    )
    amount = fields.Monetary(
        compute="_compute_total",
        string='Сума послуг',
        currency_field='currency_id',
        readonly=True,
        store=True
    )
    status = fields.Selection(
        [("new", "Реєстрація клієнта"),
         ("done", "Послуги надані"),
         ("cancel", "Відмова")],
        string="Статус виконання",
        default="new"
    )

    @api.depends("amount", "services")
    def _compute_total(self):
        for record in self:
            record["amount"] = sum(
                [item.price for item in
                 self.services])
