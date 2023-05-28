from kivy.lang import Builder
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.scrollview import MDScrollView


class Drawer(MDNavigationDrawer):
    pass


class MenuExamples(MDScrollView):
    NAMES = {
        'Быстрый счёт': 'counter',
        'Алгебра': 'square-root',
        'Геометрия': 'axis-arrow',
        'Аксиомы': 'format-text-rotation-down-vertical',
        'Алогитмика': 'language-python',
        'Теория игр': 'controller'
    }

    def __init__(self, **kwargs):
        super(MenuExamples, self).__init__(kwargs)
        list_items = MDList()
        for text, icon in self.NAMES.items():
            wid_t = f"""
OneLineIconListItem:
    text: '{text}'
    IconLeftWidget:
        icon: '{icon}'"""
            wid = Builder.load_string(wid_t)
            list_items.add_widget(wid)
        self.add_widget(list_items)
