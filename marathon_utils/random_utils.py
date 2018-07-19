# -*- coding: utf-8

from random import randrange, randint, choice
import datetime


def irandom_date(start, count):
    current = start
    while count >= 0:
        curr = current + datetime.timedelta(minutes=randrange(60))
        yield curr
        count -= 1


def random_datetime(from_time=datetime.datetime.now(), to_time=None, step=60*60*24):
    if not to_time:
        return from_time + datetime.timedelta(seconds=randrange(step))
    else:
        return from_time + datetime.timedelta(seconds=randint(0, int((to_time - from_time).total_seconds())))


def random_email(name, surname):
    return "{}.{}@yandex.ru".format(name, surname)


def random_phone():
    return "+{} ({:03d}) {:03d}-{:02d}-{:02d}".format(randint(1, 9), randint(0, 999), randint(0, 999),
                                               randint(0, 99), randint(0, 99))


def random_citizenship():
    return choice(['Россия', 'Германия', 'Япония', 'США'])


def random_city():
    return choice(['Москва', 'Лондон', 'Париж', 'Минск', 'Вашингтон', 'Сан-Диего', 'Токио'])


def random_club():
    # return choice(['勝利', 'City Wolfes', 'Изо-студия "Пальма"', 'Депутаты Гос Думы', 'Цифры 123 и Запятые ,./'])
    return choice(['City Wolfes', 'Беговой клуб А'])
