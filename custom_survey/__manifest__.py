{
    'name': 'Custom Survey',
    'version': '16.0.1.0.0',
    'category': '',
    'description': u"""
Survey customizations:
- hide the results charts on the finished page
  for surveys scored without answers.
- show the total score in the responses list view.
""",
    'author': 'Serincloud',
    'depends': [
        'survey',
    ],
    'data': [
        'views/survey_templates.xml',
        'views/survey_user_views.xml',
    ],
    'installable': True,
}
