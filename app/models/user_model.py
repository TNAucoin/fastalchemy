from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.orm import relationship
from app.models.todo_model import Todo
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    public_id = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    todos = relationship('Todo', backref='owner', lazy='dynamic')

    def __repr__(self):
        return f"User <{self.email}>"
