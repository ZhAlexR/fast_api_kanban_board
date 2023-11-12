from typing import Union, Dict, Any, Optional

from sqlalchemy.orm import Session

from backend.app.models import User
from backend.app.repository.base_crud import CRUDBase
from backend.app.schemas.schemas import UserCreate, UserUpdate
from backend.app.services.security import hash_password, verify_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(self.model).filter(self.model.email == email).first()  # noqa

    def create(self, db: Session, income_entity: UserCreate):
        hashed_password = hash_password(income_entity.password)

        user_data = income_entity.model_dump()
        user_data["password"] = hashed_password

        new_user = self.model(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def update(
        self,
        db: Session,
        *,
        database_entity: User,
        income_entity: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(income_entity, dict):
            update_data = income_entity
        else:
            update_data = income_entity.model_dump(exclude_unset=True)
        if update_data["password"]:
            update_data["password"] = hash_password(update_data["password"])
        return super().update(
            db, database_entity=database_entity, income_entity=update_data
        )

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        searched_user = self.get_by_email(db, email=email)
        if not searched_user:
            return None
        if not verify_password(password=password, hashed_password=searched_user.password):
            return None
        return searched_user


user = CRUDUser(User)
