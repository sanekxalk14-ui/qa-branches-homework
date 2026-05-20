def parse_port(value):
    """
    Преобразует value в номер порта (int) и валидирует диапазон.

    Args:
        value: int или str

    Returns:
        int: номер порта в диапазоне 1..65535

    Raises:
        TypeError: если тип не int и не str, или если передан bool
        ValueError: если значение вне диапазона или строка не может быть преобразована
    """
    # Проверка типа: bool считается неверным типом
    if isinstance(value, bool):
        raise TypeError("port must not be boolean")

    if isinstance(value, int):
        pass  # int допустим
    elif isinstance(value, str):
        # Убираем пробелы
        stripped = value.strip()
        if not stripped:  # пустая после strip
            raise ValueError("port string cannot be empty after stripping")
        if not stripped.isdigit():
            raise ValueError("port string must contain only digits")
        # Преобразуем в int
        try:
            value = int(stripped)
        except ValueError:
            raise ValueError("cannot convert string to int")
    else:
        # Любой другой тип
        raise TypeError(f"port must be int or str, not {type(value).__name__}")


    # Проверка диапазона
    if value < 1 or value > 65535:
        raise ValueError(f"port {value} out of range (1–65535)")

    return value