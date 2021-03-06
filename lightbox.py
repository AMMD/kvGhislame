import colorsys

import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, StringProperty, OptionProperty, ReferenceListProperty

from lightxypad import LightXyPad
from valuefader import ValueFader
from push import Push

class LightBox(BoxLayout):
    main_dimmer_fader = ObjectProperty(ValueFader)

    xypad= ObjectProperty(LightXyPad)

    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

    pad_width = NumericProperty(100)
    '''Width of the XY Pad'''
    pad_height = NumericProperty(100)
    '''Height of the XY Pad'''
    pad_size = ReferenceListProperty(pad_width, pad_height)
    '''Size of the XY Pad (tuple: (pad_width, pad_height))'''
    pad_x = NumericProperty(0)
    '''X position of the XY Pad'''
    pad_y = NumericProperty(0)
    '''Y position of the XY Pad'''
    pad_pos = ReferenceListProperty(pad_x, pad_y)
    '''Position of the XY Pad (tuple: (pad_x, pad_y))'''

    app_name = StringProperty()
    name = StringProperty()
    mode = OptionProperty('hsv', options=('hsv', 'rgb'))

    r_fader = ObjectProperty(ValueFader)
    g_fader = ObjectProperty(ValueFader)
    b_fader = ObjectProperty(ValueFader)

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

    path = StringProperty()
    control_path = StringProperty()
    osc_name = StringProperty()
    target = StringProperty()

# TODO Link

    # def on_touch_down(self, touch):
    #     if ('button' in touch.profile) & ('right' in touch.button):
    #         print "[LightBox " + self.name + "] OSC control:"
    #         print "sending path: " + self.path
    #         print "control path: " + self.control_path
    #     if Widget(pos=(self.x + self.pad_x, self.y + self.pad_y), size=self.pad_size).collide_point(*touch.pos):
    #         touch.grab(self)
    #         return True
    #     else:
    #         return super(LightBox, self).on_touch_down(touch)

    # def on_touch_move(self, touch):
    #     if touch.grab_current == self:
    #         new_value_x = self.xypad.value_pos[0]
    #         new_value_y = self.xypad.value_pos[1]
    #         if self.xypad.collide_point(*touch.pos):
    #             if touch.x > self.xypad.x + self.xypad.pad_x:
    #                 new_value_x = touch.x
    #             if touch.y > self.xypad.y + self.xypad.pad_y:
    #                 new_value_y = touch.y
    #             self.xypad.value_pos = (new_value_x, new_value_y)
    #         if self.main_dimmer_fader.collide_point(*touch.pos):
    #             self.main_dimmer_fader.value_pos = touch.y
    #             self.xypad.value = self.xypad.value[0], self.main_dimmer_fader.value[1]


    def rgb_to_hsv(color):
        return colorsys.rgb_to_hsv(color)


#Builder.load_file('valuefader.kv')
Builder.load_file('push.kv')
Builder.load_file('lightxypad.kv')

class LightBoxApp(App):
    def build(self):
        return LightBox(name="Ducul", color=(1, 1, 0), target="osc.udp://SCVideo:56414")


if __name__ == '__main__':
    LightBoxApp().run()


