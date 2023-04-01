# Map Abstract Data Type Using a Hash Table
Implementation of a Map ADT based on a hash table using Python built-in types. The table uses linear probing for solving collisions and a multiplicative hash function.

### On hash tables performance for implementing 1-D range search
---
Hash tables are not well suited for range queries of the form: "find all keys $k$ s.t. $k_{min}\leq k\leq k_{max}$". The argument is that it is not enough with doing just 2 searches and leveraging the structure of the distribution of keys within the structure since the structure is random by construction. The only possible way to retrieve all keys within the interval of interest is to test every element of the table to see if it lies inside the interval. This would lead to an algorithm which runs in $O(n)$. Binary Search Trees (BSTs) are better suited for this task, being able to perform range searches in $O(\log_2{n} + K)$ where $K$ is the number of elements inside the interval of interest. To see an implementation of BSTs for 1-dimensional range searches please visit my [bst-range-search
](https://github.com/a-lemus96/bst-range-search) repository.
