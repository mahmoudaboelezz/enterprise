# -*- coding: utf-8 -*-
from odoo import http, SUPERUSER_ID
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
# from odoo.tools import


class CustomerPortal(CustomerPortal):

    @http.route('/task/create', type='http', auth="user", website=True)
    def create_task(self, **kw):
        project_id = kw.get('filterby', False) and int(kw.get('filterby'))
        print('gfyudbcid')
        if project_id:
            project = request.env['project.project'].browse(project_id)
            print(project)
            values = {'project_detail': project, 'tasks_list': '/my/tasks?filterby=%s' % project.id,
                      'creator': request.env.user.name, 'page_name': 'create_task', 'create_task': True}

        return request.render("projomania_portal_create_task.portal_create_task", values)

    @http.route()
    def portal_my_tasks(self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, search=None, search_in='content', groupby='project', **kw):
        response = super(CustomerPortal, self).portal_my_tasks(page=page, date_begin=date_begin, date_end=date_end, sortby=sortby, filterby=filterby, search=search, search_in=search_in, groupby=groupby, kw=kw)
        project = filterby and request.env['project.project'].browse(int(response.qcontext.get('filterby'))) or False
        if project:
            response.qcontext.update({'project': project})
        return response

    @http.route('/task/feedback/<model("project.task"):task_obj>', auth='user', type='json')
    def projomania_approve_task(self, task_obj, **kw):
        user = request.env.user
        if kw.get('customer_feedback'):
            task_obj.with_user(SUPERUSER_ID).write({'customer_feedback': kw.get('customer_feedback')})
            message = "%s has %s the task." % (user.partner_id.name, kw.get('customer_feedback'))
            task_obj.with_user(SUPERUSER_ID).message_post(body=message, message_type='comment', subtype='mail.mt_comment')
            return {"message": "success"}
        return {"message": "error"}
