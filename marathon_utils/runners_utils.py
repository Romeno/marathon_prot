# -*- coding: utf-8

import csv
import names
import datetime
import random

if __name__ == "__main__":
    import date_utils as d_utils
    import random_utils as r_utils
else:
    from . import date_utils as d_utils
    from . import random_utils as r_utils


def generate_runners(count):
    """
    Generates list of random runners
    :param count: number of runners to generate
    :return: list of runners. runner is a list of properties
    """
    runners = []

    for i in range(count):
        dob = r_utils.random_datetime(datetime.datetime(year=1900, month=1, day=1), to_time=datetime.datetime.now())
        age = d_utils.calculate_age(dob)
        name = names.get_first_name()
        surname = names.get_last_name()
        reg_date1 = datetime.datetime.now()
        reg_date1 = reg_date1.replace(month=1, day=1)
        reg_date1 = r_utils.random_datetime(reg_date1, reg_date1.replace(year=reg_date1.year + 1))
        reg_date2 = r_utils.random_datetime(reg_date1, reg_date1.replace(year=reg_date1.year + 1))

        runners.append([
            i,                                                              # id_external
            name,                                                           # first_name
            surname,                                                        # last_name
            age,                                                            # age
            dob,                                                            # birthday
            random.choice(['M', 'F']),                                      # gender
            r_utils.random_email(name, surname),                            # email
            r_utils.random_citizenship(),                                   # citizenship
            r_utils.random_phone(),                                         # phone
            reg_date1,                                                      # user_register_date
            r_utils.random_phone(),                                         # second_phone
            r_utils.random_city(),                                          # city
            names.get_first_name(),                                         # emergency_contact
            r_utils.random_phone(),                                         # emergency_phone
            random.choice(['L', 'XL', 'M', 'S']),                           # t_shirt_size
            r_utils.random_club(),                                          # running_club
            random.randint(0, 1),                                           # is_disabled
            random.randint(0, 1),                                           # is_prof
            1 if age < 18 else 0,                                           # is_child
            random.randint(0, 1),                                           # is_elite
            reg_date2,                                                      # marathon_registration_datetime
            'Абсолют Московский Марафон',                                   # marathon
            random.choice(['10 км', '42,2 км Московский Марафон 2018']),    # route
            random.choice(['A', 'B', 'C', 'D', 'E', 'F']),                  # cluster_run_letter
            random.randint(0, 100000),                                      # runner_number
            random.randint(1, count + 1),                                   # place
        ])

    return runners


def write_runners(runners, file_into):
    """
    Writes runners into a file
    :param runners: runners to write
    :param file_into: filename string or file-like object
    :return: None
    """
    f = None
    try:
        if isinstance(file_into, str):
            f = open(file_into, mode='w', newline='', encoding='utf_8')
            csvwriter = csv.writer(f, delimiter=';',
                                   quotechar='|', quoting=csv.QUOTE_MINIMAL)
        else:
            csvwriter = csv.writer(file_into, delimiter=';',
                                   quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([
            'Id',
            'Имя',
            'Фамилия',
            'Возраст участника',
            'Дата рождения',
            'Пол',
            'E-mail',
            'Гражданство',
            'Телефон',
            'Дата регистрации',
            'Второй телефон',
            'Город',
            'Экстренный контакт',
            'Экстренный телефон',
            'Размер футболки',
            'Беговой клуб',
            'Является инвалидом',
            'Является профессиональным спортсменом',
            'Является ребёнком',
            'Является элитным спортсменом',
            'Дата и время регистрации на забег',
            'Название забега',
            'Дистанция',
            'Буква бегового кластера',
            'Номер участника',
            'Результат забега',
        ])

        for r in runners:
            out_r = r
            out_r[4] = out_r[4].strftime('%d.%m.%Y')
            out_r[9] = out_r[9].strftime('%d.%m.%Y')
            out_r[20] = out_r[20].strftime('%d.%m.%Y')
            csvwriter.writerow(out_r)
    finally:
        if f:
            f.close()


def read_runners(file_from):
    """
    Read runners from csv file
    :param file_from: filename string or file-like object
    :return: list of runners. runner is a list of properties
    """
    f = None
    try:
        if isinstance(file_from, str):
            f = open(file_from, newline='', encoding='utf_8')
            csvreader = csv.reader(f, delimiter=';', quotechar='|')
        else:
            csvreader = csv.reader(file_from, delimiter=';', quotechar='|')
        runners = list(csvreader)[1:]
        for runner in runners:
            runner[4] = datetime.datetime.strptime(runner[4], '%d.%m.%Y')
            runner[9] = datetime.datetime.strptime(runner[9], '%d.%m.%Y')
            runner[20] = datetime.datetime.strptime(runner[20], '%d.%m.%Y')
        return runners
    finally:
        if f:
            f.close()



if __name__ == "__main__":
    data = read_runners('f:\\Work\\Marathon\\марафон проект для посетителей и участников марафона\\registrations_from_runc.run.csv')
    for e in data[1:]:
        print(e)

    # runners = generate_runners(1000)
    # write_runners('f:\\Work\\Marathon\\марафон проект для посетителей и участников марафона\\sample_runners.csv', runners)