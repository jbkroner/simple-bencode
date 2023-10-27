import unittest

from simple_bencode import decode, _decode, _decode_list, _decode_dict


class test_decode(unittest.TestCase):
    def test_decode_int(self):
        self.assertEqual(decode(b"i42e"), 42)

    def test_decode_str(self):
        self.assertEqual(decode(b"4:test"), b"test")

    def test_decode_list(self):
        self.assertEqual(decode(b"li42e4:teste"), [42, b"test"])

    def test_decode_dict(self):
        self.assertEqual(
            decode(b"d4:name4:John3:agei30ee"), {"name": b"John", "age": 30}
        )

    def test__decode_int(self):
        self.assertEqual(_decode(b"i42e"), (42, b""))

    def test__decode_str(self):
        self.assertEqual(_decode(b"4:test"), (b"test", b""))

    # Tests for _decode_list
    def test__decode_list(self):
        self.assertEqual(_decode_list(b"li42e4:teste", []), ([42, b"test"], b""))

    # Tests for _decode_dict
    def test__decode_dict(self):
        self.assertEqual(
            _decode_dict(b"d4:name4:John3:agei30ee", {}),
            ({"name": b"John", "age": 30}, b""),
        )
