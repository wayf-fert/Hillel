class GameEventException(Exception):
    """
    Exception for processing game events.

    Args:
        event_type (str): Type of event (e.g., "death", "levelUp").
        details (dict): Dictionary with information about the event.
    """
    def __init__(self, event_type: str, details: dict) -> None:
        self.event_type = event_type
        self.details = details
        super().__init__(f"Game event of type {event_type} occurred with details: {details}")


def simulate_game_event(event_type: str, details: dict) -> None:
    """
    Simulates a game event and throws a corresponding exception.

    Args:
        event_type (str): Type of event.
        details (dict): Additional information about the event.

    Raises:
        GameEventException: Exception for game event.
    """
    raise GameEventException(event_type, details)


def main():
    try:
        simulate_game_event(
            event_type="You're dead!💀",
            details={"cause": "Sword strike⚔️", "location": "Forest of The Hungry Shadows\U0001F47F"}
        )
    except GameEventException as e:
        if e.event_type == "You're dead!💀":
            print(f"Handling game event: {e.event_type}")
            print(f"Cause: {e.details['cause']}")
            print(f"Location: {e.details['location']}")
        elif e.event_type == "levelUp":
            print(f"Event: {e.event_type}")
            print(f"New Level: {e.details.get('new_level')}")
            print(f"Experience Points: {e.details.get('experience_points')}")
        else:
            print(f"Unhandled event: {e.event_type}")
            print(f"Details: {e.details}")


if __name__ == "__main__":
    main()
