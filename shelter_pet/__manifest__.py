{
    'name': 'Shelter Pets',
    'version': '16.0.0.1',
    'category': 'Product',
    'description': u"""
Base module for Pets as Odoo Products.
""",
    'author': 'Serincloud',
    'depends': [
        'contacts',
        'product',
        'project',
        'stock',
        'account',
    ],
    "data": [
        "data/product_stage.xml",
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/product_views.xml",
        "views/project_task_views.xml",
        "views/stock_location_views.xml",
        "views/res_company_views.xml",
        "data/partner_type.xml",
        "views/menu_views.xml",
    ],
    'installable':True,
    'application':False,
}
