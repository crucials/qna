import datetime

from bson import ObjectId, is_valid
from errors.survey_not_found_error import SurveyNotFoundError
from models.survey_stats import PageVisitsRecord, SurveyStats
from mongo_database import survey_stats_collection


class StatsNotFoundError(Exception):
    pass


class SurveyStatsService:
    def create_initial_survey_stats(self, survey_id: str):
        if not ObjectId.is_valid(survey_id):
            raise SurveyNotFoundError()

        survey_stats_collection.insert_one({
            'survey_id': ObjectId(survey_id),
            'page_visits': []
        })

    def increment_survey_visits_count(self, survey_id: str):
        if not ObjectId.is_valid(survey_id):
            raise SurveyNotFoundError()
        
        today_date = datetime.datetime.now()
        # today_date = datetime.datetime.now() + datetime.timedelta(days=5)

        stats = survey_stats_collection.find_one({
            'survey_id': ObjectId(survey_id)
        })

        if stats is None:
            raise StatsNotFoundError()
        
        page_visits: list[PageVisitsRecord] = stats['page_visits']
        dates = [record['date'] for record in page_visits]

        visits_dates_indices = [index for index, date
                                     in enumerate(dates)
                                     if date.day == today_date.day]
        
        if len(visits_dates_indices) > 0:
            page_visits[visits_dates_indices[0]]['count'] += 1
        else:
            page_visits.append({
                'count': 1,
                'date': today_date
            })

            if len(page_visits) > 4:
                oldest_date_index = dates.index(min(dates))
                page_visits.pop(oldest_date_index)

        survey_stats_collection.update_one(
            {'_id': stats['_id']},
            {'$set': {'page_visits': page_visits}}
        )

        # dsafdafmasdkjfasdfasfjik my brain is melting


survey_stats_service = SurveyStatsService()
