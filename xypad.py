import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class xyPad(Widget):
    path = StringProperty('xypad')

class xyPadApp(App):
    def build(self):
        return xyPad();

if __name__ == '__main__':
    xyPadApp().run()
