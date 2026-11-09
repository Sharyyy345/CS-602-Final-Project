from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
import enum

class JewelryType(enum.Enum):
    Ring = 1
    Necklace = 2
    Charm = 3
    Bracelet = 4
    Earrings = 5

class MetalMaterial(enum.Enum):
    SterlingSilver = 1
    Solid14KGold = 2
    PlatinumPlated = 3
    GoldPlated = 4
    TwoTone = 5

'''class CharmType(enum.Enum):
    Clip = 1
    Bead = 2
    Dangle = 3
    Safety_Chain = 4
    Spacer = 5

class EarringsType(enum.Enum):
    Hoops = 1
    Studs = 2

class NecklaceType(enum.Enum):
    Tennis = 1
    Adjustable = 2
    Link_Chain = 3
    Snake_Chain = 4

class RingType(enum.Enum):
    Stackable = 1
    Solitaire = 2
    Cocktail = 3

class CharmHolderType(enum.Enum):
    Bangle = 1
    Snake_Chain = 2

class NonCharmHolderType(enum.Enum):
    Bangle = 1
    Tennis = 2

class BraceletType(enum.Enum):
    Charm_holder = 1
    Non_Charm_holder = 2'''

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String())
    email: Mapped[str] = mapped_column(String())

class Collection(Base):
    __tablename__ = "Collections"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    user: Mapped["User"] = relationship(back_populates="collections")

    def __repr__(self) -> str:
         return f"Collection(id={self.id!r}, email_address={User.email_address!r})"

    collection_name: Mapped[str] = mapped_column(String())
    date_created: Mapped[Date] = mapped_column(Date())
    description: Mapped[str] = mapped_column(String())
    date_updated: Mapped[Date] = mapped_column(Date())

class Item(Base):
    __tablename__ = "Items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    official_name: Mapped[str] = mapped_column(String())
    representative_img_filepath: Mapped[str] = mapped_column(String())
    price: Mapped[int] = mapped_column()
    release_date: Mapped[Date] = mapped_column(Date())
    metal_material: Mapped["MetalMaterial"]

    jewelry_type: Mapped["JewelryType"]
    '''bracelet_type: Mapped[Optional["BraceletType"]]
    charm_holder_type: Mapped[Optional["CharmHolderType"]]
    non_charm_holder_type: Mapped[Optional["NonCharmHolderType"]]
    charm_type: Mapped[Optional["CharmType"]]
    earrings_type: Mapped[Optional["EarringsType"]]
    necklace_type: Mapped[Optional["NecklaceType"]]
    ring_type: Mapped[Optional["RingType"]]'''

    #brand_affiliation: Mapped[str] = mapped_column(String())

class CollectionItem(Base):
    __tablename__ = "Collection_Items"

    collection_id: Mapped[int] = mapped_column(ForeignKey("Collections.id"), primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("Items.id"), primary_key=True)
    quantity: Mapped[int] = mapped_column()
