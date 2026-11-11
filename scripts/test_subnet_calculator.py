import unittest

from subnet_calculator import details


class TestCalculator(unittest.TestCase):
    def test_26(self):
        result = details('192.168.10.130/26')
        self.assertEqual(result['Network'], '192.168.10.128/26')
        self.assertEqual(result['Broadcast'], '192.168.10.191')
        self.assertEqual(result['Usable addresses'], 62)

    def test_31(self):
        result = details('10.0.0.0/31')
        self.assertEqual(result['Usable addresses'], 2)
        self.assertEqual(result['First usable'], '10.0.0.0')
        self.assertEqual(result['Last usable'], '10.0.0.1')

    def test_32(self):
        self.assertEqual(details('192.0.2.15/32')['Usable addresses'], 1)

    def test_no_ipv6(self):
        with self.assertRaises(ValueError):
            details('2001:db8::1/64')


if __name__ == '__main__':
    unittest.main()
