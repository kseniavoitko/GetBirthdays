from datetime import datetime
from collections import defaultdict


employees = [{'name': 'Liza', 'birthdate': datetime(1997, 1, 1)},
             {'name': 'Nick', 'birthdate': datetime(1970, 7, 2)},
             {'name': 'Max', 'birthdate': '28.06.2001'},
             {'name': 'Alex', 'birthdate': datetime(1970, 7, 3)},
             {'name': 'Alina', 'birthdate': datetime(1995, 6, 26)},
             {'name': 'Michael', 'birthdate': datetime(1975, 6, 25)},
             {'name': 'Robert', 'birthdate': datetime(1985, 7, 1)}]


def get_birthdays_per_week(employees: list) -> None:
    current_datetime = datetime.now()
    current_year = current_datetime.year
    result = defaultdict(list)
    for employee in employees:
        birthday = employee['birthdate']
        if type(birthday) is str:
            birthday = datetime.strptime(birthday, '%d.%m.%Y')
        birthday = birthday.replace(year = current_year) if birthday.month != 1 else birthday.replace(year = current_year + 1)
        if 0 <= (birthday - current_datetime).days < 7:
            birthday_weekday = birthday.weekday()
            if birthday_weekday == 5:
                result[(birthday.replace(day = birthday.day + 2), 'Monday')].append(employee['name'])
            elif birthday_weekday == 6:
                result[(birthday.replace(day = birthday.day + 1), 'Monday')].append(employee['name'])
            else:
                result[(birthday, birthday.strftime("%A"))].append(employee['name'])

    result_keys = list(result.keys())
    result_keys.sort()
    result = {i: result[i] for i in result_keys}
    
    return result


if __name__ == '__main__':
    for key, value in get_birthdays_per_week(employees).items():
        print(f"{key[1]}: {', '.join(value)}")