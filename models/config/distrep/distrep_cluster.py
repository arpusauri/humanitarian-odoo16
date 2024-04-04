from odoo import models, fields

class Cluster(models.Model):
    _name = "humanitarian.distrep_cluster"
    _description = 'Cluster'

    cluster = fields.Selection([
        ('hygiene_kit', 'Hygiene Kit'),
        ('wash', 'Wash'),
        ('nfi', 'NFI'),
        ('sar', 'SAR')
    ], string='Cluster')
    cluster_dist_id = fields.Many2one('humanitarian.humanitarian_distrep', string='Distribution')
    program = fields.Char(string="Program")
    jumlah = fields.Integer(string="Jumlah")
    satuan = fields.Char(string="Satuan")