from Crypto.Random import random
from Crypto.Util import number

class SecretSharing(object):
    def __init__(self, num_shares, threshold):
        if(num_shares < 1):
            raise ValueError("At least 1 share is needed")
        if(threshold < 1):
            raise ValueError("The threshold must be of at least 1")
        if(num_shares < threshold):
            raise ValueError("Threshold must be less or equal \
            than the number of shares")
        self.num_shares = num_shares
        self.threshold = threshold

    def split_secret(self, secret):
        coefficients = []
        coefficients.append(secret)

        prime = number.getPrime(256)

        for i in range(1, self.threshold):
            coefficients.append(random.randrange(prime))

        shares = self._get_points(self.num_shares, coefficients, prime)

        return shares

    def reconstruct_secret(self, shares):
        share_set = self._share_set(shares)
        prime = share_set[0][2]
        secret = 0
        
        for j in range(self.threshold):
            y = shares[j][1]
            numerator = 1
            denominator = 1
            for i in range(self.threshold):
                if j == i:
                    continue
                numerator = (numerator * shares[i][0] * -1) % prime
                denominator = (denominator * (shares[j][0] - shares[i][0])) % prime
            
            secret = (prime + secret + (y * numerator * number.inverse(denominator, prime))) % prime

        return secret

    def generate_new_share(self, shares, num):
        share_set = self._share_set(shares)
        prime = share_set[0][2]

        coefficients = self._recover_polynomial(share_set)

        return (num, self._get_point(num, coefficients, prime))

    def _share_set(self, shares):
        share_set = set(shares)
        if (len(share_set) < len(shares)):
            raise ValueError('provided duplicate share')
        if (len(share_set) < self.threshold):
            raise ValueError('insufficient shares')

        return share_set


    def _get_points(self, n, coefficients, prime):
        points = []
        for i in range(n):
            x = i + 1
            fx = self._get_point(x, coefficients)
            points.append((x, fx, prime))

        return points

    def _get_point(self, x, coefficients, prime):
        fx = 0
        for j in range(len(coefficients)):
            fx += coefficients[j] * pow(x, j, prime)
        
        return fx

    def _recover_polynomial(self, shares):
        prime = shares[0][2]

        for i in range(self.threshold):
