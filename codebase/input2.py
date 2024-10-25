import datetime
import os

from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input_boxes = []  # List to store input box references
        self.labels = []  # List to store labels for input fields

        # Scrollable container
        scrollview = ScrollView()
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Dynamically creating input boxes and labels
        for i in range(3):  # Example of creating multiple inputs
            label = Label(text=f'Input {i + 1}', size_hint_y=None, height=40)
            layout.add_widget(label)
            self.labels.append(label.text)  # Store each label text
            input_box = TextInput(size_hint_y=None, height=40,multiline=False)
            #input_box.bind(on_key_down=self.on_key_down)  # Bind key down event
            layout.add_widget(input_box)
            self.input_boxes.append(input_box)  # Store each TextInput in the list

        # Submit button
        submit_button = Button(text="Submit", size_hint_y=None, height=50)
        submit_button.bind(on_release=self.on_submit)
        layout.add_widget(submit_button)

        scrollview.add_widget(layout)
        self.add_widget(scrollview)

    def on_submit(self, instance):
        # Retrieve values from all input boxes
        self.collected_values = [input_box.text.strip() for input_box in self.input_boxes]
        self.save_inputs(self.collected_values)
        self.calculate(self.collected_values)
        # Access the ResultScreen and update its label text with labels and collected values
        result_screen = self.manager.get_screen('result')
        result_screen.display_values(self.labels, self.collected_values)

        # Switch to ResultScreen
        self.manager.current = 'result'

    def calculate(self,list_data):
        pass

    def save_inputs(self, data):
        # Create directory if it doesn't exist
        if not os.path.exists('kcs_data'):
            os.makedirs('kcs_data')

        # Write to a file
        file_name = f'kcs_data/{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.txt'
        with open(file_name, "w") as f:
            f.write(f'Inputs: {data}\n')

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Outer layout to hold results and back button separately
        outer_layout = BoxLayout(orientation='vertical')

        # Scrollable layout for displaying results
        scrollview = ScrollView(size_hint=(1, 0.9))
        self.result_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.result_layout.bind(minimum_height=self.result_layout.setter('height'))
        scrollview.add_widget(self.result_layout)

        # Back button to go back to the input screen
        back_button = Button(text="Back", size_hint=(1, 0.1), height=50)
        back_button.bind(on_release=self.go_back)

        # Add scrollview and back button to the outer layout
        outer_layout.add_widget(scrollview)
        outer_layout.add_widget(back_button)
        self.add_widget(outer_layout)

    def display_values(self, labels, values):
        # Clear previous results
        self.result_layout.clear_widgets()

        # Add "Hello World" label
        hello_label = Label(text="Hello World", size_hint_y=None, height=40)
        self.result_layout.add_widget(hello_label)

        # Add the current date to the layout
        date_label = Label(text=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", size_hint_y=None,height=40)
        self.result_layout.add_widget(date_label)

        # Add each label and value to the result layout
        for label, value in zip(labels, values):
            result_label = Label(text=f"{label}: {value}", size_hint_y=None, height=40)
            self.result_layout.add_widget(result_label)

    def go_back(self, instance):
        # Switch back to the InputScreen
        self.manager.current = 'input'


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.title = "Kamala Chicken Stores"
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(ResultScreen(name='result'))
        return sm


if __name__ == '__main__':
    MyApp().run()