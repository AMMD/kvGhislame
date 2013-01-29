import kivy
kivy.require('1.4.1')

from kivy.app import App
from kivy.uix.layout import Layout
from kivy.uix.slider import Slider, Widget
from kivy.properties import NumericProperty, ReferenceListProperty, AliasProperty, OptionProperty, ListProperty, ObjectProperty

class Pad(Widget):

    # Outer Color
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

    padding = NumericProperty(15)

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

    x_value = NumericProperty(0.)
    y_value = NumericProperty(0.)
    value = ReferenceListProperty(x_value, y_value)

    alt_value = ListProperty()
    value_type = OptionProperty('normal', options=('normal', 'alternate'))

    x_min = NumericProperty(0.)
    y_min = NumericProperty(0.)
    min = ReferenceListProperty(x_min, y_min)

    x_max = NumericProperty(100.)
    y_max = NumericProperty(100.)
    max = ReferenceListProperty(x_max, y_max)

    x_step = NumericProperty(1)
    y_step = NumericProperty(1)
    step = ReferenceListProperty(x_step, y_step)

    def get_norm_value(self):
        vmin = self.min
        d = self.max
        for i in (0, 1):
            d[i] -= vmin[i]

        if d == (0, 0):
            return (0, 0)

        return ((self.value[0] - vmin[0]) / float(d[0]), (self.value[1] - vmin[1]) / float(d[1]))


    def set_norm_value(self, value):
        vmin = self.min
        step = self.step
        val = (value[0] * (self.max[0] - vmin[0]) + vmin[0], value[1] * (self.max[1] - vmin[1]) + vmin[1])
        if step == 0:
            self.value = val
        else:
            self.value = (min(round((val[0] - vmin[0]) / step[0]) * step[0], self.max[0]) + vmin[0], min(round((val[1] - vmin[1]) / step[1]) * step[1], self.max[1]) + vmin[1])
    value_normalized = AliasProperty(get_norm_value, set_norm_value,
                                     bind=('value', 'min', 'max', 'step'))
    '''Normalized value inside the :data:`range` (min/max) to 0-1 range::

        >>> slider = Slider(value=50, min=0, max=100)
        >>> slider.value
        50
        >>> slider.value_normalized
        0.5
        >>> slider.value = 0
        >>> slider.value_normalized
        0
        >>> slider.value = 1
        >>> slider.value_normalized
        1

    You can also use it for setting the real value without knowing the minimum
    and maximum::

        >>> slider = Slider(min=0, max=200)
        >>> slider.value_normalized = .5
        >>> slider.value
        100
        >>> slider.value_normalized = 1.
        >>> slider.value
        200

    :data:`value_normalized` is an :class:`~kivy.properties.AliasProperty`.
    '''

    def get_value_pos(self):
        padding = self.padding
        x = self.x + self.pad_x
        y = self.y + self.pad_y
        nval = self.value_normalized
        xpos = x + padding
        ypos = y + padding
        return (xpos + nval[0] * (self.pad_width - 2 * padding), ypos + nval[1] * (self.pad_height - 2 * padding))

    def set_value_pos(self, pos):
        padding = self.padding
        x = min(self.right - padding, max(pos[0], self.x + self.pad_x + padding))
        xpos = self.x + self.pad_x + padding
        y = min(self.top - padding, max(pos[1], self.y + self.pad_y + padding))
        ypos = self.y + self.pad_y + padding
        self.value_normalized = ((x - xpos) / float(self.pad_width - 2 * padding) , (y - ypos) / float(self.pad_height - 2 * padding))
    value_pos = AliasProperty(get_value_pos, set_value_pos,
                              bind=('x', 'y', 'width', 'height', 'min',
                                    'max', 'value_normalized', 'pad_x', 'pad_y', 'pad_width', 'pad_height'))
    '''Position of the internal cursor, based on the normalized value.

    :data:`value_pos` is an :class:`~kivy.properties.AliasProperty`.
    '''
    def on_touch_down(self, touch):
        if Widget(pos=(self.x + self.pad_x, self.y + self.pad_y), size=self.pad_size).collide_point(*touch.pos):
            touch.grab(self)
            return True
        else:
            return super(Pad, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current == self:
            self.value_pos = touch.pos
            return True

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            return True

class PadApp(App):
    def build(self):
        return Pad(color=(1, 1, 0))

if __name__ == '__main__':
    PadApp().run()

