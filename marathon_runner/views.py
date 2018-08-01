import math

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from marathon_utils.exceptions import InvalidQueryParamValueException
from marathon_utils.query import get_uint_query_param

from .models import MarathonRunner


def get_runners(req):
    from marathon_utils.random_utils import random_datetime
    import random

    limit = get_uint_query_param(req, 'limit', 50)
    if limit == 0:
        raise InvalidQueryParamValueException("'limit' should be > 0")

    offset = get_uint_query_param(req, 'offset', 0)
    search = req.GET.get('search')
    order_by = req.GET.get('order_by', 'bib_asc')
    if order_by and order_by not in ['alphabet_asc', 'alphabet_desc', 'bib_asc', 'bib_desc', 'place_asc', 'place_desc']:
        raise InvalidQueryParamValueException("'order_by' should be one of 'alphabet_asc', 'alphabet_desc', 'bib_asc', 'bib_desc', 'place_asc' or 'place_desc'")

    qs = MarathonRunner.objects.all()
    if order_by:
        if order_by == "alphabet_asc":
            qs = qs.order_by("last_name")
        elif order_by == "alphabet_desc":
            qs = qs.order_by("-last_name")

        elif order_by == "bib_asc":
            qs = qs.order_by("runner_number")
        elif order_by == "bib_desc":
            qs = qs.order_by("-runner_number")

        elif order_by == "place_asc":
            qs = qs.order_by("place")
        elif order_by == "place_desc":
            qs = qs.order_by("-place")

    if search:
        qss = search_runner(qs, search)
        count = qss.count()
        runners = qss.all()[offset:offset + limit]
        # runners = []
        # for qs_ in qss:
        #     runners.extend(list(qs_.all()[:50]))
    else:
        count = qs.count()
        runners = qs.all()[offset:offset + limit]

    page_count = int(math.ceil(count / limit))
    runners_json = {
        "overall_count": count,
        "pages": page_count,
        "current_page": int(math.ceil((offset + 1) / limit)),
        "runners": [{
                "runnerId": r.pk,
                "runnerNumber": r.runner_number,
                "runnerName": r.first_name + " " + r.last_name,
                "distance": 0,
                "time": int(random_datetime().timestamp()),
                "isAcceleration": random.choice([True, False]),
                "citizenship": r.citizenship,
                "place": r.place,
            } for r in runners]
    }

    return JsonResponse(runners_json)


def get_info(req):
    pass


def add_medical_help_info(req):
    pass


def search_runner(qs, search_by):
    # убираем все пробелы
    s = search_by.strip()

    # разбиваем по словам
    words = s.split()

    # выбираем из строки все числа и слова
    nums = [word for word in words if word.isdigit]
    words = [word for word in words if not word.isdigit]

    # если числа есть, считаем что первое найденное номер участника
    if nums:
        qs = qs.filter(runner_number=int(nums[0]))

    # # не обрабатываем больше 3х слов
    # if len(words) == 0:
    #     qs1 = qs.filter(first_name__contains=words[0])
    #     # qs2 = qs.filter(first_name__contains=words[0])
    #     # qs2 = qs.filter(first_name=words[0])
    # if words:
    #     qs1 = qs.filter(first_name__contains=words[0])
    #     qs2 = qs.filter(last_name__contains=words[0])

    return qs

