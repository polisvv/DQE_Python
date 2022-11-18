import os
import random
import datetime
import normalization.HT6 as norm


class Publication:
    def __init__(self, publication_type: str) -> None:
        self.publication_type = publication_type


class News(Publication):
    def __init__(self, publish_datetime, publication_type, location: str = "") -> None:
        super().__init__(publication_type=publication_type)
        # self.publication_type = publication_type
        self.publish_datetime = publish_datetime
        self.location = location

    def get_publish_date(self):
        return self.publish_datetime.strftime('%Y-%m-%d %H:%M')

    def get_news_location(self):
        location = input('Type city name: ')
        return location


class Ad(Publication):
    def __init__(self, publication_type, expiration_date: str = "") -> None:
        Publication.__init__(self, publication_type=publication_type)
        self.expiration_date = expiration_date

    def get_due_date(self):
        print('Type advertising expiration date')
        # exp_year = int(input('Enter a year: '))
        while True:
            exp_year = int(input('Enter a year: '))
            if 2020 < exp_year <= 2024:
                break
            print('Year must be between 2021 and 2024')
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
        expiration_date = f'Actual until: {exp_date}, {date_diff.days} days left'
        if date_diff.days < 0:
            print('Your advertising is expired. It will not be published.')
            exit()
        return expiration_date


class Joke(Publication):
    def __init__(self, publication_type, funny_meter: str = "") -> None:
        super().__init__(publication_type=publication_type)
        self.funny_meter = funny_meter

    def generate_random_funny_meter(self):
        value_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        return f'Funny meter – {value_list[random.randint(0, 9)]} of Ten'


class Reader:
    def __init__(self, publication_method):
        self.publication_method = publication_method

    def read_from_file(self, fname):
        with open(fname) as file:
            input_list = file.readlines()
            input_list = [row.replace('\n','') for row in input_list]
        while True:
            if self.is_valid_file_format(input_list):
                return input_list

    def is_valid_file_name(self, fname):
        txt_file_list = [file for file in os.listdir() if file.endswith(".txt")]
        if fname in txt_file_list:
            if os.path.getsize(fname) > 0:
                return True
            else:
                print("File format is empty.\nPlease check folder templates_for_adding_publication for correct format.")
        else:
            print("File with this name is not exist. Try again.")

    def is_valid_file_format(self, input_list):
        if "Publication_Type: " in input_list[0] and "Body: " in input_list[1]:
            return True
        else:
            print("File format is invalid.\nPlease check folder templates_for_adding_publication for correct format.")
            self.get_file_name()

    def get_file_name(self):
        while True:
            file_name = f'{input("Please give name of txt file: ")}.txt'
            if self.is_valid_file_name(file_name):
                print(f"You selected file is {file_name}")
                return file_name

    def get_publication_type(self, publication_method, inp_list):
        if publication_method == "txt":
            return self.get_publication_type_from_file(inp_list)
        elif publication_method == "cli":
            return self.get_publication_type_from_cli()

    def get_publication_type_from_file(self, inp_list):
        if "News" in inp_list[0]:
            print("Your publication type is News")
            return News(publish_datetime=datetime.datetime.now(), publication_type="News")
        elif "Private Ad" in inp_list[0]:
            print("Your publication type is Ad")
            return Ad(publication_type="Ad")
        elif "Joke" in inp_list[0]:
            print("Your publication type is Joke")
            return Joke(publication_type="Joke")
        else:
            print(f"Invalid file format. Correct format is:\n\tPublication_Type: \n\tBody: \n\tCity: or Expiration_Day:")

    def __is_valid_publication_type(self, publication_type):
        if publication_type not in  ["1", "2", "3"]:
            print('Invalid record type')
        return publication_type

    def get_publication_type_from_cli(self):
        while True:
            publication_type = input("What are you going to publish?\n1 - News\n2 - Ad\n3 - Joke\n")
            if self.__is_valid_publication_type(publication_type):
                if publication_type == "1":
                    return News(publish_datetime=datetime.datetime.now(), publication_type="News")
                elif publication_type == "2":
                    return Ad(publication_type="Ad")
                elif publication_type == "3":
                    return Joke(publication_type="Joke")
            else:
                print("Wrong format. Please try again.")

    def get_publication_text(self, publication_method, inp_list):
        if publication_method == "txt":
            return self.__get_publication_text_txt(inp_list)
        elif publication_method == "cli":
            return self.__get_publication_text_cli()

    def __get_publication_text_cli(self):
        body = input('Type text: ')
        return body

    def __get_publication_text_txt(self, inp_list):
        body = inp_list[1][inp_list[1].index(': ') + 2:]
        print(f"Publication text is:\n\t{body}")
        return body

    def get_publication_specific_info(self, publication_method: str, publication, inp_list) -> str:
        if publication_method == "txt":
            return self.__add_publication_specific_info_txt(publication, inp_list)
        elif publication_method == "cli":
            return self.__add_publication_specific_info_cli(publication)

    def __add_publication_specific_info_txt(self, publication: Publication, inp_list) -> str:
        if publication.publication_type == "News":
            publication.location = inp_list[2][inp_list[2].index(': ') + 2:]
            print(f"News location is {publication.location}")
            return publication.location
        elif publication.publication_type == "Ad":
            exp_date = inp_list[2][inp_list[2].index(': ') + 2:]
            exp_date = datetime.datetime.strptime(exp_date, "%Y-%m-%d").date()
            date_diff = exp_date - datetime.date.today()
            if date_diff.days < 0:
                print('Your advertising is expired. It will not be published.')
                exit()
            publication.expiration_date = f'Actual until: {exp_date}, {date_diff.days} days left'
        elif publication.publication_type == "Joke":
            publication.funny_meter = publication.generate_random_funny_meter()
            print(publication.funny_meter)

    def __add_publication_specific_info_cli(self, publication: Publication) -> str:
        if publication.publication_type == "News":
            publication.location = publication.get_news_location()
        elif publication.publication_type == "Ad":
            publication.expiration_date = publication.get_due_date()
            print(publication.expiration_date)
        elif publication.publication_type == "Joke":
            publication.funny_meter = publication.generate_random_funny_meter()
            print(publication.funny_meter)


def write_to_list(publication, body):
    publication_list = []
    publication_list.insert(0, publication.publication_type)
    publication_list.insert(1, body)
    if publication.publication_type == "News":
        publication_list.insert(2, f'{publication.location}, {publication.get_publish_date()}')
    elif publication.publication_type == "Ad":
        publication_list.insert(2, publication.expiration_date)
    elif publication.publication_type == "Joke":
        publication_list.insert(2, publication.funny_meter)
    return publication_list

def write_to_file(publication_list):
    file = open('myfile.txt', 'a+')
    file.write('---------------------------------' + '\n')
    file.write(f'{publication_list[0]}\n{publication_list[1]}\n{publication_list[2]}\n')
    file.write('---------------------------------' + '\n\n')
    print(f"\nYou publication was added successfully.")

def get_publication_method():
    while True:
        publication_method = input("Please select publication method\n1 - via txt file\n2 - type via cli\n")
        if publication_method == "1":
            return "txt"
        elif publication_method == "2":
            return "cli"
        else:
            print("Wrong format. Please try again or Ctrl+C to exit.")

pub_method = get_publication_method()
pub = Reader(pub_method)

file_name = ""
if pub_method == "txt":
    file_name = pub.get_file_name()
    pub_list_from_file = pub.read_from_file(file_name)
else:
    pub_list_from_file = None

pub_type = pub.get_publication_type(pub_method, pub_list_from_file)
pub_body = pub.get_publication_text(pub_method, pub_list_from_file)
pub.get_publication_specific_info(pub_method, pub_type, pub_list_from_file)
write_to_file(norm.capitalize_and_append_sent(write_to_list(pub_type, pub_body)))

if file_name:
    os.remove(file_name)
    print(f"File {file_name} was deleted.")
