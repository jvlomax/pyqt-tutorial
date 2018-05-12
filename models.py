from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


engine = create_engine("sqlite:///shoppinglist.sql")
Base = declarative_base()


class List(Base):
    __tablename__ = "list"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __str__(self):
        return "{} - {}".format(self.id, self.name)


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    item_name = Column(String(255), nullable=False)
    amount = Column(Integer, default=0)
    list = relationship("List", back_populates="items")

    def __str__(self):
        return "{} - {}".format(self.id, self.item_name)


List.items = relationship("Item", order_by=Item.id, back_populates="list")