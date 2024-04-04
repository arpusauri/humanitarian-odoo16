from odoo import api, models, fields

class City(models.Model):
    _name = "humanitarian.humanitarian_kota"
    _description = 'Kota'
    _rec_name = 'kota'

    kota = fields.Char(string="Nama Kota", required=True)
    kdkota = fields.Char(string="Kode Kota", size=16, required=False)
    provinsi = fields.Many2one(comodel_name='humanitarian.humanitarian_provinsi', string='Nama Provinsi', required=False)
    kdprov = fields.Char(string="Kode Provinsi", size=16, required=False)

    @api.onchange('provinsi')
    def _onchange_kdprov(self):
        self.kdprov = self.provinsi.kdprov

