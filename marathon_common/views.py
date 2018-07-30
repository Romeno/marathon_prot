# -*- coding: utf-8
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect

from .models import Marathon, MarathonRoute


def get_settings(req):
    current_marathon = Marathon.objects.filter(is_active=True).order_by("start_time").first()
    routes = MarathonRoute.objects.filter(is_active=True).order_by("start_time")

    settings = {
        "marathon": {
            "id": current_marathon.pk,
            "name": current_marathon.name,
            "start_time": current_marathon.start_time.timestamp(),
            "end_time": current_marathon.end_time.timestamp(),
            "marathon_routes": [
            ]
        },
    }

    for r in routes:
        route = {
            "route_id": r.pk,
            "name": r.name,
            "start_time": r.start_time.timestamp(),
            "end_time": r.end_time.timestamp(),
        }

        settings["marathon"]["marathon_routes"].append(route)

    return JsonResponse(settings)


def get_route_map(req, id):
    route = MarathonRoute.objects.get(pk=id)

    return HttpResponseRedirect(route.map.url)


def get_route_heights(req, id):
    return JsonResponse({})


def get_route_info(req, id):
    sample_text = """<b><i>What is Lorem Ipsum?</i></b>
<b>Lorem Ipsum</b> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

<b><i>Why do we use it?</i></b>
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."""

    info = {
        "menu": [
            {
                # "en": "General information",
                "ru": "Общая информация",
                "menu_items": [
                    {
                        # "en": "Schedule",
                        "ru": "Расписание",
                        "text": sample_text,
                    },
                    {
                        # "en": "Awards",
                        "ru": "Награждение",
                        "text": sample_text,
                    },
                ]
            },
            {
                # "en": "Registration",
                "ru": "Регистрация",
                "menu_items": [
                    {
                        # "en": "How to register",
                        "ru": "Как зарегистрироваться",
                        "text": sample_text,
                    },
                    {
                        # "en": "Terms of participation",
                        "ru": "Основные условия",
                        "text": sample_text,
                    },
                    {
                        # "en": "Cost",
                        "ru": "Стоимость",
                        "text": sample_text,
                    },
                    {
                        # "en": "Qualification into elite",
                        "ru": "Квалификация в элиту",
                        "text": sample_text,
                    },
                ]
            },
            {
                # "en": "Acquiring a bib number",
                "ru": "Получение номера",
                "menu_items": [
                    {
                        # "en": "Where and when",
                        "ru": "Где и когда",
                        "text": sample_text,
                    },
                    {
                        # "en": "Terms of participation",
                        "ru": "Что входит в пакет участника",
                        "text": sample_text,
                    },
                    {
                        # "en": "Cost",
                        "ru": "Как получить пакет участника",
                        "text": sample_text,
                    },
                    {
                        # "en": "Medical certification",
                        "ru": "Требования к медицинской справке",
                        "text": sample_text,
                    },
                ]
            },
            {
                # "en": "Sport exhibition",
                "ru": "Спортивная выставка",
                "menu_items": [
                    {
                        # "en": "Expo",
                        "ru": "Экспо",
                        "text": sample_text,
                    },
                ]
            },
            {
                # "en": "Competition day",
                "ru": "День соревнования",
                "menu_items": [
                    {
                        # "en": "Start",
                        "ru": "Старт",
                        "text": sample_text,
                    },
                    {
                        # "en": "Finish",
                        "ru": "Финиш",
                        "text": sample_text,
                    },
                    {
                        # "en": "Pacemakers",
                        "ru": "Пейсмейкеры",
                        "text": sample_text,
                    },
                    {
                        # "en": "Medical help",
                        "ru": "Медицинская помощь",
                        "text": sample_text,
                    },
                ]
            },
            {
                # "en": "Where to stay",
                "ru": "Где разместиться",
                "text": sample_text,
            },
            {
                # "en": "Fans",
                "ru": "Болельщикам",
                "menu_items": [
                    {
                        # "en": "General info",
                        "ru": "Общие сведения",
                        "text": sample_text,
                    },
                    {
                        # "en": "Where to support the entrants",
                        "ru": "Где поддержать участников",
                        "text": sample_text,
                    },
                ]
            },
            {
                # "en": "Music",
                "ru": "Музыка",
                "text": sample_text,
            },
            {
                # "en": "Volunteers",
                "ru": "Волонтёрам",
                "text": sample_text,
            },
        ]
    }

    return JsonResponse(info)


def get_expo_info(req):
    expo = {
        "map": "http://server/someimg.png",
        "stands": [
            {
                "name": "Coca-cola",
                "website": "http://coca-cola.com",
                "description": "<b>lorem ipsum</b>",
                "categories": ["еда",],
                "topLeft": [0,0],
                "size": [100, 100],
            },
            {
                "name": "Nike",
                "website": "http://nike.com",
                "description": "<b>lorem ipsum</b>",
                "categories": ["экипировка", "одежда"],
                "topLeft": [550, 30],
                "size": [200, 20],
            },
        ]
    }

    return JsonResponse(expo)


def get_start_region_map(req, id):
    route = MarathonRoute.objects.get(pk=id)

    return HttpResponseRedirect(route.map.url)


def get_finish_region_map(req, id):
    route = MarathonRoute.objects.get(pk=id)

    return HttpResponseRedirect(route.map.url)


def get_photo_frames(req):
    return JsonResponse({})

