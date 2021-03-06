import liblo as _liblo

import kivy
kivy.require('1.4.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty, NumericProperty, BooleanProperty

class OscSender(Widget):
    target = StringProperty()
    path = StringProperty()
    control_path = StringProperty()
    args = ListProperty()
    args_pattern = StringProperty()
    osc_name = StringProperty()
    app_name = StringProperty()

    def send_message(self):
        if self.path != '':
            print "[OSC]" + self.path + " " + str(self.args)
            if self.osc_name:
                _liblo.send(self.target, self.path, self.osc_name.replace(" ", "_"), *self.args)
            else:
                _liblo.send(self.target, self.path, *self.args)


class OscServer(Widget):
    port = NumericProperty()
    port = "9999"
    server = _liblo.ServerThread(port)
    
    def on_start(self):
            self.server.register_methods(self)
            self.server.start()
            print "[OSC] listening on udp port: " + str(self.port)

    def on_exit(self):
        self.server.stop()
        del self.server
