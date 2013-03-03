import colorsys

import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, AliasProperty, NumericProperty, StringProperty, OptionProperty, ReferenceListProperty
from kivy.lang import Builder

from valuefader import ValueFader
from extendedxypad import ExtendedXyPad

from osc import OscServer

class LightXyPad(ExtendedXyPad):
    hue_w = ObjectProperty(ValueFader)
    hue = NumericProperty(0)

    hfader_x = NumericProperty()
    hfader_y = NumericProperty()
    hfader_pos = ReferenceListProperty(hfader_x, hfader_y)

    hfader_width = NumericProperty()
    hfader_height = NumericProperty()
    hfader_size = ReferenceListProperty(hfader_width, hfader_height)

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
        if(value != (0, 0, 0)):
            self.hsv = colorsys.rgb_to_hsv(value[0], value[1], value[2])
        else:
            self.hsv = self.hsv[0], self.hsv[1], 0
    rgb = AliasProperty(get_rgb_triplet, set_rgb_triplet, bind=('hsv',))

    def on_touch_down(self, touch):
        if ('button' in touch.profile) & ('right' in touch.button):
            print "[LightXY Pad " + self.name + "] OSC control:"
            print "sending path: " + self.path
            print "control path: " + self.control_path
        if Widget(pos=(self.x + self.pad_x, self.y + self.pad_y), size=self.pad_size).collide_point(*touch.pos):
            touch.grab(self)
            return True
        else:
            return super(LightXyPad, self).on_touch_down(touch)


    def on_touch_move(self, touch):
        if touch.grab_current == self:
            new_value_x = self.value_pos[0]
            new_value_y = self.value_pos[1]
            if touch.x > self.x + self.pad_x:
                self.xfader.value_pos = touch.pos
                new_value_x = touch.x
            if touch.y > self.y + self.pad_y:
                self.yfader.value_pos = touch.pos
                new_value_y = touch.y
            self.value_pos = (new_value_x, new_value_y)


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
        xypad = LightXyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y', step=(0.01, 0.01), app_name=self.name, target="9961");
        self.server.add_method(xypad.path, xypad.args_pattern, xypad.control_cb)
        return xypad


#Builder.load_file('valuefader.kv')
Builder.load_file('extendedxypad.kv')
if __name__ == '__main__':
    LightXyPadApp().run()
