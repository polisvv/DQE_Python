import os
import random
import datetime
import normalization.HT6 as norm
import typing
import csv


class Publication:
    def __init__(self, publication_type: str, publication_body: str = "") -> None:
        self.publication_type = publication_type
        self.publication_body = publication_body


class News(Publication):
    def __init__(self, publish_datetime, publication_type, publication_body: str = "", location: str = "") -> None:
        super().__init__(publication_type=publication_type, publication_body=publication_body)
        self.publish_datetime = publish_datetime
        self.location = location

    def get_publish_date(self):
        return self.publish_datetime.strftime('%Y-%m-%d %H:%M')

    @staticmethod
    def get_news_location():
        location = input('Type city name: ')
        return location


class Ad(Publication):
    def __init__(self, publication_type, publication_body: str = "", expiration_date: str = "") -> None:
        Publication.__init__(self, publication_type=publication_type, publication_body=publication_body)
        self.expiration_date = expiration_date

    @staticmethod
    def get_due_date():
        print('Type advertising expiration date')
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
    def __init__(self, publication_type, publication_body: str = "", funny_meter: str = "") -> None:
        super().__init__(publication_type=publication_type, publication_body=publication_body)
        self.funny_meter = funny_meter

    @staticmethod
    def generate_random_funny_meter():
        value_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
        return f'Funny meter – {value_list[random.randint(0, 9)]} of Ten'


class Reader:
    def __init__(self, publication_method):
        self.publication_method = publication_method


class ReaderCli(Reader):
    def __init__(self):
        super().__init__(publication_method="cli")

    @staticmethod
    def __is_valid_publication_type(publication_type):
        if publication_type not in ["1", "2", "3"]:
            print('Invalid record type')
        return publication_type

    def get_publication_type(self):
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

    @staticmethod
    def get_publication_text():
        body = input('Type text: ')
        return body

    @staticmethod
    def get_publication_specific_info(publication: typing.Union[News, Ad, Joke]) -> None:
        if publication.publication_type == "News":
            publication.location = publication.get_news_location()
        elif publication.publication_type == "Ad":
            publication.expiration_date = publication.get_due_date()
            print(publication.expiration_date)
        elif publication.publication_type == "Joke":
            publication.funny_meter = publication.generate_random_funny_meter()
            print(publication.funny_meter)


class ReaderTxt(Reader):
    def __init__(self):
        super().__init__(publication_method="txt")
        self.file_name = ""
        self.input_list = []

    def __is_valid_file_name(self, fname):
        txt_file_list = [file for file in os.listdir() if file.endswith(f".{self.publication_method}")]
        if fname in txt_file_list:
            if os.path.getsize(fname) > 0:
                return True
            else:
                print("File format is empty.\nPlease check folder templates_for_adding_publication for correct format.")
        else:
            print("File with this name is not exist. Try again.")

    def get_file_name(self):
        while True:
            fname = f'{input("Please give name of txt file: ")}.{self.publication_method}'
            if self.__is_valid_file_name(fname):
                print(f"You selected file is {fname}")
                return fname

    def read_from_txt(self):
        with open(f"{self.file_name}") as file:
            input_list = file.readlines()
            input_list = [row.replace('\n', '') for row in input_list]
        while True:
            if self.__is_valid_txt_format(input_list):
                return input_list

    def __is_valid_txt_format(self, input_list):
        if "Publication_Type: " in input_list[0] and "Body: " in input_list[1]:
            return True
        else:
            print("File format is invalid.\nPlease check folder templates_for_adding_publication for correct format.")
            self.get_file_name()

    def get_publication_type(self):
        if "News" in self.input_list[0]:
            print("Your publication type is News")
            return News(publish_datetime=datetime.datetime.now(), publication_type="News")
        elif "Private Ad" in self.input_list[0]:
            print("Your publication type is Ad")
            return Ad(publication_type="Ad")
        elif "Joke" in self.input_list[0]:
            print("Your publication type is Joke")
            return Joke(publication_type="Joke")
        else:
            print(
                f"Invalid file format. Correct format is:\n\tPublication_Type: \n\tBody: \n\tCity: or Expiration_Day:")

    def get_publication_text(self):
        body = self.input_list[1][self.input_list[1].index(': ') + 2:]
        print(f"Publication text is:\n\t{body}")
        return body

    def get_publication_specific_info(self, publication: typing.Union[News, Ad, Joke]) -> None:
        if publication.publication_type == "News":
            publication.location = self.input_list[2][self.input_list[2].index(': ') + 2:]
            print(f"News location is {publication.location}")
            return publication.location
        elif publication.publication_type == "Ad":
            exp_date = self.input_list[2][self.input_list[2].index(': ') + 2:]
            exp_date = datetime.datetime.strptime(exp_date, "%Y-%m-%d").date()
            date_diff = exp_date - datetime.date.today()
            if date_diff.days < 0:
                print('Your advertising is expired. It will not be published.')
                exit()
            publication.expiration_date = f'Actual until: {exp_date}, {date_diff.days} days left'
        elif publication.publication_type == "Joke":
            publication.funny_meter = publication.generate_random_funny_meter()
            print(publication.funny_meter)


class Counter:
    def __init__(self, file_to_count):
        self.file_to_count = file_to_count
        self.file_size_before = 0
        self.file_size_after = 0
        self.words_dict = {}
        self.letter_dict = {}

    def get_file_size(self):
        return os.path.getsize(f"{self.file_to_count}")

    def check_file_change(self):
        if self.file_size_before != self.file_size_after:
            # print("File was changed")
            self.words_dict = self.__count_words_from_final_file()
            self.letter_dict = self.__count_letters_from_final_file()
            self.__save_words_cnt_to_csv()
            self.__save_letter_cnt_to_csv()

    def __count_words_from_final_file(self):
        with open(f"{self.file_to_count}") as file:
            word_list = [word.lower() for line in file for word in line.split() if word.isalnum()]
        words_dict = {i: word_list.count(i) for i in sorted(word_list)}
        return words_dict

    def __save_words_cnt_to_csv(self):
        with open('cnt_words.csv', 'w') as csvfile:
            for key in self.words_dict.keys():
                csvfile.write("%s- %s\n" % (key, self.words_dict[key]))             #delimiter is "-" as it was requested in russian version of lesson

    def __count_letters_from_final_file(self):
        with open(f"{self.file_to_count}") as file:
            letter_list = [word for line in file for word in line if word.isalpha()]
        l_dict = {i.lower(): [letter_list.count(i.upper()) + letter_list.count(i.lower()),
                              letter_list.count(i.upper()),
                              f"{round(letter_list.count(i.upper()) / (letter_list.count(i.upper()) + letter_list.count(i.lower())), 2)} %"]
                  for i in sorted(letter_list)}
        return l_dict

    def __save_letter_cnt_to_csv(self):
        with open('cnt_letters.csv', 'w', newline='') as csvfile:
            dw = csv.writer(csvfile, delimiter=',')
            dw.writerow(["letter", "count_all", "count_uppercase", "percentage"])
            dw.writerows(
                [letter, self.letter_dict.get(letter, '0')[0], self.letter_dict.get(letter, '0')[1],
                 self.letter_dict.get(letter, '0.0 %')[2]]
                for letter in self.letter_dict.keys())


def get_publication_method():
    while True:
        publication_method = input("Please select publication method\n1 - type via cli\n2 - via txt file\n")
        if publication_method == "1":
            return ReaderCli()
        elif publication_method == "2":
            return ReaderTxt()
        else:
            print("Wrong format. Please try again or Ctrl+C to exit.")


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


counter = Counter("myfile.txt")
counter.file_size_before = counter.get_file_size()

reader = get_publication_method()

reader.file_name = ""

if reader.publication_method == "txt":
    reader.file_name = reader.get_file_name()
    reader.input_list = reader.read_from_txt()

pub = reader.get_publication_type()
pub.publication_body = reader.get_publication_text()
reader.get_publication_specific_info(pub)
write_to_file(norm.capitalize_and_append_sent(write_to_list(pub, pub.publication_body)))

counter.file_size_after = counter.get_file_size()
counter.check_file_change()

if reader.file_name:
    os.remove(reader.file_name)
    print(f"File {reader.file_name} was deleted.")
