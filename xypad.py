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
    x_value = NumericProperty(0)
    y_value = NumericProperty(0)
    value = ReferenceListProperty(x_value, y_value)

    x_min = NumericProperty()
    y_min = NumericProperty()
    min = ReferenceListProperty(x_min, y_min)

    x_max = NumericProperty()
    y_max = NumericProperty()
    max = ReferenceListProperty(x_max, y_max)


    def get_norm_value(self):
        vmin = self.min
        vmax = self.max
        d = self.max - vmin
        return (self.value - vmin) / float(d)

    def set_norm_value(self, value):
        vmin = self.min

    def on_touch_down(self, touch):
        self.value = (self.x_coef * touch.x + self.x_ord, self.y_coef * touch.y + self.y_ord)

    def on_touch_move(self, touch):
        self.value = (self.x_coef * touch.x + self.y_ord, self.y_coef * touch.y + self.y_ord)

        

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
