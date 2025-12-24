from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_file('main.kv')

class InputDialog(FloatLayout):
    def get_task(self):
        return self.ids.task_input.text
    
    def get_desc(self):
        return self.ids.desc_input.text
    
    def clear_all(self):
        self.ids.task_input.text = ''
        self.ids.desc_input.text = ''

class MainApp(App):
    def build(self):
        root = FloatLayout()
        self.dialog = InputDialog()
        
        # Connect buttons
        self.dialog.ids.submit_btn.bind(on_press=self.on_submit)
        self.dialog.ids.cancel_btn.bind(on_press=self.on_cancel)
        
        root.add_widget(self.dialog)
        return root
    
    def on_submit(self, instance):
        task = self.dialog.get_task()
        desc = self.dialog.get_desc()
        print(f"Task: {task}\nDescription: {desc}")
        self.dialog.clear_all()
    
    def on_cancel(self, instance):
        self.dialog.clear_all()
        print("Dialog cleared")

if __name__ == '__main__':
    MainApp().run()
