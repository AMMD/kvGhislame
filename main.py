import kivy

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.lang import Builder

from audiostrip import AudioStrip
Builder.load_file('audiostrip.kv')


class MenuButton(ToggleButton):
    pass

class Menu(BoxLayout):
    mix_b = ObjectProperty(MenuButton)
    odr_b = ObjectProperty(MenuButton)


class MainMix(Screen):
    drums = ObjectProperty(AudioStrip)
Builder.load_file('mainmix.kv')


class OrganicDrums(Screen):
    pass



class MainKvG(Widget):
    sm = ObjectProperty(ScreenManager)
    menu = ObjectProperty(Menu)
    mainmix = ObjectProperty(Screen)
    organicdrums = ObjectProperty(Screen)

    def change_tab(self, tab_name):
        self.sm.current = tab_name
        for child in self.children[:]:
            if isinstance(child, Menu):
                for kid in child.children[:]:
                    if (kid.text == tab_name) & isinstance(kid, MenuButton):
                        kid.state = 'down'



class kvGhislame(App):
    def build(self):
        return MainKvG()

if __name__ == "__main__":
    kvGhislame().run()
