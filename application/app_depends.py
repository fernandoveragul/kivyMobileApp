from dataclasses import dataclass


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
