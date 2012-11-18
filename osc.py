import liblo as _liblo

import kivy
kivy.require('1.4.1')
from kivy.app import App
from kivy.uix.widget import Widget

class OscSendingService(Widget):
#    def send_message(self, host, path, *args):
    def send_message(self):
        print('Message sent')

class OscSendingServiceApp(App):
    def build(self):
        return OscSendingService()

if __name__ == "__main__":
    OscSendingServiceApp().run()
