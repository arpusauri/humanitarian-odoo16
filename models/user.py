from odoo import models, fields

class User(models.Model):
    _name = "humanitarian.user"
    _description = 'User'
    
    fullname = fields.Char(string="Fullname")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    id_card = fields.Char(string="ID Card")
    id_google = fields.Char(string="ID Google")
    picture_url = fields.Char(string="Picture URL")
    active = fields.Boolean(string="Active")