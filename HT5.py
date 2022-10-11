import datetime
import random


class Publication:
    def __init__(self, name):
        self.name = name

    def get_publication_text(self):
        txt = input('Type text: ')
        return txt

    def write_to_list(self):
        pub_list.insert(0, pub.name)
        pub_list.insert(1, self.get_publication_text())
        return pub_list

    def write_to_file(self, l1):
        file = open('myfile.txt', 'a+')
        file.write('---------------------------------' + '\n')
        file.write(l1[0] + '\n' + l1[1] + '\n' + l1[2] + '\n')
        file.write('---------------------------------' + '\n\n')


class News(Publication):
    def __init__(self, name, publish_datetime):
        Publication.__init__(self, name=name)
        self.publish_datetime = publish_datetime

    def get_publish_date(self):
        return self.publish_datetime.strftime('%Y-%m-%d %H:%M')

    def news_location(self):
        location = input('Type city name: ')
        return location

    def write_to_list_news(self):
        pub_list.append(inp_location + ', ' + self.get_publish_date())
        return pub_list


class Advertising(Publication):
    def __init__(self, name):
        Publication.__init__(self, name=name)

    def due_date(self):
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
        return 'Actual until: ' + str(exp_date) + ', ' + str(date_diff.days) + ' days left'

    def write_to_list_ad(self):
        pub_list.append(self.due_date())
        return pub_list


class Joke(Publication):
    def __init__(self, name):
        Publication.__init__(self, name=name)

    def random_funny_meter(self):
        value_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        return value_list[random.randint(0, 9)]

    def write_to_list_joke(self):
        pub_list.append(f'Funny meter – {self.random_funny_meter()} of Ten')
        return pub_list


def check_record_type(input_index):
    if input_index == 0 or input_index >= len(record_type):
        print('Invalid record type')
        exit()
    return record_type[input_index]


pub_list = []

""" to input type of record """
record_type = [None, 'News', 'Advertising', 'Joke']  # None just for start from 1 index
print('Select type of new record:')
i = 1
while i < len(record_type):
    print(i, '-', record_type[i])
    i = i + 1

record_type_index = int(input(f'Select value between 1 and {len(record_type) - 1}: '))
print('You selection is ', check_record_type(record_type_index))
inp_name = input('Type publication name: ')

if record_type_index == 1:
    pub = News(inp_name, datetime.datetime.now())
    inp_location = pub.news_location()
    pub.write_to_list_news()
elif record_type_index == 2:
    pub = Advertising(inp_name)
    pub.write_to_list_ad()
elif record_type_index == 3:
    pub = Joke(inp_name)
    pub.write_to_list_joke()
else:
    print('Something went wrong...')

pub.write_to_file(pub.write_to_list())
