import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.properties import StringProperty

class Fader(Slider):
    path = StringProperty('Fader')
#    def on_touch_move(self, touch):
#        app = App.get_running_app()
#        app.send_message()

class FaderApp(App):
    def build(self):
        return Fader()

if __name__ == "__main__":
    FaderApp().run()
