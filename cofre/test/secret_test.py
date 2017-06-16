import unittest
from cofre.secret import SecretSharing

class SecretSharingTestCase(unittest.TestCase):
    def test_split_secret(self):
        secret = 25
        ss = SecretSharing(4, 2)
        shares = ss.split_secret(secret)

        self.assertEqual(len(shares), 4)
        with self.assertRaises(ValueError):
            ss = SecretSharing(4, 8)

        with self.assertRaises(ValueError):
            ss = SecretSharing(-5, 3)
        
        with self.assertRaises(ValueError):
            ss = SecretSharing(2, -3)

if __name__ == '__main__':
    unittest.main()
