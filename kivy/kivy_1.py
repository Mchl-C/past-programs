from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty, ListProperty

class ChecklistItem(BoxLayout):
    text = StringProperty('')
    
class ChecklistScreen(Screen):
    items = ListProperty([
        {'text': 'Option 1', 'checked': False},
        {'text': 'Option 2', 'checked': True},
        {'text': 'Option 3', 'checked': False},
        {'text': 'Option 4', 'checked': False},
        {'text': 'Option 5', 'checked': True},
    ])
    t1 = ChecklistItem(text = "Hello")
        
class MainApp(App):
    def build(self):
        return ChecklistScreen()

if __name__ == '__main__':
    MainApp().run()
