from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity

class UsersRepository:

    @classmethod
    def insert_user(cls, first_name:str, last_name:str, email:str, age:int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    age=age,
                )

                database.session.add(new_registry)
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc

    @classmethod
    def select_user(cls, first_name:str) -> any:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.first_name == first_name)
                        .all()
                )
                return users
            except Exception as exc:
                database.session.rollback()
                raise exc