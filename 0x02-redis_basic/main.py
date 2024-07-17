#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

# Test cases
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    retrieved_value = cache.get(key, fn=fn)
    assert retrieved_value == value, f"Error: {retrieved_value} != {value}"
    print(f"Stored and retrieved: {retrieved_value}")

# Additional tests
data = b"hello"
key = cache.store(data)
print(key)
print(cache.get(key))
print(cache.get_str(key))

data_int = 42
key_int = cache.store(data_int)
print(key_int)
print(cache.get(key_int))
print(cache.get_int(key_int))
