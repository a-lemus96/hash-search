# stdlib modules
import math
from typing import Tuple

class MapHash:
    """Implementation of the Map ADT using a Hash Table."""
    def __init__(self, size: int, alpha: float = 1/math.pi, n: int = 10):
        """Constructor method.
        ------------------------------------------------------------------------
        Args:
            size: > 0. Length of the hash table
            alpha: < 1. Multiplicative real number for hash fn
            n: number of digits to consider for multiplicative hash fn"""
        self.size = size
        self.slots = size # available slots
        self.records = size * [2 * (None,)] # record is a 2-tuple
        self.alpha = alpha
        self.ndigits = n

    def __contains__(self, key: int) -> bool:
        """In operator.
        ------------------------------------------------------------------------
        Args:
            key: record key
        Returns:
            bool: True if key is present, False otherwise"""
        pos = self.__search(key)
        if pos>=0:
            return True
        return False

    def __getitem__(self, key: int) -> any:
        """Method to access a record through its key using the '[]' subscript 
        operator.
        ------------------------------------------------------------------------
        Args:
            key: record key
        Returns:
            any: Python object associated to that key"""
        return self.get(key)

    def __setitem__(self, key: int, data: any) -> None:
        """Method for updating a record through its key using the '[]' subscript
        operator.
        ------------------------------------------------------------------------
        Args:
            key: record key
            data: Python object
        Returns:
            None"""
        self.put(key, data)

    def __len__(self) -> Tuple[int, int]:
        """Length method. Returns size of hash table and number of available
        slots."""
        return self.size, self.slots

    def __str__(self):
        """String representation method"""

        return ' '.join(f"({str(k)}, {str(d)})" for k, d in self.records)

    def __hash(self, key) -> int:
        """Multiplicative hash method for integer-valued keys.
        ------------------------------------------------------------------------
        Args:
            key: record key
        Returns:
            int: hash table idx that key is mapped to"""
        
        return int(((k * self.alpha) % 1) * 10**(-self.ndigits))


    def __search(self, key) -> int:
        """Search method for computing index in self.values list.
        ------------------------------------------------------------------------
        Args:
            key: record key
        Returns:
            pos: position in hash table where key was found, otherwise -1"""
        pos = self.__hash(key)
        found_key, _ = self.records[pos]
        if found_key == key:
            return pos

        return -1
            

    def get(self, key) -> any:
        """Public method for getting an element associated to a key.
        ------------------------------------------------------------------------
        Args:
            key: record key
        Returns:
            Any: Python object associated to that key. None if key is not
                 present inside the table"""
        pos = self.__search(key)
        if pos >= 0:
            return self.data[pos]
        return None

    def put(self, key, data):
        """Add new data value. If an element with the same key already exists, 
        replace it with the new one.
        ------------------------------------------------------------------------
        Args:
            key: record key
            data: Python object"""
        if self.slots > 0: # check if there is room in table
            pos = self.__search(key)
            if pos < 0: # key is not present in table
                
            else: # key was found, update associated data
                self.data[pos] = data
        else:
            raise Exception("Unable to insert record. Not enough space")

        

mh = MapHash(10)
print(mh)
