def merge_json(obj1, obj2):
    merged = obj1.copy()
    for key, value in obj2.items():
        if key in merged:
            # If the key exists in obj1, prioritize obj1's value
            continue
        else:
            # If the key doesn't exist in obj1, add it to merged
            merged[key] = value
    return merged