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

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Integer(string='Age')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')

    name = fields.Char(string='Test')

    # auto name
    name_seq = fields.Char(string='Patient ID', required=True,
                           copy=False, readonly=True, index=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female')
    ], default='male', string='Gender')

    age_group = fields.Selection(
        [('major', 'Major'), ('minor', 'Minor')], string='Age Group', compute='set_age_group')

    @api.model
    def create(self, vals):
        # auto name
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
                'hospital.patient.sequence') or _('New')
        # end auto name
        result = super(HospitalPatient, self).create(vals)
        return result
