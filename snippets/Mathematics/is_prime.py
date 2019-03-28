def is_prime(n):
    """ Deterministic variant of the Miller-Rabin primality test. """
    if n in [2, 3, 5, 13, 19, 73, 193, 407521, 299210837]:
        return True

    if (n == 0) or (n == 1) or (any(n % p == 0 for p in [2, 3, 5, 13, 19, 73, 193, 407521, 299210837])):
        return False

    d, s = n - 1, 0
    while not d & 1:
        d, s = d >> 1, s + 1

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False

        p = pow(a, d, n)
        for i in range(s):
            if p == n - 1:
                return False
            p = (p * p) % n

        return True

    return not any(try_composite(w) for w in [2, 325, 9375, 28178, 450775, 9780504, 1795265022])
