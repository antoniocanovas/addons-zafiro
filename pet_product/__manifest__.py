{
    'name': 'Pet Product',
    'version': '16.0.0.1',
    'category': 'Product',
    'description': u"""
Base module for Pets as Odoo Products.
""",
    'author': 'Serincloud',
    'depends': [
        'product',
        'project',
    ],
    "data": [
        "data/partner_type.xml",
        "security/ir.model.access.csv",
#        "views/product_views.xml",
    ],
    'installable':True,
    'application':False,
}
