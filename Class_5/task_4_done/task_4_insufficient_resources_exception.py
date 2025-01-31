class InsufficientResourcesException(Exception):
    def __init__(self, required_resource: str, required_amount: float, current_amount: float):
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
        message = (f"Not enough resources. Requested resource {required_amount} {required_resource}, "
                   f"available - {current_amount}")
        super().__init__(message)


class Player:
    def __init__(self, resources: dict = None):
        self.resources = resources if resources else {"gold": 100, "mana": 50}

    def perform_action(self, required_resource: str, required_amount: float):
        current_amount = self.resources.get(required_resource, 0)
        if current_amount < required_amount:
            raise InsufficientResourcesException(required_resource, required_amount, current_amount)

        self.resources[required_resource] -= required_amount
        print(f"Action done! Used {required_amount} {required_resource}. "
              f"Balance: {self.resources[required_resource]}.")


player_resources = {"gold": 64, "mana": 82}
player = Player(player_resources)

try:
    player.perform_action("gold", 120)
except InsufficientResourcesException as e:
    print(e)

try:
    player.perform_action("mana", 30)
except InsufficientResourcesException as e:
    print(e)

try:
    player.perform_action("gold", 80)
except InsufficientResourcesException as e:
    print(e)

