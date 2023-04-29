# Импорт нужных частей модуля  
from kivy.app import App 
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox


# Описываю ширину и высоту окна приложения 
root_width = 330
root_height = 580 


# Меняю размеры окна ранее выбранные 
Config.set('graphics', 'width', root_width)
Config.set('graphics', 'height', root_height)


# Класс для главного экрана
class Main(Screen):
    pass

# Класс для экрана с ноутбуками.  
class Notebooks(Screen):
    # Еще одна инициализация класса
    def __init__(self, **kw):
        super().__init__(**kw)


class SignIn(Screen):
    pass


# Класс чтобы мэнэджить все окна
class WindowsManager(ScreenManager):
    pass


# Класс для выпадающего окошка. Фильтр пойска 
class FilterWindow(Popup):
    pass


# Класс моего приложения 
class StoreApp(App):
    # Необходимый метод билд который тригериться в начале приложния
    def build(self):
        # Создаем instance менеджера скринов и добавляем в него все окна
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Main(name='main'))
        self.screen_manager.add_widget(SignIn(name='sign_in'))
        self.screen_manager.add_widget(Notebooks(name='notebooks'))
        return self.screen_manager    # Возвращаем главный экран
    
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


# Срабатывает только если он запускается как главный процесс на прямую
if __name__ == '__main__':
    StoreApp().run()
