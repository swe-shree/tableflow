# tableflow/middleware.py

def log(message: str):
    print(f"[MIDDLEWARE] {message}")


def auth_check(user: str):
    return user == "admin"


# ----------------------------
# FILTERING
# ----------------------------
def filter_data(data, key: str, value):
    """
    Filters list of dictionaries based on key-value match
    """
    return [item for item in data if str(item.get(key)) == str(value)]


# ----------------------------
# SORTING
# ----------------------------
def sort_data(data, key: str, reverse: bool = False):
    """
    Sorts list of dictionaries by given key
    """
    return sorted(data, key=lambda x: x.get(key), reverse=reverse)


# ----------------------------
# PAGINATION
# ----------------------------
def paginate_data(data, page: int = 1, limit: int = 10):
    """
    Returns paginated results
    """
    start = (page - 1) * limit
    end = start + limit
    return data[start:end]