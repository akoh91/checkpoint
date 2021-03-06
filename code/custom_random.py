class CustomRandom():
    """
    Implements a custom random number generator for use in simulation.
    Uses the Lehmer pseudorandom number generator.
    """


    # Use constants suggested by Lemmis and Park.
    M = 2**31-1
    A = 48271
    Q = 44488
    R = 3399

    """
    Creates a new CustomRandom object.

    Args:
      seed: Integer. Seed for the random number generator.

    Returns:
      A new CustomRandom object.

    """
    def __init__(self, seed):
        self.seed = seed

    # Generates a pseudorandom number using Lehmer's algorithm.
    def next(self):
        rand = self.A * (self.seed % self.Q) - self.R * (self.seed / self.Q)

        if rand > 0:
            self.seed = rand
        else:
            self.seed = rand + self.M

        return self.seed

    # Generates a uniformly distributed floating point random number in the
    # range (0,1).
    def uniform_random(self):
        return float(self.next())/self.M

    # Generates an uniformly distributed integer random number in the range
    # (min, max).
    def random_in_range(self, min, max):
        return min + int(self.uniform_random() * ((max - min) + 1))