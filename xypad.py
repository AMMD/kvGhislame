import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.factory import Factory
from kivy.lang import Builder

from pad import Pad

class XyPad(Widget):
    innerbox = ObjectProperty(None)
    path = StringProperty('xypad')
    name = StringProperty()
    name_w = ObjectProperty(None)

    ibox_x_padding = NumericProperty(0)
    ibox_y_padding = NumericProperty(0)
    ibox_padding = ReferenceListProperty(ibox_x_padding, ibox_y_padding)

    # Outer Color
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

    # Axes
    x_name = StringProperty()
    x_name_w = ObjectProperty(None)
    y_name = StringProperty()
    y_name_w = ObjectProperty(None)
    y_name_s = ObjectProperty(None)


class XyPadApp(App):
    def build(self):
        return XyPad(color=(0, 1, 1), name='My XY Pad', x_name='X', y_name='Y');

Factory.register('Pad', Pad)
Builder.load_file('pad.kv')
if __name__ == '__main__':
    XyPadApp().run()
