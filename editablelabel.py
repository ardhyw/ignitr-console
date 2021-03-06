# https://github.com/kivy/kivy/wiki/Editable-Label

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty, ObjectProperty

__all__ = ('EditableLabel', )

class EditableLabel(Label):

    edit = BooleanProperty(False)

    textinput = ObjectProperty(None, allownone=True)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.edit:
            self.edit = True
        return super(EditableLabel, self).on_touch_down(touch)

    def on_edit(self, instance, value):
        #print locals()
        if not value:
            if self.textinput:
                self.remove_widget(self.textinput)
            return

        # buat text input ketika label di klik
        self.textinput = t = TextInput(
                text=self.text, size_hint=(None, None),
                font_size=self.font_size, font_name=self.font_name,
                pos=self.pos, size=self.size, multiline=False)
        self.bind(pos=t.setter('pos'), size=t.setter('size'))
        self.add_widget(self.textinput)
        t.bind(on_text_validate=self.on_text_validate, focus=self.on_text_focus)

    def on_text_validate(self, instance):

        # kalau dikosongin, kasih nilai default = 0
        if not instance.text:
            instance.text = "0"

        self.text = instance.text
        self.edit = False

    def on_text_focus(self, instance, focus):
        if focus is False:
            if not instance.text:
                instance.text = "0"

            self.text = instance.text
            self.edit = False
