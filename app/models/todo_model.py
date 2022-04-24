from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from app.database import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    is_completed = Column(Boolean, default=False)
    public_id = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Todo <{self.name}>"
