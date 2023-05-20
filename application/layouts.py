from kivymd.uix.boxlayout import MDBoxLayout


class StartScreenLayout(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = 'start_screen_layout'
        self.orientation = 'vertical'
