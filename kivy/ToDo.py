# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty, NumericProperty, ListProperty
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.core.window import Window
import random

class Point(BoxLayout):
    apasih = StringProperty("")
    desc = StringProperty("")
    
    def checkbox_click(self, checkbox, value):
        self.ids.status_label.text = self.apasih + " " * 5 + ("True" if value else "False")    

    def tes(self, instance):
        self.ids.status_label.font_name = "Arial"
        self.ids.status_label.color = [random.random() for _ in range(4)]

class HoverButton(Button):
    effect_radius = NumericProperty(0)
    effect_color = ListProperty([1, 1, 1, 0])
    _is_pressed = False  # Track press state internally

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0.2, 0.6, 1, 1)  # Default color
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, window, pos):
        if not self._is_pressed:  # Only change if not currently pressed
            if self.collide_point(*pos):
                self.background_color = (0.3, 0.7, 1, 1)  # Hover color
            else:
                self.background_color = (0.2, 0.6, 1, 1)  # Normal color

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self._is_pressed = True
            self.effect_color = [1, 1, 1, 0.2]
            self.effect_radius = 0
            anim = Animation(
                effect_radius=max(self.width, self.height)*1.5,
                t='out_quad',
                duration=0.3
            )
            anim.bind(on_complete=self._show_input_dialog)  # Changed this line
            anim.start(self)
            self.background_color = (0.1, 0.5, 0.9, 1)
        return super().on_touch_down(touch)

    def _show_input_dialog(self, *args):
        self._reset_state()
        # Get the root widget (assuming it's the FloatLayout)
        root = self.parent.parent if hasattr(self.parent, 'parent') else App.get_running_app().root
        
        # Create and show dialog
        dialog = InputDialog()
        root.add_widget(dialog)
        
        # Center dialog (optional)
        dialog.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

    def _reset_state(self, *args):
        self._is_pressed = False
        self.effect_color = [0, 0, 0, 0]
        if self.collide_point(*Window.mouse_pos):
            self.background_color = (0.3, 0.7, 1, 1)
        else:
            self.background_color = (0.2, 0.6, 1, 1)

class ToDo(RelativeLayout):
    container = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content = self.ids.container
        
        # Add initial task
        self.add_img("Board.png")
        self.add_item("Task 1", "Create a new task")
        self.add_item("task 2", '')
        self.add_widget(HoverButton())
        
    def add_item(self, text, des):
        """Add a new task item to the scrollable list"""
        print("Add item!")
        point = Point(apasih=text, desc=des)
        self.content.add_widget(point)

    def add_img(self, loc):
        """Add an image to the scrollable list"""
        img = Image(
            source=loc,
            size_hint=(1, None),
            height=200,  # Fixed height
            allow_stretch=True
        )
        self.content.add_widget(img)


class InputDialog(FloatLayout):
    def __init__(self, todo_instance=None, **kwargs):
        super().__init__(**kwargs)
        self.todo = todo_instance  

    def on_submit(self, instance):
        task = self.get_task()
        desc = self.get_desc()
        if self.todo:  
            self.todo.add_item(task, desc)
        self.clear_all()
    
    def on_cancel(self, instance):
        self.clear_all()
        print("Dialog cleared")
    
    def get_task(self):
        return self.ids.task_input.text
    
    def get_desc(self):
        return self.ids.desc_input.text
    
    def clear_all(self):
        self.ids.task_input.text = ""
        self.ids.desc_input.text = ""
        
class InputDisplay(App):
    def build(self):
        root = FloatLayout()
        self.dialog = InputDialog()  # Now all functionality is inside InputDialog
        root.add_widget(self.dialog)
        return root
    
class background(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Background image
        self.add_widget(Image(
            source='img1.png',
            size_hint=(1, 1),
            allow_stretch=True,
            keep_ratio=False,
            opacity=0.5
        ))
        
        # Scrollable content
        self.todo = ToDo()
        self.add_widget(self.todo)
        
    
class MainApp(App):
    def build(self):
        return background()

if __name__ == '__main__':
    MainApp().run()

'''
        # Now add your items to the container
        for i in range(5):
            self.container.add_widget(Point(apasih=f"Option {i}"))

https://community.wacom.com/en-us/wp-content/uploads/sites/40/2025/01/Killer-Rabbit-Solarpunk-pixel-art-feature-image.jpg.webp'
'''
