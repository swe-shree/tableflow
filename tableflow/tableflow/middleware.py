def smart_search(data, value):
    value = str(value).lower()
    results = []

    for item in data:
        for v in item.values():
            if value in str(v).lower():
                results.append(item)
                break

    return results
