todos = [
    {"title": "レポートを提出する", "completed": False, "priority": "高"},
    {"title": "教科書を返却する", "completed": True, "priority": "中"},
]


def add_todo(title, priority="中"):
    todos.apend({"title": title, "completed": False, "priority": priority})


def show_todos():
    print("TODO一覧")
    print("状態と優先度：高・中・低／[完了]は完了済み")
    print()
    print(f"すべてのTODO ({len(todos)}件)")
    for todo in todos:
        if todo["completed"]:
            print(f'- [完了] {todo["title"]} [{todo["priority"]}]')
        else:
            print(f'- {todo["title"]} [{todo["priority"]}]')


add_todo("発表資料を作る", "高")
show_todos()