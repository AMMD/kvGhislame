import kivy

from kivy.lang import Builder
from kivy.uix.stencilview import StencilView
#from kivy.uix.bubble import Bubble
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.properties import BooleanProperty, StringProperty, ObjectProperty
#from kivy.animation import Animation

#from toggle import Toggle
from push import Push
from lightbox import LightBox

class MLightBox(LightBox):
    pass

class MultipleLightStrips(ScreenManager):
    tmp_s = StencilView()
    st1 = StencilView()
    st2 = StencilView()
    stf = StencilView()
    lb1 = MLightBox(name="moncul", color=(1, 0, 0))
    lb2 = MLightBox(name="moncul", color=(1, 0, 0))
#    vb = Toggle(path='')

#    bub = Bubble()

    name = StringProperty()

#    fl = FloatLayout()

#    sm = ScreenManager()
    main_s = Screen(name='main')
    front_s = Screen(name='front')


#    def state_to_visible(self):
#        if self.vb.state == 'down':
#            self.st.remove_widget(self.lb)
#            self.add_widget(self.bub)
#            self.bub.add_widget(self.lb)
#        else:
#            self.bub.remove_widget(self.lb)
#            self.remove_widget(self.bub)
#            self.st.add_widget(self.lb)

    def restore_zoomed_widget(self):
        for child in self.stf.children[:]:
            self.stf.remove_widget(child)
            self.tmp_s.add_widget(child)

class MultipleLightStripsApp(App):
    def build(self):
        return MultipleLightStrips()


Builder.load_file('lightbox.kv')
Builder.load_file('toggle.kv')

if __name__=="__main__":
    MultipleLightStripsApp().run()
