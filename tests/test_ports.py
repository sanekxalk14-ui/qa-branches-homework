import unittest
from netutils.ports import parse_port

class TestParsePort(unittest.TestCase):

    def test_valid_int_port(self):
        """Тестирует валидные целые числа в диапазоне 1–65535."""
        valid_ports = [1, 1024, 65535]
        for port in valid_ports:
            with self.subTest(port=port):
                result = parse_port(port)
                self.assertEqual(result, port)

    def test_valid_string_port(self):
        """Тестирует валидные строки, которые можно преобразовать в int."""
        test_cases = [
            ("1", 1),
            ("80", 80),
            ("65535", 65535),
            ("  443  ", 443),  # с пробелами
        ]
        for string_port, expected in test_cases:
            with self.subTest(string_port=string_port):
                result = parse_port(string_port)
                self.assertEqual(result, expected)

    def test_invalid_int_range(self):
        """Тестирует целые числа вне диапазона."""
        invalid_ports = [0, -1, 65536, 100000]
        for port in invalid_ports:
            with self.subTest(port=port):
                with self.assertRaises(ValueError):
                    parse_port(port)

    def test_invalid_string_format(self):
        """Тестирует строки с неверным форматом."""
        invalid_strings = [
            "",           # пустая строка
            "   ",        # только пробелы
            "abc",        # буквы
            "12a",        # смешанные символы
            "+80",        # знак +
            "-80",        # знак -
            "1.5",       # дробное число
        ]
        for invalid_str in invalid_strings:
            with self.subTest(invalid_str=invalid_str):
                with self.assertRaises(ValueError):
                    parse_port(invalid_str)

    def test_wrong_types(self):
        """Тестирует неверные типы данных."""
        wrong_types = [
            None,
            [],
            {},
            3.14,
            True,   # bool — подкласс int, но должен быть ошибкой
            False,  # bool
            [80],
            {"port": 80},
        ]
        for wrong_type in wrong_types:
            with self.subTest(wrong_type=type(wrong_type).__name__):
                with self.assertRaises(TypeError):
                    parse_port(wrong_type)

if __name__ == "__main__":
    unittest.main(verbosity=2)