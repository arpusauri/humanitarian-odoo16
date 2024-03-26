from odoo import api, models, fields

class District(models.Model):
    _name = "humanitarian.district"
    _description = 'District'
    _rec_name = "kec"

    kec = fields.Char(string="Nama Kecamatan", required=False) 
    kdkec = fields.Char(string="Kode Kecamatan", size=16, required=False) 
    city = fields.Many2one(comodel_name='humanitarian.city', string='Kota', required=False)
    kel = fields.Many2one(comodel_name='humanitarian.subdistrict', string='Desa', required=False)
    kdkel = fields.Many2one(comodel_name='humanitarian.subdistrict', string='Kode Desa', required=False)
    provinsi = fields.Many2one(comodel_name='humanitarian.province', string='Provinsi', required=False)
    kdkota = fields.Char(string="Kode Kota", size=16, required=False)

    @api.onchange('city')
    def _onchange_kdkota(self):
        self.kdkota = self.city.kdkota
