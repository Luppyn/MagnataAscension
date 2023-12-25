from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity

class UsersRepository:

    @classmethod
    def insert_user(cls, name:str, email:str, age:int) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    name=name,
                    email=email,
                    age=age,
                )

                database.session.add(new_registry)
                database.session.commit()
            except Exception as exc:
                database.session.rollback()
                raise exc
