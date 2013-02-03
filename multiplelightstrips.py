import kivy

from kivy.lang import Builder
from kivy.uix.stencilview import StencilView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.splitter import Splitter
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty

from push import Push
from lightbox import LightBox
from lightxypad import LightXyPad

class MLightBox(LightBox):
    pass

class MultipleLightStrips(ScreenManager):
    tmp_s = ObjectProperty(StencilView)
    st1 = ObjectProperty(StencilView)
    st2 = ObjectProperty(StencilView)
    st3 = ObjectProperty(StencilView)
    stf = ObjectProperty(StencilView)

    lb1 = ObjectProperty(LightBox)
    lb2 = ObjectProperty(LightBox)
    lb3 = ObjectProperty(LightBox)

    name = StringProperty()
    name1 = StringProperty()
    name2 = StringProperty()
    name3 = StringProperty()
    app_name = StringProperty()

    main_s = ObjectProperty(Screen)
    front_s = ObjectProperty(Screen)

    def restore_zoomed_widget(self):
        for child in self.stf.children[:]:
            self.stf.remove_widget(child)
#            child.width = self.tmp_s.width
            child.x = self.tmp_s.x
            self.tmp_s.add_widget(child)

class MultipleLightStripsApp(App):
    def build(self):
        return MultipleLightStrips(name1="machin", name2="chose", name3="truc", app_name="yihi")


#Builder.load_file('lightxypad.kv')
Builder.load_file('lightbox.kv')
Builder.load_file('toggle.kv')

if __name__=="__main__":
    MultipleLightStripsApp().run()
