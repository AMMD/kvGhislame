import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.factory import Factory

class InnerBox(Widget):
    # Inner Color
    h = NumericProperty()
    s = NumericProperty()
    v = NumericProperty()
    i_color = ReferenceListProperty(h, s, v)

    # Outer Color
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

    # Curseur
    pointer = ObjectProperty(None)
    x_value = NumericProperty()
    y_value = NumericProperty()
    value = ReferenceListProperty(x_value, y_value)

class XyPad(Widget):
    innerbox = ObjectProperty(None)
    path = StringProperty('xypad')
    name = StringProperty()
    name_w = ObjectProperty(None)

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
        return XyPad(color=(1, 1, 1), name='My XY Pad', x_name='X', y_name='Y');

Factory.register('InnerBox', InnerBox)
if __name__ == '__main__':
    XyPadApp().run()
