{
    'name': 'Shelter Hotel',
    'version': '16.0.1.0.0',
    'category': '',
    'description': u"""
Shelter hotel allows set Pet to volunteers home with reservations.
""",
    'author': 'Serincloud',
    'depends': [
        'shelter_pet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/shelter_room_views.xml',
        'views/shelter_reservation_views.xml',
        'views/res_partner_views.xml',
        'views/product_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
}
