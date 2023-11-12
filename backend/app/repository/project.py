from backend.app.models import Project
from backend.app.repository.base_crud import CRUDBase
from backend.app.schemas.schemas import ProjectCreate, ProjectUpdate


class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):
    pass


project = CRUDProject(Project)
