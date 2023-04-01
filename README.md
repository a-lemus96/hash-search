# Map Abstract Data Type Using a Hash Table
Implementation of a Map ADT based on a hash table using Python built-in types. The table uses linear probing for solving collisions and a multiplicative hash function.

### Running tests for HashTable datatype
---
The script `test_hash.py` contains a battery of tests for evaluating the correctness of the hash table. Simply run `python test_hash.py -m=M -n=N` being `M` the size of the table and `N` the number of random character for each data associated to each key.

Specifically, it performs the following tests:

1. Creates an empty hash table of size $m$.
2. Inserts `m` elements.
3. Randomly selects `m//2` of the keys to delete their associated records.
4. Selects `m//3` of the first inserted keys to either update or insert records.
5. Searchs for the records associated to the first inserted keys, some of the results are `None` since some keys do not exist anymore.
6. Attempts to delete `m//3` of the first inserted keys. Here the operation is silent if succesful and displays message if key does not exist.

The table is displayed after applying each operation. Here is a screenshot of how the result should look like:

![image](https://user-images.githubusercontent.com/95151624/229262296-d8f5097c-30a3-4b94-815a-9afec310c16c.png)

### Running tests for RevHashTable datatype
---
The script `test_reverse.py` contains the same battery of tests for evaluating the correctness of the hash table with reversed linear probing for handling collisions. Simply run `python test_reverse.py -m=M -n=N` being `M` the size of the table and `N` the number of random character for each data associated to each key. The script performs the same tests as in the case aforementioned. Here is a screenshot of how the output format should look like:

![image](https://user-images.githubusercontent.com/95151624/229262421-93f27096-f5b5-4455-9ec7-f643002f54a6.png)

### Hash tables performance for implementing 1-D range search
---
Hash tables are not well suited for range queries of the form: "find all keys $k$ s.t. $k_{min}\leq k\leq k_{max}$". The argument is that it is not enough with doing just 2 searches and leveraging the structure of the distribution of keys within the structure since the structure is random by construction. The only possible way to retrieve all keys within the interval of interest is to test every element of the table to see if it lies inside the interval. This would lead to an algorithm which runs in $O(n)$. Binary Search Trees (BSTs) are better suited for this task, being able to perform range searches in $O(\log_2{n} + K)$ where $K$ is the number of elements inside the interval of interest. To see an implementation of BSTs for 1-dimensional range searches please visit my [bst-range-search
](https://github.com/a-lemus96/bst-range-search) repository.
