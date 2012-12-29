import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from valuefader import Fader
from xypad import XyPad

class ExtendedXyPad(XyPad):
    xfader = ObjectProperty(Fader)
    yfader = ObjectProperty(Fader)

    subpad = (60, 80)
    x_name_pad = 40
    y_name_pad = 40
                    
    def update_cursor_from_pad(self, touch):
#        if (touch.x < obj.x + obj.width + 5) & (touch.x > obj.x + 5) & (touch.y < obj.y + obj.height + 5) & (touch.y > obj.y - 5):
        if touch.pos > self.subpad:
            self.xfader.value_pos = touch.pos
            self.yfader.value_pos = touch.pos

    def on_touch_move(self, touch):
        new_value_x = self.value_pos[0]
        new_value_y = self.value_pos[1]
        if touch.x > self.subpad[0] + self.padding:
            self.xfader.value_pos = touch.pos
            new_value_x = touch.x
        if touch.y > self.subpad[1] + self.padding:
            self.yfader.value_pos = touch.pos
            new_value_y = touch.y
        self.value_pos = (new_value_x, new_value_y)

class ExtendedXyPadApp(App):
    def build(self):
        return ExtendedXyPad(color=(1,0,0), name='My Xtended XY Pad', x_name='X', y_name='Y', step=(0.01, 0.01))


Factory.register('Fader', Fader)
Builder.load_file('xypad.kv')
Builder.load_file('valuefader.kv')

if __name__ == '__main__':
    ExtendedXyPadApp().run()
