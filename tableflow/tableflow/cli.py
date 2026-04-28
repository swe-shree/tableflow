import typer

app = typer.Typer()

# dummy data (replace with DB later)
DATA = [
    {"id": 1, "name": "ram", "department": "IT"},
    {"id": 2, "name": "john", "department": "HR"},
    {"id": 3, "name": "raj", "department": "IT"},
]

@app.command()
def search(name: str = "", department: str = "", sort: str = "", page: int = 1):
    result = DATA

    if name:
        result = [r for r in result if name.lower() in r["name"].lower()]

    if department:
        result = [r for r in result if department.lower() in r["department"].lower()]

    if sort:
        reverse = sort.startswith("-")
        key = sort.lstrip("-")
        result = sorted(result, key=lambda x: x.get(key), reverse=reverse)

    start = (page - 1) * 10
    end = start + 10

    print(result[start:end])

if __name__ == "__main__":
    app()