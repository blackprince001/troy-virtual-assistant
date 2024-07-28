from app.core.security import get_password_hash
from app.database import SessionLocal
from app.models.user import User


def create_initial_admin():
    db = SessionLocal()
    admin_user = User(
        username="admin",
        email="admin@example.com",
        hashed_password=get_password_hash("admin_password"),
        role="admin",
        is_admin=True,
    )
    db.add(admin_user)
    db.commit()
    db.close()


if __name__ == "__main__":
    create_initial_admin()
    print("Initial admin user created.")
