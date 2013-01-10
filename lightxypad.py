import colorsys

import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, AliasProperty, NumericProperty, StringProperty, OptionProperty
from kivy.lang import Builder

from valuefader import ValueFader
from extendedxypad import ExtendedXyPad

from osc import OscServer

class LightXyPad(ExtendedXyPad):
    hue_w = ObjectProperty(ValueFader)
    hue = NumericProperty(0)

    subpad = (60, 160)
    x_name_pad = 120
    faders_subpad = (80, 0)

    mode = OptionProperty('hsv', options=('hsv', 'rgb'))

    def get_hsv_triplet(self):
        return(self.hue, self.value[0], self.value[1])

    def set_hsv_triplet(self, value):
        self.hue_w.value = value[0]
        self.value = (value[1], value[2])
    hsv = AliasProperty(get_hsv_triplet, set_hsv_triplet, bind=('value', 'hue'))

    def get_rgb_triplet(self):
        return(colorsys.hsv_to_rgb(self.hsv[0], self.hsv[1], self.hsv[2]))

    def set_rgb_triplet(self, value):
        self.hsv = colorsys.rgb_to_hsv(value[0], value[1], value[3])
    rgb = AliasProperty(get_rgb_triplet, set_rgb_triplet)

    def control_cb(self, path, args, types, src):
        if re.search('127.0.0.1', src.get_url()):
            print "self-incoming message"
        else:
            print "OSC controlled"
            if self.mode == 'hsv':
                self.hsv = (float(args[0]), float(args[1]), float(args[2]))
                self.xfader.value = float(args[1])
                self.yfader.value = float(args[2])
                self.hue = float(args[0])
                self.hue_w.value = float(args[0])
            else:
                self.rgb = (float(args[0]), float(args[1]), float(args[2]))
                self.xfader.value = self.hsv[1]
                self.yfader.value = self.hsv[2]
                            



class LightXyPadApp(OscServer, App):
    name = StringProperty()
    name = "kvGhislame"
    def build(self):
        xypad = LightXyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y', step=(0.01, 0.01), app_name=self.name);
        self.server.add_method(xypad.path, xypad.args_pattern, xypad.control_cb)
        return xypad


Builder.load_file('valuefader.kv')
Builder.load_file('extendedxypad.kv')
if __name__ == '__main__':
    LightXyPadApp().run()
