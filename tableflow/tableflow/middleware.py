# tableflow/middleware.py

class TableFlow:
    def __init__(self, data):
        self.data = data
        self.result = data

    # ---------------- FILTER ----------------
    def filter(self, **kwargs):
        for key, value in kwargs.items():
            self.result = [
                item for item in self.result
                if str(item.get(key, "")).lower() == str(value).lower()
            ]
        return self

    # ---------------- SORT ----------------
    def sort(self, key, reverse=False):
        self.result = sorted(self.result, key=lambda x: x.get(key), reverse=reverse)
        return self

    # ---------------- PAGINATION ----------------
    def paginate(self, page=1, limit=10):
        start = (page - 1) * limit
        end = start + limit
        self.result = self.result[start:end]
        return self

    # ---------------- OUTPUT ----------------
    def run(self):
        return self.result
