# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    allow_add_tasks = fields.Boolean(string="Allow Add Tasks", )


class ProjectTask(models.Model):
    _name = 'project.task'
    _inherit = 'project.task'

    customer_feedback = fields.Selection(string="Customer Feedback", selection=[('waiting_approval', 'Waiting Approval'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='waiting_approval', tracking=True)
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", default=lambda self: self.env.company.currency_id )
    estimated_cost = fields.Monetary(string='Estimated Cost')

    def ask_partner_approval(self):
        for rec in self:
            if rec.customer_feedback == 'rejected' or not rec.customer_feedback:
                rec.customer_feedback = 'waiting_approval'

    def print_planned_hours_website(self, planned_hours):
        planned_seconds = planned_hours * 60 * 60
        minute, seconds = divmod(planned_seconds, 60)
        hours, minutes = divmod(minute, 60)
        planned_time = "%02d Hours" % (hours)
        if minutes:
            planned_time += ", %02d Minutes" % (minutes)
        return planned_time