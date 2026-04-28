def smart_search(data, value):
    """
    Universal search across ALL fields:
    - id, name, role, email, phone, etc.
    - partial + exact match
    - case insensitive
    """

    value = str(value).lower()
    results = []

    for item in data:
        matched = False  # prevents duplicate entries

        for val in item.values():

            # convert everything to string and compare
            if value in str(val).lower():
                matched = True
                break

        if matched:
            results.append(item)

    return results
