{
    'name': 'Shelter CRM',
    'version': '16.0.1.0.0',
    'category': '',
    'description': u"""
Shelter CRM to adopters
""",
    'author': 'Serincloud',
    'depends': [
        'crm',
        'sale_management',
        'shelter_pet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/model_views.xml',
    ],
    'installable': True,
}
