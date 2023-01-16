
class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 protection: int = 0, potion: int = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.potion = potion

    def apply_armour(self, armours: dict) -> None:
        for armour in armours["armour"]:
            self.protection += armour["protection"]

    def apply_weapon(self, weapons: dict) -> None:
        self.power += weapons["weapon"]["power"]

    def apply_potion(self, potion: dict) -> None:
        if potion:
            power = potion["effect"].get("power", 0)
            self.power += power
            protection = potion["effect"].get("protection", 0)
            self.protection += protection
            hp = potion["effect"].get("hp", 0)
            self.hp += hp


def create_knight(knights: dict) -> Knight:
    return Knight(knights["name"], knights["power"], knights["hp"])
