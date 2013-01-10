import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ReferenceListProperty
from kivy.lang import Builder

from osc import OscSender

class Toggle(ToggleButton, OscSender):
    name = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

class ToggleApp(App):
    name = StringProperty()
    name = "kvGhislame"
    def build(self):
        return Toggle(name="My Toggle", color=(1,0,0), app_name=self.name)

if __name__ == "__main__":
    ToggleApp().run()
