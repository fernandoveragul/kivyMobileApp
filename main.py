from pathlib import Path

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog

from py.dependencies import Depends
from py.screens import StartScreen, SettingsScreen, BottomBar
from py.drawer import Drawer, MenuExamples


class MainApp(MDApp):

    def __init__(self):
        super().__init__()
        self.menu = None
        self.summary_app = Depends.Names.summary
        self.config_app = Depends.FileConfig.get_file_config()

    def build(self):
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
        # 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.title = "Математические игры"
        self.theme_cls.primary_palette = "Lime"
        self.theme_cls.theme_style = "Dark"
        self.root = Builder.load_file(f"{Path(Path.cwd(), 'main.kv')}")

    def oc_menu(self, type_move: str = 'open'):
        self.root.ids.nav_drawer.set_state(type_move)

    def ch_screen(self, screen_name: str = 'start_screen', direction: str = 'left', dg: MDDialog = None):
        self.root.ids.screen_manager.transition.direction = direction
        self.root.ids.screen_manager.current = screen_name
        if dg:
            dg.dismiss()

    def shutdown_dg(self):
        dialog = MDDialog(
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

    def difficulty_dg(self):
        dialog = MDDialog(
            text=f"Текущая сложность {Depends.FileConfig.init_diff(self.config_app.difficulty)}",
            buttons=[
                MDRectangleFlatButton(
                    text="ВЫБРАТЬ",
                    on_press=lambda e: self.ch_screen('settings_screen', 'down', dialog)
                ),
                MDRectangleFlatButton(
                    text="ПОНЯТНО",
                    on_press=lambda e: dialog.dismiss()
                )
            ],
        )
        dialog.open()


if __name__ == '__main__':
    MainApp().run()
