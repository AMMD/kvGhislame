import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, AliasProperty, ReferenceListProperty, NumericProperty
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder

from valuefader import ValueFader
from extendedxypad import ExtendedXyPad

class LightXyPad(ExtendedXyPad):
    hue_w = ObjectProperty(ValueFader)
    hue = NumericProperty(0)

    subpad = (60, 160)
    x_name_pad = 120
    faders_subpad = (80, 0)

    # i_h = NumericProperty()
    # i_s = NumericProperty()
    # i_v = NumericProperty()
    # i_color = ReferenceListProperty(i_h, i_s, i_v)

    # def on_hue_w(self, *args):
    #     self.hue_w.bind(value=self.setter('hue'))

    # def get_hue(self):
    #     return(self.hue_w.value)
    # def set_hue(self, value):
    #     self.hue_w.value = value
    # hue = AliasProperty(get_hue, set_hue)

    def get_hsv_triplet(self):
        return(self.hue_w.value, self.value[0], self.value[1])

    def set_hsv_triplet(self, value):
        self.hue_w.value = value[0]
        self.value = (value[1], value[2])
    hsv = AliasProperty(get_hsv_triplet, set_hsv_triplet, 
                        bind=('value', 'hue'))

#    def change_bg(self):
#        with self.canvas:
#            Color(self.hue, self.hsv[1], self.hsv[2], mode='hsv')
#            Rectangle(pos=(self.x, 20), size=(self.width, 60))

class LightXyPadApp(App):
    def build(self):
        return LightXyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y', step=(0.01, 0.01));

Builder.load_file('valuefader.kv')
Builder.load_file('extendedxypad.kv')
if __name__ == '__main__':
    LightXyPadApp().run()
