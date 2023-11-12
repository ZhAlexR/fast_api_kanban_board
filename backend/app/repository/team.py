from backend.app.models import Team
from backend.app.repository.base_crud import CRUDBase
from backend.app.schemas.schemas import TeamCreate, TeamUpdate


class CRUDTeam(CRUDBase[Team, TeamCreate, TeamUpdate]):
    pass


team = CRUDTeam(Team)
