from odoo import api, models, fields

class Subdistrict(models.Model):
    _name = 'humanitarian.humanitarian_kel'
    _description = 'Kelurahan'
    _rec_name = 'kel'

    kel = fields.Char(string="Nama Kelurahan", required=False) 
    kdkel = fields.Char(string="Nomor Induk Kelurahan", size=16, required=False) 
    kec = fields.Many2one(comodel_name='humanitarian.humanitarian_kec', string='Nama Kecamatan', required=False)
    kdkec = fields.Char(string="Kode Kecamatan", size=16, required=False)
    kota = fields.Many2one(comodel_name='humanitarian.humanitarian_kota', string='Nama Kota', required=False)
    kdkota = fields.Char(string="Kode Kota", size=16, required=False)
    provinsi = fields.Many2one(comodel_name='humanitarian.humanitarian_provinsi', string='Nama Provinsi', required=False)
    kdprov = fields.Char(string="Kode Provinsi", size=16, required=False)
     
    @api.onchange('kec')
    def _onchange_kdkec(self):
        self.kdkec = self.kec.kdkec
    
    @api.onchange('kota')
    def _onchange_kdkota(self):
        self.kdkota = self.kota.kdkota

    @api.onchange('provinsi')
    def _onchange_kdprov(self):
        self.kdprov = self.provinsi.kdprov