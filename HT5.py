import datetime
import random


class Publication:
    def __init__(self, title):
        self.title = title

    def get_publication_text(self):
        body = input('Type text: ')
        return body

    def write_to_list(self):
        pub_list.insert(0, pub.title)
        pub_list.insert(1, self.get_publication_text())
        return pub_list

    def write_to_file(self, l1):
        file = open('myfile.txt', 'a+')
        file.write('---------------------------------' + '\n')
        file.write(f'{l1[0]}\n{l1[1]}\n{l1[2]}\n')
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

    def write_to_list_news(self):
        pub_list.append(f'{inp_location}, {self.get_publish_date()}')
        return pub_list


class Advertising(Publication):
    def __init__(self, title):
        Publication.__init__(self, title=title)

    def get_due_date(self):
        print('Type advertising expiration date')
        exp_year = int(input('Enter a year: '))
        exp_month = int(input('Enter a month: '))
        exp_day = int(input('Enter a day: '))
        exp_date = datetime.date(exp_year, exp_month, exp_day)
        print('Expiration date is ', exp_date)
        date_diff = datetime.date(exp_year, exp_month, exp_day) - datetime.date.today()
        if date_diff.days < 0:
            print('Your advertising is expired')
            exit()
        return f'Actual until: {exp_date}, {date_diff.days} days left'

    def write_to_list_ad(self):
        pub_list.append(self.get_due_date())
        return pub_list


class Joke(Publication):
    def __init__(self, title):
        Publication.__init__(self, title=title)

    def generate_random_funny_meter(self):
        value_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        return value_list[random.randint(0, 9)]

    def write_to_list_joke(self):
        pub_list.append(f'Funny meter – {self.generate_random_funny_meter()} of Ten')
        return pub_list


def check_record_type(input_index):
    if input_index > len(record_type) - 1:
        print('Invalid record type')
        exit()
    return record_type[input_index]


pub_list = []

""" to input type of record """
record_type = ['News', 'Advertising', 'Joke']
print('Select type of new record:')
# i = 0
for num, record in enumerate(record_type):
    print(num, record)
    # i = i + 1

record_type_index = int(input(f'Select value between 0 and {len(record_type) - 1}: '))
print('You selection is ', check_record_type(record_type_index))


if record_type_index == 0:
    pub = News(record_type[record_type_index], datetime.datetime.now())
    inp_location = pub.get_news_location()
    pub.write_to_list_news()
elif record_type_index == 1:
    pub = Advertising(record_type[record_type_index])
    pub.write_to_list_ad()
elif record_type_index == 2:
    pub = Joke(record_type[record_type_index])
    pub.write_to_list_joke()
else:
    print('Something went wrong...')


pub.write_to_file(pub.write_to_list())
