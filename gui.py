from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from editablelabel import EditableLabel

class TimingTable(GridLayout):

    def __init__(self, **kw):
        maxx = 9
        maxy = 5
        kw['rows'] = maxy
        kw['cols'] = maxx
        super(TimingTable, self).__init__(**kw)

        self.add_widget(Label(text='Table'))
        for x in xrange(maxx-1):
            self.add_widget(Label(text='RPM'))

        for y in xrange(maxy-1):
            self.add_widget(Label(text='Load'))

            for x in xrange(maxx-1):
                t = str(x), str(y)
                self.add_widget(EditableLabel(text=''.join(t)))

class RootWidget(BoxLayout):
    pass

class Gui(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    Gui().run()
