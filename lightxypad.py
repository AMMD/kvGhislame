import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, AliasProperty, ReferenceListProperty
from kivy.factory import Factory
from kivy.lang import Builder

from valuefader import Fader
from extendedxypad import ExtendedXyPad

class LightXyPad(ExtendedXyPad):
    hue_w = ObjectProperty(Fader)

    def get_hue(self):
        return(self.hue_w.value)
    def set_hue(self, value):
        self.hue_w.value = value
    hue = AliasProperty(get_hue, set_hue)

    def get_hsv_triplet(self):
        return(self.hue_w.value, self.value[0], self.value[1])

    def set_hsv_triplet(self, value):
        self.hue_w.value = value[0]
        self.value = (value[1], value[2])

    hsv = AliasProperty(get_hsv_triplet, set_hsv_triplet, 
                        bind=('value', 'hue'))

class LightXyPadApp(App):
    def build(self):
        return LightXyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y');

Builder.load_file('extendedxypad.kv')
if __name__ == '__main__':
    LightXyPadApp().run()
