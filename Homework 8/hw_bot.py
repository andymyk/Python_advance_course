from telebot import TeleBot
from envparse import Env
from DBClient import DBClient
#
env = Env()
TOKEN = env.str("TOKEN")
bot = TeleBot(TOKEN)


class BotApi:

    MENU_STRING = "\n1 - работа с базой\n"

    def __init__(self, DBClient):
        self.DBClient = DBClient

    def setup_all_components(self):
        self.DBClient.setup()


    def check_active_status(self):
        self.DBClient.check_status_a()

    def check_personal(self):
        self.DBClient.check_p()

    def run(self):
        self.setup_all_components()

        choice_mapper = {"1": self.setup_all_components,
                         "2": self.check_active_status,
                         "3": self.check_personal}

        while True:
            user_choice = input(f"Введите желаемое действие: {self.MENU_STRING}или q для выхода: ")
            if user_choice.lower() == "q":
                break
            elif user_choice == "1":
                user_choice = input(f"1 - вывести все книги\n2 - добавить новую книгу\n3 - удалить книгу по id ")
                choice_mapper[user_choice]()

        print("Спасибо за пользованием нашим софтом!")


BotApi(DBClient=DBClient).run()