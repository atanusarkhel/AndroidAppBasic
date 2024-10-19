# https://chatgpt.com/share/6713eb5a-be04-8010-9282-ebf0542e8d46

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.today_collection = TextInput(hint_text='Enter today\'s collection', multiline=False)
        self.remaining_yesterday = TextInput(hint_text='Enter remaining from yesterday', multiline=False)
        self.remaining_today = TextInput(hint_text='Enter remaining amount', multiline=False)

        self.submit_button = Button(text='Submit')
        self.submit_button.bind(on_press=self.calculate)

        self.layout.add_widget(self.today_collection)
        self.layout.add_widget(self.remaining_yesterday)
        self.layout.add_widget(self.remaining_today)
        self.layout.add_widget(self.submit_button)

        self.add_widget(self.layout)

    def calculate(self, instance):
        total_sales = float(self.today_collection.text) + float(self.remaining_yesterday.text)
        profit = total_sales - float(self.remaining_today.text)
        self.manager.current = 'result'
        self.manager.get_screen('result').update_result(total_sales, profit)


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
