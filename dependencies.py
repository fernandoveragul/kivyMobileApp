from dataclasses import dataclass


@dataclass
class RootIds:
    root_screen: str = 'root_screen'
    screen_manager: str = 'screen_manager'
    navigation_layout: str = 'navigation_layout'
    navigation_drawer: str = 'navigation_drawer'

    start_screen: str = 'start_screen'
    start_screen_layout: str = 'start_screen_layout'


@dataclass
class SummaryApp:
    summary: str = """
    [size=24]Математические игры[/size]
    Данное приложение разработано для поддержания и повышения аналитических 
    и логических знаний студентов СПО.
    """


@dataclass
class DifficultVariable:
    easy: str = 'power-socket-us'
    bullet: str = 'bullet'
    nightmare: str = 'skull-scan'
