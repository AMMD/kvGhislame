import kivy
kivy.require('1.5.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.factory import Factory
from kivy.lang import Builder

from audiostrip import AudioStrip
from lightxypad import LightXyPad
from lightstrip import LightStrip
# from osc import OscSendingService

class OscSendingService(Widget):
    port = NumericProperty(1234)
    def send_message(self):
        print('Message sent')

class MainWidget(Widget):
    mystrip1 = ObjectProperty(None)
    mystrip2 = ObjectProperty(None)
    mystrip3 = ObjectProperty(None)
    mystrip4 = ObjectProperty(None)
    stripwidth = NumericProperty(70)
    mlstrip1 = LightStrip()
    mlstrip2 = LightStrip()

class MainWidgetApp(App):
    def build(self):
        mainwidget = MainWidget()
        return mainwidget
    def send_message(self):
        oscsendingservice = OscSendingService()
        oscsendingservice.send_message()




Builder.load_file('audiostrip.kv')
Builder.load_file('oscsendingservice.kv')
Builder.load_file('lightstrip.kv')
Factory.register('AudioStrip', AudioStrip)
Factory.register('OscSendingService', OscSendingService)
if __name__ == '__main__':
    app = MainWidgetApp()
    app.run()
