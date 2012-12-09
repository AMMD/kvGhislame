import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty, ReferenceListProperty, AliasProperty

from valuefader import Fader
from xypad import XyPad

class ExtendedXyPad(XyPad):
    xfader = ObjectProperty(Fader)
    yfader = ObjectProperty(Fader)
                    
    def update_cursor_from_pad(self, obj, touch):
        if touch.x < obj.x + obj.width + 5:
            self.xfader.value_pos = touch.pos
        if touch.y < obj.y + obj.height + 5:
            self.yfader.value_pos = touch.pos

class ExtendedXyPadApp(App):
    def build(self):
        return ExtendedXyPad(color=(1,0,0), name='My Xtended XY Pad', x_name='X', y_name='Y', step=(0.01, 0.01))


#Factory.register('XyPad', XyPad)
Factory.register('Fader', Fader)
Builder.load_file('xypad.kv')
Builder.load_file('valuefader.kv')

if __name__ == '__main__':
    ExtendedXyPadApp().run()
