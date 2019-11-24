# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Record'
    # init chatter
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']
    # init Record name
    _rec_name = 'name'
    _order = "id desc"

    name = fields.Char(string="Name")
    gender = fields.Selection(
        [('male', 'Male'), ('fe_male', 'Female')], string="Gender")
    user_id = fields.Many2one(
        'res.users', string="Related User")
