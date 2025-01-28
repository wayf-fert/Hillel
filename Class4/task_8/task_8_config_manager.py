import configparser


class IniConfigManager:
    """
    Контекстний менеджер для автоматичного зчитування та запису конфігураційного файлу у форматі .ini.

    Attributes:
        filepath (str): Шлях до файлу конфігурації.
        config (configparser.ConfigParser): Об'єкт для зберігання і маніпуляції конфігураційними даними.
    """

    def __init__(self, filepath: str) -> None:
        """Ініціалізує контекстний менеджер з указаним шляхом до файлу конфігурації."""
        self.filepath = filepath
        self.config = configparser.ConfigParser()

    def __enter__(self) -> configparser.ConfigParser:
        self.config.read(self.filepath)
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Записує конфігураційний файл при виході з контексту.

        Args:
            exc_type: Тип виключення, якщо виникло.
            exc_val: Значення виключення, якщо виникло.
            exc_tb: Трасування виключення, якщо виникло.
        """
        with open(self.filepath, 'w') as file:
            self.config.write(file)


config_file = "task_8_config_file.ini"

with IniConfigManager(config_file) as config:
    if 'Settings' not in config:
        config['Settings'] = {}
    config['Settings']['theme'] = 'deep_dark'
    config['Settings']['language'] = 'ukrainian'
    config['Settings']['size'] = '300'
