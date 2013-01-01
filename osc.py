import liblo as _liblo

import kivy
kivy.require('1.4.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class OscSender(Widget):
    path = StringProperty()
#    def send_message(self, host, path, *args):
    def send_message(self):
        print('Message sent')

class OscSenderApp(App):
    def build(self):
        return OscSender()

if __name__ == "__main__":
    OscSendingServiceApp().run()
