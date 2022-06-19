from odoo import fields, models, _


class FormRegister(models.Model):
    _name = 'form.register'

    name = fields.Char('Name', required=True) 
    gender = fields.Selection([("male", "Male"), ("female", "Female")], default="female")
    birth_date = fields.Date('Birth Date')
    skills = fields.Text()
    job_type = fields.Selection([("full time", "Full Time"), ("part time", "Part Time"), 
        ("on site", "On Site"), ("remote", "Remote")], default="full time")