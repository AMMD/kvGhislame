import colorsys

import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.layout import Layout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from lightxypad import LightXyPad
from valuefader import ValueFader
from push import Push

class LightBox(LightXyPad):
    main_dimmer_fader = ValueFader()

    r_fader = ValueFader()
    g_fader = ValueFader()
    b_fader = ValueFader()

    custom_color_1 = Push()
    custom_color_2 = Push()
    custom_color_3 = Push()
    custom_color_4 = Push()
    custom_color_5 = Push()
    custom_color_6 = Push()
    custom_color_7 = Push()
    custom_color_8 = Push()

# TODO Flash
    flash = Push()
    old_hue = NumericProperty()

# TODO Link
# TODO Develop
    sm = ScreenManager()
    micro_screen = Screen()
    main_screen = Screen()


    def on_touch_down(self, touch):
        if ('button' in touch.profile) & ('right' in touch.button):
            print "[LightBox " + self.name + "] OSC control:"
            print "sending path: " + self.path
            print "control path: " + self.control_path
        if Widget(pos=(self.x + self.pad_x, self.y + self.pad_y), size=self.pad_size).collide_point(*touch.pos):
            touch.grab(self)
            return True
        else:
            return super(LightBox, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current == self:
            new_value_x = self.value_pos[0]
            new_value_y = self.value_pos[1]
            if touch.x > self.x + self.pad_x:
#                self.xfader.value_pos = touch.pos
                new_value_x = touch.x
            if touch.y > self.y + self.pad_y:
#                self.yfader.value_pos = touch.pos
#                self.main_dimmer_fader.value_pos = touch.pos
                new_value_y = touch.y
            self.value_pos = (new_value_x, new_value_y)
#            self.r_fader.value = self.rgb[0]
#            self.g_fader.value = self.rgb[1]
#            self.b_fader.value = self.rgb[2]
#        root.main_dimmer_fader.value = root.hsv[2]
#        root.r_fader.value = root.rgb[0]
#        root.g_fader.value = root.rgb[1]
#        root.b_fader.value = root.rgb[2]

    def rgb_to_hsv(color):
        return colorsys.rgb_to_hsv(color)


Builder.load_file('valuefader.kv')
Builder.load_file('push.kv')
Builder.load_file('lightxypad.kv')

class LightBoxApp(App):
    def build(self):
        return LightBox(name="Ducul", color=(1, 1, 0))


if __name__ == '__main__':
    LightBoxApp().run()


