import liblo as _liblo

import kivy
kivy.require('1.4.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty

class OscSender(Widget):
    target = StringProperty("osc.udp://localhost:1234")
    path = StringProperty()
    args = ListProperty()


    def send_message(self):
        _liblo.send(self.target, self.path, *self.args)
        print('Message sent')

class OscSenderApp(App):
    def build(self):
        return OscSender()

if __name__ == "__main__":
    OscSendingServiceApp().run()
