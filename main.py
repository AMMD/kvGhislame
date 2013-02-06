import kivy

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty
from kivy.app import App


class MenuButton(ToggleButton):
    pass

class MainMix(Screen):
    pass

class OrganicDrums(Screen):
    pass



class MainKvG(Widget):
    sm = ObjectProperty(ScreenManager)
    menu = ObjectProperty(BoxLayout)
    mainmix = ObjectProperty(Screen)
    organicdrums = ObjectProperty(Screen)

    def change_tab(self, tab_name):
        self.sm.current(tab_name)



class kvGhislame(App):
    def build(self):
        return MainKvG()

if __name__ == "__main__":
    kvGhislame().run()
