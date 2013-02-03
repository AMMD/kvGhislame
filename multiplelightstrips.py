import kivy

from kivy.lang import Builder
from kivy.uix.stencilview import StencilView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty

from push import Push
from lightbox import LightBox

class MLightBox(LightBox):
    pass

class MultipleLightStrips(ScreenManager):
    tmp_s = ObjectProperty(None)
    st1 = ObjectProperty(None)
    st2 = ObjectProperty(None)
    stf = ObjectProperty(None)

    lb1 = ObjectProperty(None)
    lb2 = ObjectProperty(None)

    name = StringProperty()
    name1 = StringProperty()
    name2 = StringProperty()

    main_s = ObjectProperty(None)
    front_s = ObjectProperty(None)

    def restore_zoomed_widget(self):
        for child in self.stf.children[:]:
            self.stf.remove_widget(child)
            self.tmp_s.add_widget(child)

class MultipleLightStripsApp(App):
    def build(self):
        return MultipleLightStrips(name1="machin", name2="chose", app_name="yihi")


Builder.load_file('lightbox.kv')
Builder.load_file('toggle.kv')

if __name__=="__main__":
    MultipleLightStripsApp().run()
