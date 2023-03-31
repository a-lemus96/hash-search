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

t = table.RevHashMap(args.m)
print(f"(*) Initalized hash table:\n{t}\n")
m, n = args.m, args.n

# create a list of random records to insert
rand_keys = rand.sample(range(10**9), m)
chars = string.ascii_letters + string.digits

# try to insert m elements
rand_strs = [''.join(rand.choice(chars) for _ in range(n)) for _ in range(m)]
to_insert = [(key, string) for key, string in zip(rand_keys, rand_strs)]
# insert records
for key, data in to_insert:
    t[key] = data

# print table after insertions
print(f"(*) Hash table after some insertions:\n{t}\n")

# randomly select a half of the records to delete
to_delete = rand.sample(to_insert, m // 2)
for key, _ in to_delete:
    del t[key]
# print table after deletions
deleted = [key for key, _ in to_delete]
print(f"(*) Hash table after deleting records with keys in {deleted}:\n{t}\n")

# update/insert a third of the keys
up_keys = rand.sample(rand_keys, m//3)
up_strs = [''.join(rand.choice(chars) for _ in range(n)) for _ in range(m//3)]
to_update = [(key, string) for key, string in zip(up_keys, up_strs)]

# insert/update records
for key, data in to_update:
    t[key] = data

# print table after new insertions/updates
updated = [key for key, _ in to_update]
print(f"(*) Hash table after updating/inserting in keys {updated}:\n{t}\n")

# search for the initial key values that were inserted into the table
query_results = []
for key in rand_keys:
    query_results.append(t[key])
print(f"(*) Query results for keys {rand_keys}:\n{query_results}\n")

# attempt to delete some of the original keys
rand_keys = rand.sample(rand_keys, m//3)
print(f"(*) Deleting entries for some keys")
for key in rand_keys:
    del t[key]
print(f"(*) Hash table after deleting records with keys {rand_keys}:\n{t}")
