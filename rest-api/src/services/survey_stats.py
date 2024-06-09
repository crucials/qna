import datetime

from bson import ObjectId
from errors.survey_not_found_error import SurveyNotFoundError
from models.survey_stats import PageVisitsRecord
from mongo_database import survey_stats_collection, responses_collection


class StatsNotFoundError(Exception):
    pass


class SurveyStatsService:
    def create_initial_survey_stats(self, survey_id: str, survey_title: str):
        if not ObjectId.is_valid(survey_id):
            raise SurveyNotFoundError()

        survey_stats_collection.insert_one({
            'survey_id': ObjectId(survey_id),
            'survey_title': survey_title,
            'weekly_page_visits': [],
            'total_visits_count': 0,
        })

    def get_survey_stats(self, survey_id: str, include_responses_stats: bool = False):
        def has_optional_question_answer(response):
            return len([answer for answer in response['answers']
                        if answer['optional']
                        and answer['value'] is not None]) > 0

        if not ObjectId.is_valid(survey_id):
            return None
        
        survey_object_id = ObjectId(survey_id)
        
        stats = survey_stats_collection.find_one({
            'survey_id': survey_object_id
        })
        
        if not include_responses_stats or stats is None:
            return stats

        responses = list(responses_collection.find({'survey_id': survey_object_id}))

        stats['responses_count'] = len(responses)

        if stats['responses_count'] == 0:
            stats['responses_with_optional_question_percentage'] = 0
        else:
            responses_with_optional_questions_count = len([
                response for response in responses
                if has_optional_question_answer(response)
            ])

            stats['responses_with_optional_question_percentage'] = (
                responses_with_optional_questions_count / stats['responses_count']
                * 100
            )
            
        return stats

    def increment_survey_visits_count(self, survey_id: str):
        today_date = datetime.datetime.now()
        # today_date = datetime.datetime.now() + datetime.timedelta(days=9)

        stats = self.get_survey_stats(survey_id)

        if stats is None:
            raise StatsNotFoundError()
        
        weekly_visits: list[PageVisitsRecord] = stats['weekly_page_visits']
        dates = [record['date'] for record in weekly_visits]

        visits_dates_indices = [index for index, date
                                     in enumerate(dates)
                                     if date.day == today_date.day]
        
        if len(visits_dates_indices) > 0:
            weekly_visits[visits_dates_indices[0]]['count'] += 1
        else:
            weekly_visits.append({
                'count': 1,
                'date': today_date
            })

            if len(weekly_visits) > 7:
                oldest_date_index = dates.index(min(dates))
                weekly_visits.pop(oldest_date_index)

        survey_stats_collection.update_one(
            {'_id': stats['_id']},
            {
                '$set': {'weekly_page_visits': weekly_visits},
                '$inc': {'total_visits_count': 1}
            }
        )

        # dsafdafmasdkjfasdfasfjik my brain is melting


survey_stats_service = SurveyStatsService()
