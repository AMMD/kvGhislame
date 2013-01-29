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
    '''Relative Pad Main Name X position'''
    name_pad_y = NumericProperty(0)
    '''Relative Pad Main Name Y position'''
    name_pad_pos = ReferenceListProperty(name_pad_x, name_pad_y)
    '''Relative Pad Main Name position'''
    name_pad_width = NumericProperty(0)
    '''Pad Main Name width'''
    name_pad_height = NumericProperty(0)
    '''Pad Main Name height'''
    name_pad_size = ReferenceListProperty(name_pad_width, name_pad_height)
    '''Pad Main Name size'''

    # Axes
    x_name = StringProperty()
    x_name_w = ObjectProperty(None)
    x_name_pad_x = NumericProperty(0)
    '''Relative X Axis Name X position'''
    x_name_pad_y = NumericProperty(0)
    '''Relative X Axis Name Y position'''
    x_name_pad_pos = ReferenceListProperty(x_name_pad_x, x_name_pad_y)
    '''Relative X Axis Name position'''
    x_name_pad_width = NumericProperty(0)
    '''X Axis Name width'''
    x_name_pad_height = NumericProperty(0)
    '''X Axis Name height'''
    x_name_pad_size = ReferenceListProperty(x_name_pad_width, x_name_pad_height)
    '''X Axis Name size'''

    y_name = StringProperty()
    y_name_w = ObjectProperty(None)
    y_name_pad_x = NumericProperty(0)
    '''Relative Y Axis Name X position'''
    y_name_pad_y = NumericProperty(0)
    '''Relative Y Axis Name Y position'''
    y_name_pad_pos = ReferenceListProperty(y_name_pad_x, y_name_pad_y)
    '''Relative Y Axis Name position'''
    y_name_pad_width = NumericProperty(0)
    '''Y Axis Name width'''
    y_name_pad_height = NumericProperty(0)
    '''Y Axis Name height'''
    y_name_pad_size = ReferenceListProperty(y_name_pad_width, y_name_pad_height)
    '''Y Axis Name size'''
    y_name_s = ObjectProperty(None)


    def on_touch_down(self, touch):
        if ('button' in touch.profile) & ('right' in touch.button):
            print "[Fader " + self.name + "] OSC control:"
            print "sending path: " + self.path
            print "control path: " + self.control_path
        if Widget(pos=(self.x + self.pad_x, self.y + self.pad_y), size=self.pad_size).collide_point(*touch.pos):
            touch.grab(self)
            return True
        else:
            return super(XyPad, self).on_touch_down(touch)

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
        xypad=XyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y', app_name=self.name, pad_size=(30, 50));
        self.server.add_method(xypad.path, xypad.args_pattern, xypad.control_cb)
        return xypad

Builder.load_file('pad.kv')
if __name__ == '__main__':
    XyPadApp().run()
