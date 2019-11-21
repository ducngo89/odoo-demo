# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    # init chatter
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    _order = "id desc"

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _("New"):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hospital.appointment.sequence') or _('New')
            result = super(HospitalAppointment, self).create(vals)
            return result

    def _get_default_note(self):
        return 'test default'

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    name = fields.Char(string="Appointment ID", required=True, copy=False,
                       readonly=True, index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one(
        'hospital.patient', string="Patient", required=True)
    patient_age = fields.Integer("Age", related="patient_id.patient_age")
    notes = fields.Char(string="Register Note", default=_get_default_note)
    appointment_date = fields.Date(string="Date", required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string="Status", readonly=True, default="draft")
