from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.toolbar import MDTopAppBar

from py.dependencies import Depends


class StartScreen(MDScreen):
    pass


class SettingsScreen(MDScreen):
    pass


class BottomBar(MDTopAppBar):

    def show_difficulty(self):
        config = Depends.FileConfig.get_file_config()
        return [[config.difficulty, lambda e: self.open_dialog_difficulty(config.difficulty)]]

    @staticmethod
    def open_dialog_difficulty(diff):
        dialog = MDDialog(
            text=f"Текущая сложность {Depends.FileConfig.init_diff(diff)}",
            buttons=[
                MDRectangleFlatButton(
                    text="ПОНЯТНО",
                    on_press=lambda e: dialog.dismiss()
                )
            ],
        )
        dialog.open()
