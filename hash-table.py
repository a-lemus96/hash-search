class MapHash:
    """Implementation of the Map ADT using a Hash Table."""
    def __init__(self, size):
        """Constructor method"""
        self.size = size
        self.values = size * [-1]

    def __len__(self):
        """Length method"""
        return self.size

    def __search(self, key):
        """Search method for computing index in self.values list."""
        pass
