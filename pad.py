import kivy
kivy.require('1.4.1')

__all__ = ('Pad',)

from kivy.app import App
from kivy.uix.slider import Slider, Widget
from kivy.properties import NumericProperty, ReferenceListProperty, AliasProperty

class Pad(Widget):

    # Outer Color
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

    padding = NumericProperty(15)

    x_value = NumericProperty(0.)
    y_value = NumericProperty(0.)
    value = ReferenceListProperty(x_value, y_value)

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
        x = self.x
        y = self.y
        nval = self.value_normalized
        return (x + padding + nval[0] * (self.width - 2 * padding), y + padding + nval[1] * (self.height - 2 * padding))

    def set_value_pos(self, pos):
        x = min(self.right, max(pos[0], self.x))
        y = min(self.top, max(pos[1], self.y))
        self.value_normalized = ((x - self.x) / float(self.width) , (y - self.y) / float(self.height))
    value_pos = AliasProperty(get_value_pos, set_value_pos,
                              bind=('x', 'y', 'width', 'height', 'min',
                                    'max', 'value_normalized'))
    '''Position of the internal cursor, based on the normalized value.

    :data:`value_pos` is an :class:`~kivy.properties.AliasProperty`.
    '''
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.value_pos = touch.pos
            return True

    def on_touch_move(self, touch):
        if touch.grab_current == self:
            self.value_pos = touch.pos
            return True

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            self.value_pos = touch.pos
            return True




class PadApp(App):
    def build(self):
        return Pad(color=(1, 1, 1))

if __name__ == '__main__':
    PadApp().run()

