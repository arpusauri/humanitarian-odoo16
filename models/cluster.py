from odoo import models, fields

class Cluster(models.Model):
    _name = "humanitarian.cluster"
    _description = 'Cluster'


    cluster = fields.Selection([
        ('hygiene_kit', 'Hygiene Kit'),
        ('wash', 'Wash'),
        ('nfi', 'NFI'),
        ('sar', 'SAR')
    ], string='Cluster')
    distrep_id = fields.Char(string="Distribution")
    program = fields.Char(string="Program")
    jumlah = fields.Char(string="Jumlah")
    satuan = fields.Char(string="Satuan")