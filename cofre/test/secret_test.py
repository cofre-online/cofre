import unittest
from cofre.secret import SecretSharing

class SecretSharingTestCase(unittest.TestCase):
    def test_instantiation(self):
        with self.assertRaises(ValueError):
            SecretSharing(4, 8)

        with self.assertRaises(ValueError):
            SecretSharing(-5, 3)

        with self.assertRaises(ValueError):
            SecretSharing(2, -3)

    def test_split_secret(self):
        secret = 10
        ss = SecretSharing(4, 2)
        shares = ss.split_secret(secret)

        self.assertEqual(len(shares), 4)
        self.assertEqual(shares[0][0], 1)
        self.assertEqual(shares[3][0], 4)

        self.assertNotEqual(shares[0][1], secret)
        self.assertNotEqual(shares[0][1], shares[1][1])

    def test_reconstruct_secret(self):
        secret = 68468
        ss = SecretSharing(8, 5)
        shares = ss.split_secret(secret)

        recon = ss.reconstruct_secret(shares[:5])

        self.assertEqual(recon, secret)

        recon = ss.reconstruct_secret(shares)

        self.assertEqual(recon, secret)
        
        with self.assertRaises(ValueError):
            ss.reconstruct_secret(shares[0])

        with self.assertRaises(ValueError):
            ss.reconstruct_secret([shares[0], shares[0], shares[1], shares[2], shares[3]])

    def test_generate_new_share(self):
        secret = 77545
        ss = SecretSharing(4, 2)
        shares = ss.split_secret(secret)

        new_share = ss.generate_new_share(shares, 37)
        self.assertEqual(new_share[0], 37)

        recon = ss.reconstruct_secret([shares[0], new_share])
        self.assertEqual(recon, secret)

        new_share = ss.generate_new_share(shares, 2)
        self.assertEqual(new_share, shares[1])

        with self.assertRaises(ValueError):
            ss.generate_new_share([shares[0]], 45)

        with self.assertRaises(ValueError):
            ss.generate_new_share([shares[0], shares[0]], 12)

        with self.assertRaises(ValueError):
            ss.generate_new_share(shares, 0)

        with self.assertRaises(ValueError):
            ss.generate_new_share(shares, -5)


if __name__ == '__main__':
    unittest.main()
