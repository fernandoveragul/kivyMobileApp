from dataclasses import dataclass
from enum import Enum

from kivymd.app import MDApp


@dataclass
class AppData:
    application: MDApp


@dataclass
class RootIds:
    root_screen: str = 'root_screen'
    screen_manager: str = 'screen_manager'
    navigation_layout: str = 'navigation_layout'
    navigation_drawer: str = 'navigation_drawer'

    start_screen: str = 'start_screen'
    start_screen_layout: str = 'start_screen_layout'
