from sqlalchemy.orm import Session

from db.models import User
from repository.repository import CRUDBase
from user.schemas import UserDB


class CRUDUser(CRUDBase[User, UserDB, UserDB]):

    def get_by_email(self, db: Session, email: str):
        return db.query(self.model).filter(self.model.email == email).first()


crud_users = CRUDUser(User)