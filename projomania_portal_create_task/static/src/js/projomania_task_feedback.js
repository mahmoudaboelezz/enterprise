odoo.define('website.theme', function (require) {
    'use strict';

    var ajax = require('web.ajax');
    var task_id = $('#task_id_estimation').val();
    var feedback_url = '/task/feedback/' + task_id

    $('#approve_task_estimation').on('click', '', function () {
        ajax.jsonRpc(feedback_url, 'call', {'customer_feedback': 'approved'})
        $('#customer_feedback').html("(Approved)");
        $('#customer_feedback').css('color', 'green');
        $('#approve_task_estimation').addClass('d-none');
        $('#reject_task_estimation').addClass('d-none');
    });

    $(document).on('click', '#reject_task_estimation', function () {
        ajax.jsonRpc(feedback_url, 'call', {'customer_feedback': 'rejected'})
        $('#customer_feedback').html("(Rejected)");
        $('#customer_feedback').css('color', 'red');
        $('#approve_task_estimation').addClass('d-none');
        $('#reject_task_estimation').addClass('d-none');
    });

})