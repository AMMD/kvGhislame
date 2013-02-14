import kivy

from kivy.lang import Builder
from kivy.uix.stencilview import StencilView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ReferenceListProperty

from lightbox import LightBox

class LightStrip(BoxLayout):
    name = StringProperty()
    r = NumericProperty()
    g = NumericProperty()
    b = NumericProperty()
    color = ReferenceListProperty(r, g, b)

    path = StringProperty()
    control_path = StringProperty()

    lightbox = ObjectProperty(LightBox)
    button = ObjectProperty(Button)
    stencil = ObjectProperty(StencilView)

class LightStripApp(App):
    def build(self):
        return LightStrip()


Builder.load_file('lightbox.kv')

if __name__=="__main__":
    LightStripApp().run()
