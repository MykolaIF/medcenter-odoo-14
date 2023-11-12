from odoo import models, fields


class MedicalService(models.Model):
    _name = 'medcenter.service'
    _description = 'Послуга'

    name = fields.Char(
        string='Послуга',
        required=True
    )
    responsible = fields.Many2one(
        'medcenter.doctor',
        string='Відповідальний',
        required=True
    )
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
    price = fields.Monetary(
        string='Вартість',
        currency_field='currency_id',
        required=True,
    )

    _sql_constraints = [(
        'service_name_unique',
        'unique(name)',
        'Назва послуги не унікальна (введіть іншу назву)'
    )]
