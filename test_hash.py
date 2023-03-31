# stdlib modules
import argparse
import random as rand
import string

# custom modules
import hashtable as table

# instantiate argument parser
parser = argparse.ArgumentParser(description="Test Hash Map ADT")
parser.add_argument("-m", default=10, type=int,
                    help="Size of the hash table")
parser.add_argument("-n", default=5, type=int,
                    help="Lenght of record strings")
args = parser.parse_args()

t = table.HashMap(args.m)
print(f"Initalized hash table:\n{t}\n")
m, n = args.m, args.n

# create a list of random records to insert
rand_keys = rand.sample(range(10**9), m)
chars = string.ascii_letters + string.digits

# try to insert m + 1 elements
rand_strs = [''.join(rand.choice(chars) for _ in range(n)) for _ in range(m)]
to_insert = [(key, string) for key, string in zip(rand_keys, rand_strs)]

# insert records
for key, data in to_insert:
    t[key] = data

# print table after insertions
print(f"Hash table after insertions:\n{t}\n{t.mask}\n")

# randomly select half the records to delete
to_delete = rand.sample(to_insert, m // 2)

for key, _ in to_delete:
    del t[key]

# print table after deletions
print(f"Hash table after deletions:\n{t}\n{t.mask}\n")

# introduce a new half of data 
rand_keys = rand.sample(range(10**9), m//2)
rand_strs = [''.join(rand.choice(chars) for _ in range(n)) for _ in range(m//2)]
to_insert = [(key, string) for key, string in zip(rand_keys, rand_strs)]

# insert records
for key, data in to_insert:
    t[key] = data

# print table after new insertions
print(f"Hash table after new insertions:\n{t}\n{t.mask}\n")

# search for a not existing key and try to delete it
