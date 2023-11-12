from typing import Generic, TypeVar, Type, Any, Optional, List, Union, Dict

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.app.database import Base

ModelType = TypeVar(name="ModelType", bound=Base)
CreateSchemaType = TypeVar(name="CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar(name="UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):  # noqa
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, *, id_: int) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id_).first()  # noqa

    def get_all(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, income_entity: CreateSchemaType) -> ModelType:
        new_entity = self.model(**income_entity.model_dump())
        db.add(new_entity)
        db.commit()
        db.refresh(new_entity)
        return new_entity

    @staticmethod
    def update(
        db: Session,
        *,
        database_entity: ModelType,
        income_entity: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(database_entity)
        if isinstance(income_entity, dict):
            update_data = income_entity
        else:
            update_data = income_entity.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(database_entity, field, update_data[field])
        db.add(database_entity)
        db.commit()
        db.refresh(database_entity)
        return database_entity

    def remove(self, db: Session, *, id_: int) -> None:
        entity = db.query(self.model).get(id_)
        db.delete(entity)
        db.commit()
