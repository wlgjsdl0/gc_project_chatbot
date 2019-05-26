from sqlalchemy import Column, Integer, Boolean, Date, String, Table, ForeignKey, Float
from sqlalchemy.orm import relationships, backref

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:kpy680126@localhost:3306/CctvProject')
Sessoion = sessionmaker(bind=engine)
Base = declarative_base()


class Cctv(Base):
    __tablename__ = 'cctv'

    id = Column(Integer, primary_key=True)
    cityholl_id = Column(Integer, ForeignKey('cityholl.id'))
    road_address = Column(String(100), nullable=True)
    address = Column(String(100), nullable=True)
    purpose_id = Column(Integer, ForeignKey('purpose.id'), nullable=True)
    num_camera = Column(Integer)
    direction = Column(String(50), nullable=True)
    days_to_keep = Column(Integer)
    phone_number_id = Column(Integer, ForeignKey('phone_number.id'))
    latitude = Column(Float)
    longitude = Column(Float)
    data_date = Column(String(50))

    def __init__(self, road_address, address, num_camera, direction, days_to_keep, latitude, longitude, data_date):
        self.road_address = road_address
        self.address = address
        self.num_camera = num_camera
        self.direction = direction
        self.days_to_keep = days_to_keep
        self.latitude = latitude
        self.longitude = longitude
        self.data_date = data_date


class Cityholl(Base):
    __tablename__ = 'cityholl'

    id = Column(Integer, primary_key=True)
    cityholl_name = Column(String(100))

    def __init__(self, cityholl_name):
        self.cityholl_name = cityholl_name


class Purpose(Base):
    __tablename__ = 'purpose'

    id = Column(Integer, primary_key=True)
    set_purpose = Column(String(100))

    def __init__(self, set_purpose):
        self.set_purpose = set_purpose


class PhoneNumber(Base):
    __tablename__ = 'phone_number'

    id = Column(Integer, primary_key=True)
    number = Column(String(100))

    def __init__(self, number):
        self.number = number
