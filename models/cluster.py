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
    distrep_id = fields.Many2one('humanitarian.distrep', string="Distribution")
    program = fields.Char(string="Program")
    jumlah = fields.Integer(string="Jumlah")
    satuan = fields.Char(string="Satuan")