from sqlalchemy import Column, Integer, String, Table, ForeignKey, Float
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:kpy680126@localhost:3306/CctvProject')
Sessoion = sessionmaker(bind=engine)
Base = declarative_base()


citys_cctvs_association = Table(
    'citys_cctvs', Base.metadata,
    Column('cctv_id', Integer, ForeignKey('cctv.id')),
    Column('city_id', Integer, ForeignKey('city.id'))

)


cityholls_cctvs_association = Table(
    'cityholls_cctvs', Base.metadata,
    Column('cctv_id', Integer, ForeignKey('cctv.id')),
    Column('cityholl_id', Integer, ForeignKey('cityholl.id'))

)

purpose_cctvs_association = Table(
    'purpose_cctvs', Base.metadata,
    Column('cctv_id', Integer, ForeignKey('cctv.id')),
    Column('purpose_id', Integer, ForeignKey('purpose.id'))

)

numbers_cctvs_association = Table(
    'numbers_cctvs', Base.metadata,
    Column('cctv_id', Integer, ForeignKey('cctv.id')),
    Column('number_id', Integer, ForeignKey('phone_number.id'))

)


class Cctv(Base):
    __tablename__ = 'cctv'

    id = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey('city.id'))
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


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    city_name = Column(String(100))
    cctvs = relationship("Cctv", secondary=citys_cctvs_association)

    def __init__(self, city_name):
        self.city_name = city_name


class Cityholl(Base):
    __tablename__ = 'cityholl'

    id = Column(Integer, primary_key=True)
    cityholl_name = Column(String(100))
    cctvs = relationship("Cctv", secondary=cityholls_cctvs_association)

    def __init__(self, cityholl_name):
        self.cityholl_name = cityholl_name


class Purpose(Base):
    __tablename__ = 'purpose'

    id = Column(Integer, primary_key=True)
    set_purpose = Column(String(100))
    cctvs = relationship("Cctv", secondary=purpose_cctvs_association)

    def __init__(self, set_purpose):
        self.set_purpose = set_purpose


class PhoneNumber(Base):
    __tablename__ = 'phone_number'

    id = Column(Integer, primary_key=True)
    number = Column(String(100))
    cctvs = relationship("Cctv", secondary=numbers_cctvs_association)

    def __init__(self, number):
        self.number = number
