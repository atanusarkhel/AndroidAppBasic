from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Set the window size for better appearance on desktop
Window.size = (400, 600)


class InputSection(BoxLayout):
    def __init__(self, heading, **kwargs):
        super(InputSection, self).__init__(orientation='vertical', **kwargs)
        self.padding = (10, 10)
        self.spacing = 10

        # Heading label with custom color
        heading_label = Label(
            text=heading,
            size_hint_y=None,
            height=40,
            color=(1, 1, 1, 1),  # White color
            font_size='20sp',
            bold=True
        )
        self.add_widget(heading_label)

        # Create three input boxes with custom background and color
        for i in range(1, 4):
            input_box = TextInput(
                hint_text=f'Input {i}',
                multiline=False,
                size_hint_y=None,
                height=40,
                background_color=(0.9, 0.9, 0.9, 1),  # Light gray
                foreground_color=(0, 0, 0, 1)  # Black text
            )
            self.add_widget(input_box)


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)

        # Create a layout for the screen
        layout = BoxLayout(orientation='vertical', padding=10)

        # Create a ScrollView to hold sections
        scroll_view = ScrollView()
        scroll_layout = BoxLayout(orientation='vertical', size_hint_y=None)

        # Create five sections
        for i in range(1, 6):
            section = InputSection(f'Section {i}')
            scroll_layout.add_widget(section)

        # Set the height of scroll_layout based on the number of sections
        # Each section has a heading (40) + 3 input boxes (3 * 40) + spacing
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))
        scroll_layout.height = (40 + (3 * 40) + 10) * 5  # Total height for 5 sections

        scroll_view.add_widget(scroll_layout)
        layout.add_widget(scroll_view)

        self.submit_button = Button(
            text='Submit',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 0.2, 1),  # Dark green
            color=(1, 1, 1, 1),  # White text
            font_size='16sp',
            bold=True
        )
        self.submit_button.bind(on_press=self.calculate)

        layout.add_widget(self.submit_button)

        self.add_widget(layout)

    def calculate(self, instance):
        # Your calculation logic goes here
        pass


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.result_label = Label()
        self.layout.add_widget(self.result_label)
        self.add_widget(self.layout)

    def update_result(self, total_sales, profit):
        self.result_label.text = f'Total Sales: {total_sales}\nProfit: {profit}'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(ResultScreen(name='result'))
        return sm


if __name__ == '__main__':
    MyApp().run()
