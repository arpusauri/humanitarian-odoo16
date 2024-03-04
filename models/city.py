from odoo import models, fields

class City(models.Model):
    _name = "humanitarian.city"
    _description = 'City'

    city_id = fields.Char(string="City")