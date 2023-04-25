{
    'name': 'Sale Order Report',
    'version': '1.0',
    'summary': 'Sale order report Customization',
    'description': '',
    'category': 'Sales',
    'author': 'Asad Ali',
    'website': '',
    'license': '',
    'depends': ['sale', 'stock', 'web', 'website'],

    'data': [
        'views/sale_order_report.xml',
        # 'views/sale_order_report_v1.xml',
        'views/irsaliye.xml',
        'views/teslimat_fisi.xml',
        'views/partner.xml',
        'views/saleorder.xml',
        'views/form_harcama.xml',
        # 'views/templates.xml',

    ],

    # 'assets': {
    #     'web.assets_backend': [
    #         'sale_order_report/static/src/css/style.css',
    #
    #     ],
    # },
    'auto_install': False,
}
