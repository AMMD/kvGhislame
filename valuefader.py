import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.factory import Factory

class Fader(Slider):
    path = StringProperty('Fader')
#    def on_touch_move(self, touch):
#        app = App.get_running_app()
#        app.send_message()

class ValueFader(Widget):
    fader = ObjectProperty(None)
    name_f = ObjectProperty(None)
    name = StringProperty()

class ValueFaderApp(App):
    def build(self):
        return ValueFader(name='My Fader')

Factory.register('Fader', Fader)
if __name__ == "__main__":
    ValueFaderApp().run()
