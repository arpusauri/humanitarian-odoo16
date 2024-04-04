from odoo import api, models, fields

class District(models.Model):
    _name = "humanitarian.humanitarian_kec"
    _description = 'Kecamatan'
    _rec_name = "kec"

    kec = fields.Char(string="Nama Kecamatan", required=False) 
    kdkec = fields.Char(string="Kode Kecamatan", size=16, required=False) 
    kel = fields.Many2one(comodel_name='humanitarian.humanitarian_kel', string='Kelurahan', required=False)
    kdkel = fields.Char(comodel_name='Kode Kelurahan', required=False)
    provinsi = fields.Many2one(comodel_name='humanitarian.humanitarian_provinsi', string='Provinsi', required=False)
    kota = fields.Many2one(comodel_name='humanitarian.humanitarian_kota', string='Kota', required=False)
    kdkota = fields.Char(string="Kode Kota", size=16, required=False)

    @api.onchange('kota')
    def _onchange_kdkota(self):
        self.kdkota = self.kota.kdkota
