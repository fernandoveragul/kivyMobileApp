from pathlib import Path

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.navigationdrawer import MDNavigationDrawerItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar

from dependencies import AppData, SummaryApp


class MainApp(MDApp):

    def __init__(self):
        super().__init__()
        self.menu = None
        self.summary_app = SummaryApp.summary

    def build(self):
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
        # 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
        self.title = "Математические игры"
        self.icon = 'android'
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Lime"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file(f"{Path(Path.cwd(), 'main.kv')}")

    def open_close_menu(self, state: str = 'open'):
        self.root.ids.navigation_drawer.set_state(state)

    def change_screen(self, name_sc: str, direction: str = 'left'):
        self.root.ids.screen_manager.transition.direction = direction
        self.root.ids.screen_manager.current = name_sc

    def menu_hard_open(self):
        menu_items = [
            {
                "text": f"Салага",
                "viewclass": "MDRectangleFlatIconButton",
                "icon": "power-socket-us",
                "on_release": lambda x=f"Item": print(x),
                "size_hint_x": None,
                "pos_hint": {'center_x': .5, 'center_y': .5}
            },
            {},
            {
                "text": f"Ветеран",
                "viewclass": "MDRectangleFlatIconButton",
                "icon": "bullet",
                "on_release": lambda x=f"Item": print(x),
                "size_hint_x": None,
                "pos_hint": {'center_x': .5, 'center_y': .5}
            },
            {},
            {
                "text": f"Кошмар",
                "viewclass": "MDRectangleFlatIconButton",
                "icon": "skull-scan",
                "on_release": lambda x=f"Item": print(x),
                "size_hint_x": None,
                "pos_hint": {'center_x': .5, 'center_y': .5}
            },
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.ids.menu_opener,
            items=menu_items,
            width_mult=17,
            max_height=220,
            position="auto",
        )
        self.menu.open()


class MenuItem(MDNavigationDrawerItem):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        if AppData.application.theme_cls.theme_style == 'Dark':
            self.text_color = "#FFFFFF"
            self.selected_color = '#FFFFFF'
        else:
            self.text_color = '#000000'
        self.font_style = 'Body2'


class StartScreenBar(MDTopAppBar):
    id = 'app_bottom_bar'
    use_overflow = True
    left_action_items = [['skull-scan']]
    elevation = 0


class StartScreenLayout(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = 'start_screen_layout'
        self.orientation = 'vertical'


class StartScreen(MDScreen):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)


class SettingsScreen(MDScreen):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)


if __name__ == '__main__':
    AppData.application = MainApp()
    AppData.application.run()
