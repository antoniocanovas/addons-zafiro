from odoo import models


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    def _get_max_score(self):
        """ Maximum reachable score, same rules as survey.user_input._compute_scoring_values """
        self.ensure_one()
        scores = self.suggested_answer_ids.mapped('answer_score')
        if self.question_type == 'simple_choice':
            return max([score for score in scores if score > 0], default=0)
        if self.question_type == 'multiple_choice':
            return sum(score for score in scores if score > 0)
        if self.is_scored_question:
            return self.answer_score
        return 0
