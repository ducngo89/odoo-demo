# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name = fields.Char(string='Patient Name')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'
    # init chatter
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    # init Record name
    _rec_name = 'patient_name'

    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Integer(string='Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')

    # auto name
    name_seq = fields.Char(string='Order Reference', required=True,
                           copy=False, readonly=True, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        # auto name
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient.sequence') or _('New')
        # end auto name
        result = super(HospitalPatient, self).create(vals)
        return result
