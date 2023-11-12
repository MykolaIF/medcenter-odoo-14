from odoo import models, fields


class MedicalSpecialty(models.Model):
    _name = 'medcenter.specialty'
    _description = 'Спеціальність'

    name = fields.Char(string='Назва спеціальності', required=True)
    color = fields.Integer(string='Колір')

    _sql_constraints = [(
        'specialty_name_unique',
        'unique(name)',
        'Назва спеціальності не унікальна (введіть іншу назву)'
    )]
