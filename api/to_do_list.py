from fastapi import APIRouter

router = APIRouter(prefix="/to-do-list")

todos=[]

@router.get("/", summary="Get tasks from the todo list")
def get_tasks():
    return {"tasks": todos }

@router.post("/", summary="Add task to todo list")
def add_tasks(task: str):
    todos.append(task)
    return {"message": f"Added : {task}", "total": len(todos)}


@router.delete("/", summary="Delete task from the todo list")
def delete_tasks(task: str):
    if task in todos:
        todos.remove(task)
        return {"message": f"Deleted: {task}"}
    return {"message": "Task not found"}
