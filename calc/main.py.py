from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 300)
Config.set('graphics', 'height', 500)

class CalculatorApp(App):
    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation='vertical', padding=10)
        gl = GridLayout(cols=4, spacing=3)

        self.lbl = Label(text='0', font_size=40, halign='right', valign='center', size_hint=(None, None), size=(220, 192), text_size=(400-50,500*.4-50))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='7', on_press=self.add_n))
        gl.add_widget(Button(text='8', on_press=self.add_n))
        gl.add_widget(Button(text='9', on_press=self.add_n))
        gl.add_widget(Button(text='*', on_press=self.add_op))

        gl.add_widget(Button(text='4', on_press=self.add_n))
        gl.add_widget(Button(text='5', on_press=self.add_n))
        gl.add_widget(Button(text='6', on_press=self.add_n))
        gl.add_widget(Button(text='-', on_press=self.add_op))

        gl.add_widget(Button(text='1', on_press=self.add_n))
        gl.add_widget(Button(text='2', on_press=self.add_n))
        gl.add_widget(Button(text='3', on_press=self.add_n))
        gl.add_widget(Button(text='+', on_press=self.add_op))

        gl.add_widget(Button(text='C', on_press=self.clear))
        gl.add_widget(Button(text='0', on_press=self.add_n))
        gl.add_widget(Button(text=',', on_press=self.add_op))
        gl.add_widget(Button(text='=', on_press=self.calc))
        bl.add_widget(gl)
        return bl
    def add_n(self, instance):
        if len(self.formula) < 13:
            if self.formula == '0':
                self.formula = ''
            self.formula += str(instance.text)
            self.update_lbl()
        print(self.formula)
    def add_op(self, instance):
        if len(self.formula) < 13:
            self.formula += str(instance.text)
            self.update_lbl()
        print(self.formula)
    def update_lbl(self):
        self.lbl.text = self.formula
    def clear(self, instance):
        self.formula = '0'
        self.update_lbl()
    def calc(self, instance):
        self.formula = str(eval(self.lbl.text))
        self.update_lbl()

if __name__ == '__main__':
    CalculatorApp().run()
