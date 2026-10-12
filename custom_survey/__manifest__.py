{
    'name': 'Custom Survey',
    'version': '16.0.1.1.0',
    'category': '',
    'description': u"""
Survey customizations:
- hide the results charts on the finished page
  for surveys scored without answers.
- show the total score in the responses list view.
- printable PDF report of a participant's answers,
  with correct answers and score per question.
""",
    'author': 'Serincloud',
    'depends': [
        'survey',
    ],
    'data': [
        'views/survey_templates.xml',
        'views/survey_user_views.xml',
        'report/survey_user_input_report.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'custom_survey/static/src/scss/survey_report.scss',
        ],
    },
    'installable': True,
}
