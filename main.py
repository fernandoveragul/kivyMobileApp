from pathlib import Path
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.chip import MDChip
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.snackbar import Snackbar

from dependencies import Depends, FileConfig, OpenGame
from py.settings_sc import SettingsScreen
from py.start_sc import StartScreen
from py.example_sc import ExampleScreen
from py.example_screen import ExampleRunScreen, AnswerField, QuestionLabel


class MainApp(MDApp):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.menu = None
        self.config_app = Depends.File.get_config()
        self.app_header = Depends.Names.app_header
        self.app_summary = Depends.File.get_summary()
        self.settings_summary = Depends.Names.settings_summary
        self.game_summary = Depends.Names.game_summary

    def build(self):
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
        # 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']

        self.title = "Математические игры"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Indigo" if self.config_app.enable_switches[0] else "Lime"
        self.theme_cls.theme_style = "Light" if self.config_app.enable_switches[0] else "Dark"
        self.root = Builder.load_file(f"{Path(Path.cwd(), 'main.kv')}")

    def on_start(self):
        switches: list = []
        for child in self.root.ids.settings_sc.ids.sett.children:
            for el in child.children:
                if isinstance(el, MDSwitch):
                    switches.append(el)
        for prop, e in zip(self.config_app.enable_switches, switches):
            e.active = prop

        chips: list = []
        for child in self.root.ids.settings_sc.ids.chips_box.children:
            if isinstance(child, MDChip):
                chips.append(child)
        for prop, e in zip(self.config_app.current_diff, chips):
            e.active = prop

    def only_one_chip(self, chip):
        for child in self.root.ids.settings_sc.ids.chips_box.children:
            if isinstance(child, MDChip) and child is not chip:
                child.active = False

    def shutdown_dg(self, dg: MDDialog = None):
        if dg:
            dg.dismiss()
        dialog = MDDialog(
            title="ВЫКЛЮЧЕНИЕ",
            text=f"Вы хотите завершить работу приложения?",
            buttons=[
                MDRectangleFlatButton(
                    text="ВЫКЛЮЧИТЬ",
                    on_press=lambda e: self.stop()
                ),
                MDRectangleFlatButton(
                    text="ЗАКРЫТЬ",
                    on_press=lambda e: dialog.dismiss()
                )
            ],
        )
        dialog.open()

    def save_dg(self, type_save: str = 'save'):
        switches: list = []
        chips: list = []
        icon = None
        for child in self.root.ids.settings_sc.ids.sett.children:
            for el in child.children:
                if isinstance(el, MDSwitch):
                    switches.append(el.active)

        for child in self.root.ids.settings_sc.ids.chips_box.children:
            if isinstance(child, MDChip):
                chips.append(child.active)
                if child.active:
                    icon = child.icon_left
        if icon is not None:
            dialog_save = MDDialog(
                title='СОХРАНЕНИЕ',
                text='Чтобы применить настройки, необходимо перезагрузить приложение.',
                buttons=[
                    MDRectangleFlatButton(
                        text='OK',
                        on_press=lambda e: self.shutdown_dg(dialog_save)
                    )
                ]
            )
            push_save = Snackbar(
                text='Сложность' + Depends.File.get_difficulty_name(icon),
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=.975
            )
            match type_save:
                case 'save':
                    dialog_save.open()
                    push_save.open()
                    self.config_app = FileConfig(**{'current_diff': chips, 'enable_switches': switches})
                    Depends.File.save_config(self.config_app)
                case 'reset':
                    dialog_save.open()
                    push_save.open()
                    self.config_app = FileConfig()
                    Depends.File.save_config(self.config_app)
        else:
            self.warring_dg()

    @staticmethod
    def warring_dg():
        dg = MDDialog(
            title='ПРЕДУПРЕЖДЕНИЕ',
            text='Не выбрана сложность игрового процесса!',
            buttons=[MDRectangleFlatButton(
                text="ПОНЯТНО",
                on_press=lambda e: dg.dismiss()
            )]
        )
        dg.open()

    def switch_to_main_screen(self):
        self.root.transition.direction = 'up'
        self.root.current = 'home_screen'

    def show_diff_dg(self):
        dialog = MDDialog(
            title='ПРЕДУПРЕЖДЕНИЕ',
            text='Выбранная сложность не позволяет вам пройти эту игру. Подробнее смотрите в справке.',
            buttons=[
                MDRectangleFlatButton(
                    text='OK',
                    on_press=lambda e: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def switch_to_run_example(self, open_game: str):
        OpenGame.current_open_game = open_game
        examples = ['Быстрый счёт', 'Алгебра', 'Геометрия', 'Аксиомы', 'Алгоритмика', 'Теория игр']
        running = False
        if OpenGame.current_open_game in examples:
            if self.config_app.current_diff[0]:
                self.root.transition.direction = 'down'
                self.root.current = 'example_screen'
                running = True
        if OpenGame.current_open_game in examples[0:5]:
            if self.config_app.current_diff[1]:
                self.root.transition.direction = 'down'
                self.root.current = 'example_screen'
                running = True
        if OpenGame.current_open_game in examples[0:3]:
            if self.config_app.current_diff[2]:
                self.root.transition.direction = 'down'
                self.root.current = 'example_screen'
                running = True
        if running is False:
            self.show_diff_dg()


MainApp().run()
