from Crypto.Random import random
from Crypto.Util import number

class SecretSharing(object):
    def __init__(self, num_shares, threshold):
        self.num_shares = num_shares
        self.threshold = threshold
        self.prime = number.getPrime(256)

    def split_secret(self, secret):
        coefficients = []
        coefficients.append(secret)

        for i in range(1, self.threshold-1):
            coefficients.append(random.randrange(self.prime))

        shares = self._get_points(self.num_shares, coefficients)

        return shares

    def reconstruct_secret(self, shares):
        share_set = set(shares)
        if (len(share_set) < len(shares)):
            raise Exception('provided duplicate share')
        if (len(share_set) < self.threshold):
            raise Exception('insufficient shares')
        
        secret = 0
        
        for j in range(self.threshold):
            y = shares[j][1]
            numerator = 1
            denominator = 1
            for i in range(self.threshold):
                if j == i:
                    continue
                numerator = (numerator * shares[i][0] * -1) % self.prime
                denominator = (denominator * (shares[j][0] - shares[i][0])) % self.prime
            
            secret = (self.prime + secret + (y * numerator * number.inverse(denominator, self.prime))) % self.prime

        return secret

    def generate_new_share(self, shares, num):
        # TODO Recover polynomial f(x) from shares and calculate f(num)
        pass

    def _get_points(self, n, coefficients):
        points = []
        for i in range(n):
            x = i + 1
            fx = 0
            for j in range(len(coefficients)):
                fx += coefficients[j] * pow(x, j, self.prime)

            points.append((x, fx))

        return points
