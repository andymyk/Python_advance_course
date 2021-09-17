from telebot import TeleBot
from envparse import Env
from DBClient import DBClient

env = Env()
TOKEN = env.str("TOKEN")
bot = TeleBot(TOKEN)


class BotApi:

    MENU_STRING = "\n1 - работа с базой\n"

    def __init__(self, DBClient):
        self.DBClient = DBClient

    def setup_all_components(self):
        self.DBClient.setup(self)


    def check_active_status(self):
        self.DBClient.check_status_a(self)

    def check_personal(self):
        self.DBClient.check_p(self)

    def check_order(self):
        self.DBClient.check_d(self)

    def check_id(self):
        self.DBClient.check_id_o(self)

    def run(self):
        self.setup_all_components()

        choice_mapper = {"1": self.check_active_status,
                         "2": self.check_personal,
                         "3": self.check_order,
                         "4": self.check_id}

        while True:
            user_choice = input(f"Введите желаемое действие: {self.MENU_STRING}или q для выхода: ")
            if user_choice.lower() == "q":
                break
            elif user_choice == "1":
                user_choice = input(f"1 - Показать активные заявки\n2 - Перечень сотрудников и департаментов, в которых они работают"
                                    f"\n3 - количество заявок за '2021-09-07'\n4 - перечень заявок и ФИО сотрудников, которые их создали ")
                choice_mapper[user_choice]()

        print("Спасибо за пользованием нашим софтом!")

BotApi(DBClient=DBClient).run()