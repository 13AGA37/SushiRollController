class SushiRoll:
    def __init__(self, name, rice, nori, fillings, optional_toppings=None):
        self._name = name
        self._rice = rice
        self._nori = nori
        self._fillings = fillings
        self._optional_toppings = optional_toppings if optional_toppings else []

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_rice(self):
        return self._rice

    def set_rice(self, value):
        self._rice = value

    def get_nori(self):
        return self._nori

    def set_nori(self, value):
        self._nori = value

    def get_fillings(self):
        return self._fillings

    def set_fillings(self, value):
        self._fillings = value

    def get_optional_toppings(self):
        return self._optional_toppings

    def add_optional_topping(self, topping):
        self._optional_toppings.append(topping)

    def remove_optional_topping(self, topping):
        if topping in self._optional_toppings:
            self._optional_toppings.remove(topping)

    def change_recipe(self, new_rice, new_nori, new_fillings):
        self.set_rice(new_rice)
        self.set_nori(new_nori)
        self.set_fillings(new_fillings)

def create_custom_roll(name, rice, nori, fillings, optional_toppings=None):
    if not isinstance(name, str) or not isinstance(rice, str) or not isinstance(nori, str) or not isinstance(fillings, list):
        raise ValueError("Invalid input types")
    return SushiRoll(name, rice, nori, fillings, optional_toppings)

class SushiRollController:
    def __init__(self):
        self.rolls = []

    def add_roll(self, roll):
        self.rolls.append(roll)

    def get_rolls_for_restaurant(self):
        return [{"name": roll.get_name(), "rice": roll.get_rice(), "nori": roll.get_nori(), "fillings": roll.get_fillings(), "optional_toppings": roll.get_optional_toppings()} for roll in self.rolls]

    def get_rolls_for_website(self):
        return [{"name": roll.get_name(), "description": f"{roll.get_rice()} with {', '.join(roll.get_fillings())}", "toppings": roll.get_optional_toppings()} for roll in self.rolls]

    def update_roll(self, roll_name, new_rice=None, new_nori=None, new_fillings=None, user_role=None):
        if user_role != "admin":
            raise PermissionError("Доступ запрещен. У вас нет прав для изменения роллов.")
        for roll in self.rolls:
            if roll.get_name() == roll_name:
                if new_rice:
                    roll.set_rice(new_rice)
                if new_nori:
                    roll.set_nori(new_nori)
                if new_fillings:
                    roll.set_fillings(new_fillings)
                return
        raise ValueError("Ролл не найден.")

controller = SushiRollController()

california_roll = SushiRoll("California Roll", "Sushi Rice", "Nori", ["Crab Sticks", "Avocado"], ["Egg", "Sesame Seeds"])
controller.add_roll(california_roll)

restaurant_view = controller.get_rolls_for_restaurant()
website_view = controller.get_rolls_for_website()

try:
    controller.update_roll("California Roll", new_rice="Brown Rice", user_role="admin")
except PermissionError as e:
    print(e)

print(restaurant_view)
print(website_view)
