# tableflow/middleware.py

def smart_search(data, value):
    """
    Universal search:
    - matches id (exact)
    - matches name/role (partial)
    - case insensitive
    """

    value = str(value).lower()
    results = []

    for item in data:

        for key, val in item.items():

            # 1. ID exact match
            if key == "id" and str(val) == value:
                results.append(item)
                break

            # 2. Name/Role/Text partial match
            if value in str(val).lower():
                results.append(item)
                break

    return results
