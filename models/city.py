from odoo import models, fields

class City(models.Model):
    _name = "humanitarian.city"
    _description = 'City'
    _rec_name = "city_id"

    city_id = fields.Char(string="City")