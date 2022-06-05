{
    'name':'Website Animate',
    'description':"Provide animation for page\'s blocks",
    'category': 'Website',
    'version':'1.1',
    'author':'Odoo S.A.',
    'data': [
        # 'views/assets.xml',
        'views/options.xml',
    ],
    'depends': ['website'],
    'images': [
        'static/description/icon.png',
    ],
    'assets': {
        'website.assets_frontend': [
            '/website_animate/static/src/scss/o_animate_frontend.scss',
            '/website_animate/static/src/js/o_animate.frontend.js'
        ],
        'website.assets_editor': [
            '/website_animate/static/src/scss/o_animate_editor.scss',
            '/website_animate/static/src/js/o_animate.editor.js'
        ],
    },
}
