# Импорт нужных частей модуля
import kivymd  
from kivymd.app import MDApp 
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.core.window import Window

import mysql.connector


db = mysql.connector.connect(user='root',
                              password='',
                              host='localhost',
                              database='user_data')


# Описываю ширину и высоту окна при ложения 
root_width = 330
root_height = 580 


# Меняю размеры окна ранее выбранные
Window.size = (root_width, root_height)


# Класс для главного экрана
class Main(Screen):
    pass

# Класс для экрана с ноутбуками.  
class Notebooks(Screen):
    # Еще одна инициализация класса
    def __init__(self, **kw):
        super().__init__(**kw)


class SignUp(Screen):
    def user_data_insert(self):
        user_data = [self.ids.user_name.text,
                     self.ids.user_last_name.text,
                     self.ids.user_login_number.text,
                     self.ids.user_password.text
                    ]
        print(user_data)

        cursor = db.cursor()

        cmd = 'insert into data (name, last_name, login, password) values (%s, %s, %s, %s)'

        cursor.execute(cmd, user_data)

        db.commit()

        cursor.close()

class SignIn(Screen):
    def user_data_check(self):
        cursor = db.cursor()

        cmd = 'select * from data'

        cursor.execute(cmd)
        data = cursor.fetchall()

        for i in data:
            print(f'login,  {i[3]}')
            print(f'password,  {i[4]}')

        cursor.close()
        print('Checking...')


# Класс чтобы мэнэджить все окна
class WindowsManager(ScreenManager):
    pass


# Класс для выпадающего окошка. Фильтр пойска 
class FilterWindow(Popup):
    pass


# Класс моего приложения 
class StoreApp(MDApp):
    # Необходимый метод билд который тригериться в начале приложния
    def build(self):
        self.theme_cls.primary_palette = 'LightBlue'

        # Создаем instance менеджера скринов и добавляем в него все окна
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(SignUp(name='sign_up'))
        self.screen_manager.add_widget(SignIn(name='sign_in'))
        self.screen_manager.add_widget(Main(name='main'))
        self.screen_manager.add_widget(Notebooks(name='notebooks'))
        return self.screen_manager    # Возвращаем главный экран
    
    def MainScreen(self):
        self.screen_manager.current = 'main'

    # Метод для открывания фильтра поиска. Тригериться при нажатия на кнопку в киви 
    def OpenFilter(self, instance, touch):
        # Окно фильтр открываеться только если нажали на саму кнопку 
        if instance.collide_point(*touch.pos):
            self.popup = FilterWindow()
            self.popup.open()

    # Закрывает фильтр окошко. Срабатывает при нажатии на подходящую кнопку в киви 
    def CloseFilter(self):
        self.popup.dismiss()


    def Profile(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # change screen 
            self.screen_manager.current = 'sign_in'

# Загружаем киви файл 
kv = Builder.load_file('kivy.kv')
kv = Builder.load_file('Sign_in.kv')
kv = Builder.load_file('Sign_up.kv')

# Срабатывает только если он запускается как главный процесс на прямую
if __name__ == '__main__':
    StoreApp().run()
