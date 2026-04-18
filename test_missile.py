import unittest
from missile import Missile

class TestMissile(unittest.TestCase):
    def test_launch(self):
        m = Missile("Test", 100, 1.5)
        self.assertIn("launched", m.launch())

if __name__ == "__main__":
    unittest.main()
