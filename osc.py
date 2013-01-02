import liblo as _liblo

import kivy
kivy.require('1.4.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty, NumericProperty

class OscSender(Widget):
    target = StringProperty("osc.udp://localhost:1234")
    path = StringProperty()
    args = ListProperty()
    app_name = StringProperty()

    def send_message(self):
        _liblo.send(self.target, self.path, *self.args)
        print('Message sent')


class OscServer(Widget):
    port = NumericProperty()
    port = 9999
    server = _liblo.ServerThread(port)
    
    def on_start(self):
            self.server.register_methods(self)
            self.server.start()
            print "listening on udp port: " + str(self.port)

    def on_exit(self):
        self.server.stop()
        del self.server
