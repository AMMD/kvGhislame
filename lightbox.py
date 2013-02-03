import colorsys

import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.layout import Layout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty

from lightxypad import LightXyPad
from valuefader import ValueFader
from push import Push

class LightBox(LightXyPad):
    main_dimmer_fader = ObjectProperty(ValueFader)

    # r_fader = ObjectProperty(ValueFader)
    # g_fader = ObjectProperty(ValueFader)
    # b_fader = ObjectProperty(ValueFader)

    custom_color_1 = ObjectProperty(Push)
    custom_color_2 = ObjectProperty(Push)
    custom_color_3 = ObjectProperty(Push)
    custom_color_4 = ObjectProperty(Push)
    custom_color_5 = ObjectProperty(Push)
    custom_color_6 = ObjectProperty(Push)
    custom_color_7 = ObjectProperty(Push)
    custom_color_8 = ObjectProperty(Push)

    flash = ObjectProperty(Push)
    old_hue = NumericProperty()

# TODO Link

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
                new_value_x = touch.x
            if touch.y > self.y + self.pad_y:
                new_value_y = touch.y
            self.value_pos = (new_value_x, new_value_y)

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


