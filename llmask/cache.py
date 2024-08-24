import os
import json
import hashlib
from functools import wraps

CACHE_FILE = "/Users/majid/code/llmask/cache.jsonl"  # TODO: Proper path


def generate_cache_key(func_name, args, kwargs):
    """Generates a cache key based on the function name and its arguments."""
    key = json.dumps(
        {
            "func_name": func_name,
            "args": args,
            "kwargs": kwargs,
        },
        sort_keys=True,
    )
    return hashlib.md5(key.encode()).hexdigest()


def load_cache():
    """Loads the cache from the JSONL file."""
    if not os.path.exists(CACHE_FILE):
        return {}
    cache = {}
    with open(CACHE_FILE, "r") as f:
        for line in f:
            entry = json.loads(line)
            cache[entry["key"]] = entry
    return cache


def save_cache_entry(key, func_name, args, kwargs, result):
    """Saves a single cache entry to the JSONL file."""
    with open(CACHE_FILE, "a") as f:
        entry = {
            "key": key,
            "func_name": func_name,
            "args": args,
            "kwargs": kwargs,
            "result": result,
        }
        f.write(json.dumps(entry) + "\n")


def disk_cache(func):
    """Decorator to cache the result of a function to a JSONL file."""
    cache = load_cache()

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = generate_cache_key(func.__name__, args, kwargs)
        if key in cache:
            return cache[key]["result"]

        result = func(*args, **kwargs)
        cache[key] = {
            "key": key,
            "func_name": func.__name__,
            "args": args,
            "kwargs": kwargs,
            "result": result,
        }
        save_cache_entry(key, func.__name__, args, kwargs, result)
        return result

    return wrapper
