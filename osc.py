import liblo as _liblo

import kivy
kivy.require('1.4.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty, NumericProperty

from time import time

class OscSender(Widget):
    target = StringProperty("osc.udp://localhost:1234")
    path = StringProperty()
    control_path = StringProperty()
    args = ListProperty()
    args_pattern = StringProperty()
    app_name = StringProperty()

    def send_message(self):
        _liblo.send(self.target, self.path, *self.args)


class OscServer(Widget):
    port = NumericProperty()
    port = 9999
    server = _liblo.ServerThread(port)
    
    def on_start(self):
            self.server.register_methods(self)
            self.server.start()
            print "[OSC] listening on udp port: " + str(self.port)

    def on_exit(self):
        self.server.stop()
        del self.server
