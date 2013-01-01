import liblo as _liblo

import kivy
kivy.require('1.4.1')
from kivy.app import App
from kivy.uix.widget import Widget

class OscSender(Widget):
#    def send_message(self, host, path, *args):

    def __init__(self, target, path, args):
        self.target = target
        self.path = path
        self.args = args

    def send_message(self):
        _liblo.send(self.target, self.path, *args)
        print('Message sent')

class OscSenderApp(App):
    def build(self):
        return OscSender()

if __name__ == "__main__":
    OscSendingServiceApp().run()
