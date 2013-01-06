import re

import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.factory import Factory
from kivy.lang import Builder



from pad import Pad
from osc import OscSender, OscServer

class XyPad(Pad, OscSender):
    name = StringProperty()
    name_w = ObjectProperty(None)
    name_pad = NumericProperty(0)

    subpad = (20, 40)

    # Axes
    x_name = StringProperty()
    x_name_w = ObjectProperty(None)
    x_name_pad = NumericProperty(0)
    y_name = StringProperty()
    y_name_w = ObjectProperty(None)
    y_name_pad = NumericProperty(0)
    y_name_s = ObjectProperty(None)


    def on_touch_down(self, touch):
        if ('button' in touch.profile) & ('right' in touch.button):
            print "[Fader " + self.name + "] OSC control:"
            print "sending path: " + self.path
            print "control path: " + self.control_path
        if self.collide_point(*touch.pos):
            touch.grab(self)
            return True

    def on_touch_move(self, touch):
        if touch.grab_current == self:
            self.value_pos = touch.pos
            return True

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            return True

    def control_cb(self, path, args, types, src):
        if re.search('127.0.0.1', src.get_url()):
            print "self-incoming message"
        else:
            print "OSC controlled"
            self.value = (float(args[0]), float(args[1]))



class XyPadApp(OscServer, App):
    name = StringProperty()
    name = "kvGhislame"
    def build(self):
        xypad=XyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y', subpad=(200,200), app_name=self.name);
        self.server.add_method(xypad.path, xypad.args_pattern, xypad.control_cb)
        return xypad

Builder.load_file('pad.kv')
if __name__ == '__main__':
    XyPadApp().run()
