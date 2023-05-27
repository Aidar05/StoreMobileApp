from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder 
from kivymd.uix.list import OneLineListItem
from kivy.properties import StringProperty


import mysql.connector


db = mysql.connector.connect(user='root', password='',
                             host='localhost', database='mess')

db_second = mysql.connector.connect(user='root', password='',
                                    host='localhost', database='user_account_data')

count = 2

class SpeedType(Screen):
    def game_start(self):
        self.ids.speedtype.data = []

        global count

        def add_user_name(word):
            self.ids.speedtype.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "text": word,
                    "callback": lambda x: x,
                }
            )

        cursor = db.cursor()

        cursor.execute('select word from words')

        words = cursor.fetchall()

        for i in range(count):
            print(words[i][0])
            add_user_name(words[i][0])
        count+=2


class Profile(Screen):
    pass


class CustomOneLineIconListItem(OneLineListItem):
    icon = StringProperty()


class Main(Screen):    
    pass


class SignIn(Screen):
    def check_account(self):
        data = [self.ids.login.text, self.ids.password.text]

        cursor = db_second.cursor()

        cmd = 'select email, pass from data '

        cursor.execute(cmd)

        result = cursor.fetchall()

        count = 0
        for i in result:
            if i[0] == data[0]:
                count += 1
                if i[1] == data[1]:
                    print('logged in')
                    break
                else: 
                    self.ids.password.error = True
            else: 
                pass
        
        if count == 0:
            self.ids.login.error = True


class SignUp(Screen):
    def create_account(self):
        user_data = [self.ids.name.text, self.ids.last_name.text,
                    self.ids.gender.text, self.ids.age.text,
                    self.ids.login.text, self.ids.password.text] 

        cursor = db_second.cursor() 

        cmd = 'insert into data (name, surname, gender, age, email, pass) values (%s, %s, %s, %s, %s, %s)'
    
        cursor.execute(cmd, user_data)

        db_second.commit()

        cursor.close()


class Profile(Screen):
    pass


class Settings(Screen):
    pass


class Chosen(Screen):
    pass


# class MusNote(Screen):
#     pass

class Settings(Settings):
    pass


class MessApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'

        self.main = Main()

        self.sc = ScreenManager()
        # self.sc.add_widget(MusNote(names='MusNote'))
        self.sc.add_widget(Main(name='main'))
        self.sc.add_widget(SpeedType(name='SpeedType'))
        self.sc.add_widget(Chosen(name='chosen'))
        self.sc.add_widget(Profile(name='profile'))
        self.sc.add_widget(SignUp(name='sign_up'))
        self.sc.add_widget(SignIn(name='sign_in'))
        # self.sc.add_widget(Settings(name='settings'))
        return self.sc

    def theme_yellow(self):
        self.theme_cls.primary_palette = 'LightGreen'

    def screen_main(self):
        self.sc.current = 'main'

    def screen_main_s(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.sc.current = 'main'

    def screen_sign_in(self):
        self.sc.current = 'sign_in'

    def screen_sign_in_s(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.sc.current = 'sign_in'

    def screen_sign_up(self):
        self.sc.current = 'sign_up'

    def screen_sign_up_s(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.sc.current = 'sign_up'

    def screen_SpeedType(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.sc.current = 'SpeedType'

    def screen_chosen(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.sc.current = 'chosen'

    def screen_profile(self):
        self.sc.current = 'profile'

    def screen_settings(self):
        pass
    
kv = Builder.load_file('kivy_files/main.kv')
# kv = Builder.load_file('kivy_files/MusNote.kv')
kv = Builder.load_file('kivy_files/sign_in.kv')
kv = Builder.load_file('kivy_files/sign_up.kv')
kv = Builder.load_file('kivy_files/profile.kv')
kv = Builder.load_file('kivy_files/settings.kv')
kv = Builder.load_file('kivy_files/asdf.kv')
kv = Builder.load_file('kivy_files/speedtype.kv')

if __name__ == '__main__':
    MessApp().run()
