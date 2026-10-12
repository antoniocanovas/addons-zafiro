from odoo import models


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    def _get_report_sections(self):
        """ Answered questions grouped by section (page), numbered continuously, for the answers report """
        self.ensure_one()
        questions = self.predefined_question_ids & self._get_print_questions()
        sections = []
        number = 0
        for question in self.survey_id.question_and_page_ids:
            if question.is_page:
                sections.append({'page': question, 'questions': []})
            elif question in questions:
                if not sections:
                    sections.append({'page': False, 'questions': []})
                number += 1
                lines = self.user_input_line_ids.filtered(lambda line: line.question_id == question)
                sections[-1]['questions'].append({
                    'number': number,
                    'question': question,
                    'lines': lines,
                    'score': sum(lines.mapped('answer_score')),
                    'max_score': question._get_max_score(),
                })
        return [section for section in sections if section['questions']]

    def _get_report_max_score(self):
        self.ensure_one()
        questions = self.predefined_question_ids & self._get_print_questions()
        return sum(question._get_max_score() for question in questions)
