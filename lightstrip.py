import kivy

from kivy.lang import Builder
from kivy.uix.stencilview import StencilView
from kivy.uix.bubble import Bubble
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import BooleanProperty, StringProperty, ObjectProperty
from kivy.animation import Animation

from toggle import Toggle
from lightbox import LightBox

class MLightBox(LightBox):
    pass

class LightStrip(Widget):
    st = StencilView()
    lb = MLightBox(name="moncul", color=(1, 0, 0))
    vb = Toggle(path='')

    bub = Bubble()

    name = StringProperty()

#    fl = FloatLayout()


    def state_to_visible(self):
        if self.vb.state == 'down':
            self.st.remove_widget(self.lb)
            self.add_widget(self.bub)
            self.bub.add_widget(self.lb)
        else:
            self.bub.remove_widget(self.lb)
            self.remove_widget(self.bub)
            self.st.add_widget(self.lb)

class LightStripApp(App):
    def build(self):
        return LightStrip()


Builder.load_file('lightbox.kv')
Builder.load_file('toggle.kv')

if __name__=="__main__":
    LightStripApp().run()
