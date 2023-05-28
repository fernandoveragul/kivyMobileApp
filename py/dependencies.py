import json
from dataclasses import dataclass

from pydantic import BaseModel


@dataclass
class Names:
    summary: str = """
    [size=18sp]Математические игры[/size]
    Данное приложение разработано для поддержания и повышения аналитических 
    и логических знаний студентов СПО.
    """
    easy: str = 'power-socket-us'
    bullet: str = 'bullet'
    nightmare: str = 'skull-scan'


class DefaultConfig(BaseModel):
    difficulty: str = 'power-socket-us'
    enable_time: bool = False
    enable_time_to_example: bool = False
    enable_tips: bool = False


class AppConfig(BaseModel):
    difficulty: str
    enable_time: bool
    enable_time_to_example: bool
    enable_tips: bool


class FileConfig:
    @staticmethod
    def get_file_config():
        try:
            with open('app_config.json', 'r') as config:
                return AppConfig(**json.loads(config.read()))
        except FileNotFoundError:
            with open('app_config.json', 'w') as config:
                config.write(json.dumps(DefaultConfig().dict(), indent=4))

    @staticmethod
    def init_diff(name_icon: str):
        if name_icon == Names.easy:
            return "САЛАГА"
        if name_icon == Names.bullet:
            return "ВЕТЕРАН"
        if name_icon == Names.nightmare:
            return "КОШМАР"


class Depends:
    class Names(Names):
        pass

    class FileConfig(FileConfig):
        pass
