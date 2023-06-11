import random
from copy import deepcopy
from datetime import datetime

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

from db.crud import DB
from db.schemas import *
from dependencies import OpenGame, Depends


class ExampleRunScreen(MDScreen):
    def load_cur_question(self, main_app: MDApp = None):
        self.get_text_from_fields()
        self.remove_text_fields()
        try:
            current = next(self.generator_questions, None)
        except AttributeError:
            self.load_all()
            current = next(self.generator_questions, None)
        if current is not None:
            if OpenGame.current_open_game == 'Быстрый счёт':
                self.ids.question_text.halign = 'center'
                self.set_text_question(f'[size=52sp]{current[0].text_question}[/size]')
            else:
                self.ids.question_text.halign = 'left'
                self.set_text_question(current[0].text_question)

            if main_app.config_app.enable_switches[1]:
                self.set_tip_question(current[0].tip)
            else:
                self.set_tip_question(Depends.Names.start_game_tip)
            self.add_answer_fields(current[1])
        else:
            self.show_end_game_dg()
            self.ids.question_text.text = Depends.Names.game_summary
            main_app.get_running_app().switch_to_main_screen()

    def load_all(self):
        game = OpenGame.current_open_game
        examples: list[SExample] = DB.select(table_name='example', where_param=f"example.name_game = '{game}'")
        example: SExample = random.choice(examples)
        self.questions: list[SQuestion] = DB.select(table_name='question',
                                                    where_param=f"question.name_example = '{example.name}'")
        self.origin_questions = deepcopy(self.questions)
        self.user_answers: list = []
        self.generator_questions = self.__gen_cur_question()

    def __gen_cur_question(self):
        self.start = datetime.now()
        self.counter_usr: int = 0
        while len(self.questions) > 0:
            qu: SQuestion = random.choice(self.questions)
            answers: list[SAnswers] = DB.select(table_name='answer',
                                                where_param=f"answer.question = '{qu.text_question}'")
            self.counter_usr += 1
            yield qu, answers
            self.questions.remove(qu)
        self.time2game = datetime.now() - self.start

    def set_text_question(self, text_question: str):
        self.ids.question_text.text = text_question
        return self

    def set_tip_question(self, text_tip: str):
        self.tip_dialog = dict(text=text_tip, is_start=False)

    def show_tip_dg(self):
        try:
            text_tip = self.tip_dialog.get('text')
        except AttributeError:
            text_tip = Depends.Names.start_game_tip
        dialog = MDDialog(
            title='ПОДСКАЗКА',
            text=text_tip,
            buttons=[
                MDRectangleFlatButton(
                    text='OK',
                    on_press=lambda e: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def count_true_answers(self):
        counter_true_ua: int = 0
        db_answers: list = []
        try:
            for qu in self.origin_questions:
                for ans in DB.select(table_name='answer', where_param=f"answer.question = '{qu.text_question}'"):
                    db_answers.append(ans.answers)
            true_answers = ' '.join(db_answers).split(' ')
            for ua in self.user_answers:
                if ua in true_answers:
                    counter_true_ua += 1
            try:
                res_time = str(self.time2game).split('.')[0]
            except AttributeError:
                res_time = str(datetime.now() - self.start).split('.')[0]
            return f"Дано ответов: {self.counter_usr} из {len(self.origin_questions)}\n" \
                   f"Правльных ответов: {(counter_true_ua / len(true_answers)) * 100: .1f}%\n" \
                   f"Затраченное время: {res_time} c"
        except AttributeError:
            return 'Вы вышли даже не начав'

    def show_end_game_dg(self):
        dialog = MDDialog(
            title='ИГРА ЗАКОНЧЕНА',
            text=self.count_true_answers(),
            buttons=[
                MDRectangleFlatButton(
                    text='OK',
                    on_press=lambda e: dialog.dismiss()
                )
            ]
        )
        dialog.open()
        self.remove_text_fields()
        try:
            del self.time2game
        except AttributeError:
            pass
        try:
            del self.origin_questions
        except AttributeError:
            pass
        try:
            del self.user_answers
        except AttributeError:
            pass
        try:
            del self.questions
        except AttributeError:
            pass
        try:
            del self.tip_dialog
        except AttributeError:
            pass
        try:
            del self.generator_questions
        except AttributeError:
            pass
        try:
            del self.start
        except AttributeError:
            pass

    def add_answer_fields(self, answers: list[SAnswers]):
        for ans in answers:
            txt_filed = MDTextField()
            txt_filed.hint_text = ans.name_field_answer
            txt_filed.font_size = "24sp"
            self.ids.answer_field.add_widget(txt_filed)

    def remove_text_fields(self):
        self.ids.answer_field.clear_widgets()

    def get_text_from_fields(self):
        for child in self.ids.answer_field.children:
            if child.text != '':
                self.user_answers.append(child.text.strip().lower())


class AnswerField(MDBoxLayout):
    pass


class QuestionLabel(MDLabel):
    pass
