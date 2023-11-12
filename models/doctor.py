from odoo import models, fields


class MedicalDoctor(models.Model):
    _name = 'medcenter.doctor'
    _description = 'Лікар'

    name = fields.Char(string='Лікар', required=True)
    phone = fields.Char(string='Телефон', required=True)
    email = fields.Char(string='Ел. пошта')
    specialty = fields.Many2many('medcenter.specialty', string='Спеціальність')
    description = fields.Char(string='Опис')
    photo = fields.Image('Фото', max_width=1067, max_height=1200)
