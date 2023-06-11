import json
from dataclasses import dataclass, Field

from pydantic import BaseModel


class FileConfig(BaseModel):
    current_diff: list[bool] = [False, False, True]
    enable_switches: list[bool] = [False, True]


@dataclass
class OpenGame:
    current_open_game: str


class Depends:
    class File:
        @staticmethod
        def __create_config_file():
            with open('app_config.json', 'w') as config:
                config.write(json.dumps(FileConfig().dict(), indent=4))
                return FileConfig()

        @classmethod
        def get_config(cls):
            try:
                with open('app_config.json', 'r') as config:
                    return FileConfig(**json.loads(config.read()))
            except FileNotFoundError:
                return cls.__create_config_file()

        @staticmethod
        def save_config(config: FileConfig = FileConfig()):
            with open('app_config.json', 'w') as conf:
                conf.write(json.dumps(config.dict(), indent=4))
                return None

        @staticmethod
        def get_difficulty_name(name_diff: str):
            if name_diff == 'baby-carriage':
                return ', молокосос.'
            if name_diff == 'bullet':
                return ', товарищ солдат.'
            if name_diff == 'skull':
                return ', оверлорд.'

        @staticmethod
        def get_summary():
            with open('summary.tx', 'r', encoding='utf8') as f:
                return f.read()

    @dataclass
    class Names:
        app_header: str = """[size=28sp][b]Вы зашли в приложение «Математические игры для студентов СПО»[/b][/size]"""
        app_summary: str = ''
        settings_summary = """
Чтобы выбрать сложность, зажмите кнопку с соответствующим значком после чего приложение оповестит вас о выбранной сложности.
Не забудьте сохранить изменения!
        """
        game_summary: str = """
[size=48sp]Добро пожаловать![/size]
\n[size=28sp]Чтобы начать игру, нажмите кнопку со стрелкой вправо[/size]
        """
        start_game_tip: str = "Здесь возможно была подсказка..."
