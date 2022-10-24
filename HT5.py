import datetime
import random


class Publication:
    def __init__(self, title):
        self.title = title

    def get_publication_text(self):
        body = input('Type text: ')
        return body

    def write_to_list(self, publication_list):
        publication_list.insert(0, pub.title)
        publication_list.insert(1, self.get_publication_text())
        return publication_list

    def write_to_file(self, publicution_list):
        file = open('myfile.txt', 'a+')
        file.write('---------------------------------' + '\n')
        file.write(f'{publicution_list[0]}\n{publicution_list[1]}\n{publicution_list[2]}\n')
        file.write('---------------------------------' + '\n\n')


class News(Publication):
    def __init__(self, title, publish_datetime):
        Publication.__init__(self, title=title)
        self.publish_datetime = publish_datetime

    def get_publish_date(self):
        return self.publish_datetime.strftime('%Y-%m-%d %H:%M')

    def get_news_location(self):
        location = input('Type city name: ')
        return location

    def write_to_list_news(self, publication_list, location):
        publication_list.append(f'{location}, {self.get_publish_date()}')
        return publication_list


class Advertising(Publication):
    def __init__(self, title):
        Publication.__init__(self, title=title)

    @property
    def get_due_date(self):
        print('Type advertising expiration date')
        # exp_year = int(input('Enter a year: '))
        while True:
            exp_year = int(input('Enter a year: '))
            if 2020 < exp_year <= 2030:
                break
            print('Year must be between 2021 and 2030')
        while True:
            exp_month = int(input('Enter a month: '))
            if 1 <= exp_month <= 12:
                break
            print('Month must be a number between 1 and 12')
        while True:
            exp_day = int(input('Enter a day: '))
            if 1 <= exp_day <= 31:
                break
            print('Day must be a number between 1 and 31')
        exp_date = datetime.date(exp_year, exp_month, exp_day)
        print('Expiration date is ', exp_date)
        date_diff = datetime.date(exp_year, exp_month, exp_day) - datetime.date.today()
        if date_diff.days < 0:
            print('Your advertising is expired')
            exit()
        return f'Actual until: {exp_date}, {date_diff.days} days left'

    def write_to_list_ad(self, publication_list):
        publication_list.append(self.get_due_date)
        return publication_list


class Joke(Publication):
    def __init__(self, title):
        Publication.__init__(self, title=title)

    def generate_random_funny_meter(self):
        value_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        return value_list[random.randint(0, 9)]

    def write_to_list_joke(self, publication_list):
        publication_list.append(f'Funny meter – {self.generate_random_funny_meter()} of Ten')
        return publication_list


def check_record_type(input_index):
    if input_index > len(record_type) - 1:
        print('Invalid record type')
        exit()
    return record_type[input_index]


pub_list = []

""" to input type of record """
record_type = ['News', 'Advertising', 'Joke']
print('Select type of new record:')
for num, record in enumerate(record_type):
    print(num, record)

record_type_index = int(input(f'Select value between 0 and {len(record_type) - 1}: '))
print('You selection is ', check_record_type(record_type_index))


if record_type_index == 0:
    pub = News(record_type[record_type_index], datetime.datetime.now())
    inp_location = pub.get_news_location()
    pub.write_to_list_news(pub_list, inp_location)
elif record_type_index == 1:
    pub = Advertising(record_type[record_type_index])
    pub.write_to_list_ad(pub_list)
elif record_type_index == 2:
    pub = Joke(record_type[record_type_index])
    pub.write_to_list_joke(pub_list)
else:
    print('Something went wrong...')


pub.write_to_file(pub.write_to_list(pub_list))
