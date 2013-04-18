#import liblo as _liblo
import math
import re

import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty, OptionProperty, NumericProperty, ReferenceListProperty, AliasProperty
from kivy.factory import Factory

from osc import OscSender, OscServer

class Fader(Slider, OscSender):

    # Couleur
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

    subpad = NumericProperty(20)

    def get_value_pos(self):
        padding = self.padding
        subpad = self.subpad
        x = self.x
        y = self.y
        nval = self.value_normalized
        if self.orientation == 'horizontal':
            return (x + padding + nval * (self.width - 2 * padding), y)
        else:
            return (x, y + subpad + padding + nval * (self.height - 2 * padding - subpad))

    def set_value_pos(self, pos):
        padding = self.padding
        subpad = self.subpad
        x = min(self.right - padding, max(pos[0], self.x + padding))
        y = min(self.top - padding, max(pos[1], self.y + padding + subpad))
        if self.orientation == 'horizontal':
            if self.width == 0:
                self.value_normalized = 0
            else:
                self.value_normalized = (x - self.x - padding) / float(self.width - 2 * padding)
        else:
            if self.height == 0:
                self.value_normalized = 0
            else:
                self.value_normalized = (y - self.y - padding - subpad) / float(self.height - 2 * padding - subpad)
    value_pos = AliasProperty(get_value_pos, set_value_pos,
                              bind=('x', 'y', 'width', 'height', 'min',
                                    'max', 'value_normalized', 'orientation'))

    # def get_value_displayed(self):
    #     return round(3.0/20.0*(math.log(self.value_normalized)/math.log(2.0)+16.0/3.0),2)

    # def set_value_displayed(self, value):
    #     self.value_normalized = math.pow(2, (20.0 / 3.0) * value - 16.0 / 3.0)
    # value_displayed = AliasProperty(get_value_displayed, set_value_displayed, bind=('value_normalized',))


    def on_touch_down(self, touch):
        if ('button' in touch.profile) & ('right' in touch.button):
            print "[Fader " + self.name + "] OSC control:"
            print "sending path: " + self.path
            print "control path: " + self.control_path
        if Widget(pos=(self.x, self.y + self.subpad), size=(self.width, self.height - self.subpad)).collide_point(*touch.pos):
            touch.grab(self)
            return True
        else:
            return super(Slider, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            return True

    def control_cb(self, path, args, types, src):
        if re.search('127.0.0.1', src.get_url()):
            print "Self-incoming message"
        else:
            print "OSC controlled"
            self.value = float(args[0])
        if re.search('load', path):
            print 'OSC controlled (Load)'
            self.value = float(args[0])


class ValueFader(Fader):
    name_f = ObjectProperty(None)
    name = StringProperty()

class ValueFaderApp(OscServer, App):
    name = StringProperty()
    name = "kvGhislame"
    def build(self):
        valuefader = ValueFader(name='My Fader', orientation='vertical', color=(1,0.5,0.5), app_name=self.name)
        self.server.add_method(valuefader.path, valuefader.args_pattern, valuefader.control_cb)
        return valuefader

Factory.register('Fader', Fader)
if __name__ == "__main__":
    ValueFaderApp().run()
