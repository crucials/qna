import datetime
from typing import TypedDict


class PageVisitsRecord(TypedDict):
    date: datetime.datetime
    count: int


class SurveyStats(TypedDict):
    _id: str
    survey_id: str
    page_visits: list[PageVisitsRecord]
