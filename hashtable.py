# stdlib modules
import math
import random
from typing import Tuple

class HashMap:
    """Implementation of the Map ADT using a Hash Table."""

    # SPECIAL METHODS

    def __init__(
            self, 
            size: int, 
            alpha: float = 1 / math.pi, 
            n: int = 10, 
            step: int = 1):
        """Constructor method.
        ------------------------------------------------------------------------
        Args:
            size: > 0. Length of the hash table
            alpha: < 1. Multiplicative real number for hash fn
            n: number of digits to consider for multiplicative hash fn
            step: step size for linear probing"""
        self.size = size
        self.slots = size # available slots
        self.records = (size) * [None]
        self.mask = size * [False] # boolean mask for deletion operation
        self.alpha = alpha
        self.ndigits = n
        # check if step and table length are coprime
        if math.gcd(step, self.size) != 1:
            raise Exception("Step size and len(table) must be coprime ints.")
        self.step = step

    def __contains__(self, key: int) -> bool:
        """In operator.
        ------------------------------------------------------------------------
        Args:
            key: record key
        Returns:
            bool: True if key is present, False otherwise"""
        pos = self.__search(key)
        if self.records[pos] is not None:
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

    def __delitem__(self, key: int) -> None:
        """Method for deleting a record through its key using the del operator
        ------------------------------------------------------------------------
        Args:
            key: record key
        Returns:
            None"""
        pos = self.__search(key)
        if self.records[pos] is None:
            print(f"There is no entry for key={key} inside the table")
            return

        self.records[pos] = None # reset entry in table
        self.mask[pos] = True # tag this entry for search method
        self.slots +=1 # update available amount of slots

    def __len__(self) -> Tuple[int, int]:
        """Length method. Returns size of hash table and number of available
        slots."""
        return self.size, self.slots

    def __str__(self):
        """String representation method"""

        return '[' + ', '.join(f"{str(record)}" for record in self.records) + ']'

    # PRIVATE METHODS

    def __hash(self, key) -> int:
        """Multiplicative hash method for integer-valued keys.
        ------------------------------------------------------------------------
        Args:
            key: record key
        Returns:
            int: hash table idx that key is mapped to"""
        f_k = ((key * self.alpha) % 1) / 10**(-self.ndigits)
        
        return int(f_k % self.size)

    def __linear_prob(
            self, 
            key: int, 
            pos: int, 
            count: int, 
            step: int,
            mode: str = 'get'
            ) -> int:
        """Linear probing method for solving collisions in hash table. It may 
        work with any step size such that step and table size are coprime.
        ------------------------------------------------------------------------
        Args:
            key: record key
            pos: table position to probe
            count: counter of iterations
            step: step size
            mode: 'put' or 'get'
        Returns:
            pos: position where found key or first None entry""" 
        record = self.records[pos]
        new_pos = (pos + step) % self.size
        count += 1

        if count > self.size: # 1st termination case
            return None

        if record is None and mode == 'put': # 2nd termination case
            return pos

        if record is None and mode == 'get': # 3rd termination case
            if self.mask[pos] == True:
                # probe next slot
                return self.__linear_prob(key, new_pos, count, step, mode)
            else:
                return pos
        
        found_key, _ = record
        if found_key == key: # 3rd termination case
            return pos

        # probe next slot
        return self.__linear_prob(key, new_pos, count, step, mode) 

    def __search(self, key: int, mode: str = 'get') -> int:
        """Search method for computing index in self.values list.
        ------------------------------------------------------------------------
        Args:
            key: record key
            mode: 'inserting' or 'retrieving' record
        Returns:
            pos: position in hash table where key was found, otherwise -1"""
        pos = self.__hash(key)
        count = 0 # counter to avoid exceeding max recursion depth

        return self.__linear_prob(key, pos, count, self.step, mode)
            

    # PUBLIC METHODS

    def get(self, key) -> any:
        """Public method for getting an element associated to a key.
        ------------------------------------------------------------------------
        Args:
            key: record key
        Returns:
            Any: Python object associated to that key. None if key is not
                 present inside the table"""
        pos = self.__search(key)
        if pos is not None:
            if self.records[pos] is not None:
                return self.records[pos][1]
        return None

    def put(self, key, data):
        """Add new data value. If an element with the same key already exists,
        replace it with the new one.
        ------------------------------------------------------------------------
        Args:
            key: record key
            data: Python object"""
        if self.slots < 1: # check if there is room in table
            print(f"Unable to insert record ({key},{data}). Not enough space\n")
            return

        pos = self.__search(key, mode='put')
        if pos is not None:
            if self.records[pos] is None:
                self.slots -= 1 # update number of available slots
                self.mask[pos] = False # update flag value
            self.records[pos] = (key, data) # update associated data
            return
        
        print(f"Unable to update ({key}, {data}). Record is not present")
