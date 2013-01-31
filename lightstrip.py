import kivy

from kivy.lang import Builder
from kivy.uix.stencilview import StencilView
from kivy.uix.bubble import Bubble
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.animation import Animation

from toggle import Toggle
from lightbox import LightBox

class LightStrip(Widget):
    st = StencilView()
    lb = LightBox(name="moncul", color=(1, 0, 0))
    vb = Toggle(path='')

    bub = Bubble()
    

    def state_to_visible(self):
        if self.vb.state == 'down':
            self.st.remove_widget(self.lb)
            self.add_widget(self.bub)
            self.bub.add_widget(self.lb)

#            Animation(width=500, d=0.3).start(self.st)
        else:
            self.bub.remove_widget(self.lb)
            self.remove_widget(self.bub)
            self.st.add_widget(self.lb)
#            Animation(width=100, d=0.3).start(self.st)

class LightStripApp(App):
    def build(self):
        return LightStrip()


Builder.load_file('lightbox.kv')
Builder.load_file('toggle.kv')

if __name__=="__main__":
    LightStripApp().run()
