from odoo import api, models, fields

class DistrepDocumentation(models.Model):
    _name = "humanitarian.distrep_dokumentasi"
    _description = 'Dokumentasi Distribution Reports'

    image = fields.Binary(string="Image")
    image_url = fields.Char('Image URL', compute='get_image_url')
    dok_dist_id = fields.Many2one('humanitarian.humanitarian_distrep', string='Distribution')


@api.depends('image')
def get_image_url(self):
    web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
    for record in self:
        record.image_url = f"{web_base_url}/web/image?model={self._name}&id={record.id}&field=image"