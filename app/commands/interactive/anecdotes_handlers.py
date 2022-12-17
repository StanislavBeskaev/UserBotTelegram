import random
from dataclasses import dataclass

import requests

RETRIES_COUNT = 5


@dataclass
class Anecdote:
    """Класс анекдота с источником и успехом получения"""

    text: str
    source: str
    success: bool


def get_anecdote() -> Anecdote:
    """Функция для получения анекдота. Источник анекдота выбирается случайным образом из списка источников"""
    anecdote_sources = {'rzhunemogu.ru': _get_rzhunemogu_anecdote}
    attempts_count = 0
    while attempts_count < RETRIES_COUNT:
        source = random.choice(list(anecdote_sources.keys()))
        anecdote_query = anecdote_sources[source]()
        if not anecdote_query.success:
            attempts_count += 1
            continue
        return anecdote_query

    return Anecdote(text='', source='', success=False)


def _get_rzhunemogu_anecdote() -> Anecdote:
    """Функция получения текста анекдота с сайта rzhunemogu.ru"""
    rzhunemogu_api_url = 'http://rzhunemogu.ru/RandJSON.aspx?CType=1'
    rzhunemogu_source = 'rzhunemogu.ru'

    response = requests.get(rzhunemogu_api_url)
    if response.status_code != 200:
        return Anecdote(text='', success=False, source=rzhunemogu_source)
    anecdote_text = response.text[12:]
    anecdote_text = anecdote_text[:-2]
    return Anecdote(text=anecdote_text, success=True, source=rzhunemogu_source)
