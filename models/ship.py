from typing import Optional
from .modul import Modul


class Ship():

    def __init__(self, ship_name: str = "Ship Name not set", modules: Optional[list[Modul]] = None):
        self.ship_name: str = ship_name
        self.modules: Optional[list[Modul]] = modules

    def get_modules(self, modul_type: Modul.Type = Modul.Type.Active) -> list[Modul]:
        return [modul for modul in self.modules if modul.modul_type == modul_type]
