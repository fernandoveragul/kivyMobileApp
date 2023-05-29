from pathlib import Path
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.chip import MDChip
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.snackbar import Snackbar
from dependencies import Depends, FileConfig
from py.settings_sc import SettingsScreen
from py.start_sc import StartScreen
from py.example_sc import ExampleScreen


class MainApp(MDApp):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.menu = None
        self.config_app = Depends.File.get_config()
        self.app_summary = Depends.Names.app_summary
        self.settings_summary = Depends.Names.settings_summary

    def build(self):
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
        # 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.title = "Математические игры"
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Indigo"
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

    def shutdown_dg(self):
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
        dialog = MDDialog(
            title=f"СОХРАНЕНИЕ",
            text=f"Для сохранения настроек требуется перезапуск приложения",
            buttons=[
                MDRectangleFlatButton(
                    text="ОК",
                    on_press=lambda e: self.show_message_in_bar("Настройки сохранены", dialog, True, type_save)
                ),
                MDRectangleFlatButton(
                    text="ЗАКРЫТЬ",
                    on_press=lambda e: self.show_message_in_bar("Настройки сохранены", dialog)
                )
            ],
        )
        dialog.open()

    def show_message_in_bar(self, text_message: str, dg: MDDialog = None, restart: bool = False, type_save: str = None):
        switches: list = []
        for child in self.root.ids.settings_sc.ids.sett.children:
            for el in child.children:
                if isinstance(el, MDSwitch):
                    switches.append(el.active)

        icon = None
        chips: list = []
        for child in self.root.ids.settings_sc.ids.chips_box.children:
            if isinstance(child, MDChip):
                chips.append(child.active)
                if child.active: icon = child.icon_left
        if icon:
            self.config_app = FileConfig(**{'current_diff': chips, 'enable_switches': switches})
            if type_save == 'save':
                Depends.File.save_config(self.config_app)
            else:
                self.config_app = FileConfig()
                Depends.File.save_config(self.config_app)
            if dg:
                dg.dismiss()
            if restart:
                self.shutdown_dg()
            Snackbar(
                text=text_message + Depends.File.get_difficulty_name(icon),
                snackbar_x="10dp",
                snackbar_y="10dp",
                size_hint_x=1
            ).open()
        else:
            self.warring_dg()

    def warring_dg(self):
        def close_dg(dg):
            if dg: dg.dismiss()
        dialog = MDDialog(
            title='ПРЕДУПРЕЖДЕНИЕ',
            text='Не выбрана сложность игрового процесса!',
            buttons=[MDRectangleFlatButton(
                text="ПОНЯТНО",
                on_press=lambda e: close_dg(dialog),
            ),]
        ).open()


if __name__ == '__main__':
    MainApp().run()
