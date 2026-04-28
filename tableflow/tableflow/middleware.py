def smart_search(data, value=None, page=1, limit=10, sort_by=None, sort_order="asc"):
    value = str(value).lower() if value else None

    # 1️⃣ FILTER / SEARCH
    results = []
    for item in data:
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
        results.sort(
            key=lambda x: x.get(sort_by),
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
