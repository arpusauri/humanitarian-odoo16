from odoo import api, models, fields

class City(models.Model):
    _name = "humanitarian.city"
    _description = 'City'
    _rec_name = 'kota'

    kota = fields.Char(string="Nama Kota", required=True)
    kdkota = fields.Char(string="Kode Kota", size=16, required=False)
    province = fields.Many2one(comodel_name='humanitarian.province', string='Nama Provinsi', required=False)
    kdprov = fields.Char(string="Kode Provinsi", size=16, required=False)

    @api.onchange('province')
    def _onchange_kdprov(self):
        self.kdprov = self.province.kdprov
