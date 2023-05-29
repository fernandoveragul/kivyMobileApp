from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


class ExampleRunScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.text_question = 'text'


class AnswerField(MDBoxLayout):
    pass


class QuestionField(MDBoxLayout):
    pass
