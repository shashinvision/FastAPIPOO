from app.repository import user_repository


class UserService:
    def get_users(self):
        return user_repository.get_all_users()

    def get_user_by_id(self, user_id: int):
        return user_repository.get_user_by_id(user_id)

    def create_user(self, username: str, email: str):
        return user_repository.create_user(username, email)
