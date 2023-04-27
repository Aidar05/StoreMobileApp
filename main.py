from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox


# on_touch_down: app.Btn_Press_Filter(*args)

root_width = 330
root_height = 580 


Config.set('graphics', 'width', root_width)
Config.set('graphics', 'height', root_height)


class Main(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


class Notebooks(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


class WindowsManager(ScreenManager):
    pass


class FilterWindow(Popup):
    pass


class StoreApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Main(name='main'))
        self.screen_manager.add_widget(Notebooks(name='notebooks'))
        return self.screen_manager
    
    # def Btn_Press_Filter(self, instance, touch):
    #     if instance.collide_point(*touch.pos):
    #         if self.screen_manager.current == 'main':
    #             self.screen_manager.current = 'notebooks'
    #         elif self.screen_manager.current == 'notebooks':
    #             self.screen_manager.current = 'main'

    def OpenFilter(self):
        self.popup = FilterWindow()
        self.popup.open()

    def CloseFilter(self):
        self.popup.dismiss()

kv = Builder.load_file('kivy.kv')


if __name__ == '__main__':
    StoreApp().run()
