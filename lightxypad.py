import colorsys

import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, AliasProperty, ReferenceListProperty, NumericProperty, StringProperty
from kivy.lang import Builder

from valuefader import ValueFader
from extendedxypad import ExtendedXyPad

class LightXyPad(ExtendedXyPad):
    hue_w = ObjectProperty(ValueFader)
    hue = NumericProperty(0)

    subpad = (60, 160)
    x_name_pad = 120
    faders_subpad = (80, 0)

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

    def hsv_to_value(self, obj, hsv):
        print 'hsv to value (hsv, self.hsv, self.value):' 
        print hsv
        print self.hsv
        print self.value
        self.value = hsv[0], self.value[:]


class LightXyPadApp(App):
    name = StringProperty()
    name = "kvGhislame"
    def build(self):
        return LightXyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y', step=(0.01, 0.01), app_name=self.name);

Builder.load_file('valuefader.kv')
Builder.load_file('extendedxypad.kv')
if __name__ == '__main__':
    LightXyPadApp().run()
