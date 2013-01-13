import re

import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.factory import Factory
from kivy.lang import Builder

from time import time

from pad import Pad
from osc import OscSender, OscServer

class XyPad(Pad, OscSender):
    name = StringProperty()
    name_w = ObjectProperty(None)
    name_pad_x = NumericProperty(0)
    '''Pad Main Name X position'''
    name_pad_y = NumericProperty(0)
    '''Pad Main Name Y position'''
    name_pad_pos = ReferenceListProperty(name_pad_x, name_pad_y)
    '''Pad Main Name position'''

    # Axes
    x_name = StringProperty()
    x_name_w = ObjectProperty(None)
    x_name_pad_x = NumericProperty(0)
    '''X Axis Name X position'''
    x_name_pad_y = NumericProperty(0)
    '''X Axis Name Y position'''
    x_name_pad_pos = ReferenceListProperty(x_name_pad_x, x_name_pad_y)
    '''X Axis Name position'''

    y_name = StringProperty()
    y_name_w = ObjectProperty(None)
    y_name_pad_x = NumericProperty(0)
    '''Y Axis Name X position'''
    y_name_pad_y = NumericProperty(0)
    '''Y Axis Name Y position'''
    y_name_pad_pos = ReferenceListProperty(y_name_pad_x, y_name_pad_y)
    '''Y Axis Name position'''
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
        xypad=XyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y', app_name=self.name);
        self.server.add_method(xypad.path, xypad.args_pattern, xypad.control_cb)
        return xypad

Builder.load_file('pad.kv')
if __name__ == '__main__':
    XyPadApp().run()
