def smart_search(data, value=None, page=1, limit=10, sort_by=None, sort_order="asc"):
    """
    Search, filter, sort, and paginate data with robust error handling.
    
    Args:
        data (list): List of dictionaries to search
        value (str, optional): Search term to filter by
        page (int): Page number (1-indexed), default 1
        limit (int): Items per page, default 10
        sort_by (str, optional): Field name to sort by
        sort_order (str): 'asc' or 'desc', default 'asc'
    
    Returns:
        dict: Contains 'total', 'page', 'limit', and 'data' keys
    
    Raises:
        TypeError: If data is not a list
        ValueError: If page/limit are invalid or sort_order is invalid
    
    Example:
        >>> data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        >>> result = smart_search(data, value="Alice", page=1, limit=10)
        >>> print(result)
        {'total': 1, 'page': 1, 'limit': 10, 'data': [{'name': 'Alice', 'age': 30}]}
    """
    
    # ✅ Input validation
    if not isinstance(data, list):
        raise TypeError("data must be a list")
    if not isinstance(page, int) or page < 1:
        raise ValueError("page must be an integer >= 1")
    if not isinstance(limit, int) or limit < 1:
        raise ValueError("limit must be an integer >= 1")
    if sort_order not in ["asc", "desc"]:
        raise ValueError("sort_order must be 'asc' or 'desc'")
    
    # Convert value to lowercase string for case-insensitive search
    value = str(value).lower() if value else None

    # 1️⃣ FILTER / SEARCH
    results = []
    for item in data:
        if not isinstance(item, dict):
            continue  # Skip non-dict items
            
        if value:
            match = False
            for v in item.values():
                if value in str(v).lower():
                    match = True
                    break
            if match:
                results.append(item)
        else:
            results.append(item)

    # 2️⃣ SORTING
    if sort_by:
        try:
            # Sort with None values at the end
            results.sort(
                key=lambda x: (x.get(sort_by) is None, x.get(sort_by)),
                reverse=(sort_order == "desc")
            )
        except TypeError:
            # Handle mixed types by converting to string
            results.sort(
                key=lambda x: str(x.get(sort_by, "")),
                reverse=(sort_order == "desc")
            )

    # 3️⃣ PAGINATION
    start = (page - 1) * limit
    end = start + limit
    paginated = results[start:end]

    return {
        "total": len(results),
        "page": page,
        "limit": limit,
        "data": paginated
    }
