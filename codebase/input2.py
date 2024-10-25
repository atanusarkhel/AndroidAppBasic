from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class MyApp(App):
    def build(self,no_input=10):
        # Scrollable container
        scrollview = ScrollView()

        # Layout to hold input boxes and labels
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Dynamically creating input boxes and labels
        for i in range(no_input):  # Example of creating multiple inputs
            label = Label(text=f'Input {i + 1}', size_hint_y=None, height=40)
            layout.add_widget(label)
            input_box = TextInput(size_hint_y=None, height=40)
            layout.add_widget(input_box)

        scrollview.add_widget(layout)
        return scrollview


if __name__ == '__main__':
    MyApp().run()
