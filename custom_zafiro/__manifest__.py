{
    'name': 'Custom Zafiro',
    'version': '16.0.1.0.0',
    'category': '',
    'description': u"""
Zafiro particular customizations
""",
    'author': 'Serincloud',
    'depends': [
        'shelter_website',
        'hide_cart',
        'calendar',
    ],
    'data': [
        'views/product_views.xml',
        'views/sale_order_views.xml',
        'views/calendar_event_views.xml',
    ],
    'installable': True,
}
