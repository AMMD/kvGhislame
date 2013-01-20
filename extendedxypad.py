import re

import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty, StringProperty

from valuefader import Fader
from xypad import XyPad

from osc import OscServer

class ExtendedXyPad(XyPad):
    xfader = ObjectProperty(Fader)
    '''X value Fader'''
    xfader_x = NumericProperty()
    '''X value Fader X position'''
    xfader_y = NumericProperty()
    '''X value Fader Y position'''
    xfader_pos = ReferenceListProperty(xfader_x, xfader_y)
    '''X value Fader position'''

    yfader = ObjectProperty(Fader)
    '''Y value Fader'''
    yfader_x = NumericProperty()
    '''Y value Fader X position'''
    yfader_y = NumericProperty()
    '''Y value Fader Y position'''
    yfader_pos = ReferenceListProperty(yfader_x, yfader_y)
    '''Y value Fader position'''

    def on_touch_move(self, touch):
        new_value_x = self.value_pos[0]
        new_value_y = self.value_pos[1]
        if touch.x > self.x + self.pad_x + self.padding:
            self.xfader.value_pos = touch.pos
            new_value_x = touch.x
        if touch.y > self.y + self.pad_y + self.padding:
            self.yfader.value_pos = touch.pos
            new_value_y = touch.y
        self.value_pos = (new_value_x, new_value_y)
                    

    def control_cb(self, path, args, types, src):
        if re.search('127.0.0.1', src.get_url()):
            print "self-incoming message"
        else:
            print "OSC controlled"
            self.value = (float(args[0]), float(args[1]))
            self.xfader.value = self.value[0]
            self.yfader.value = self.value[1]



class ExtendedXyPadApp(OscServer, App):
    name = StringProperty()
    name = "kvGhislame"

    def build(self):
        xypad=ExtendedXyPad(color=(1,0,0), name='My Xtended XY Pad', x_name='X', y_name='Y', step=(0.01, 0.01), app_name=self.name)
        self.server.add_method(xypad.path, xypad.args_pattern, xypad.control_cb)
        return xypad


Factory.register('Fader', Fader)
Builder.load_file('xypad.kv')
Builder.load_file('valuefader.kv')

if __name__ == '__main__':
    ExtendedXyPadApp().run()
