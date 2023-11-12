from backend.app.models import Task
from backend.app.repository.base_crud import CRUDBase
from backend.app.schemas.schemas import TaskCreate, TaskUpdate


class CRUDTask(CRUDBase[Task, TaskCreate, TaskUpdate]):
    pass


task = CRUDTask(Task)
