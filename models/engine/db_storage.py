#!/usr/bin/python3
""" SQLAlchemy class """

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review

class DBStorage:
    """ Tables creation in env"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dict """
        dictiory = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for e in query:
                key = "{}.{}".format(type(e).__name__, elem.id)
                dictiory[key] = e
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for c in lista:
                query = self.__session.query(c)
                for e in query:
                    key = "{}.{}".format(type(e).__name__, e.id)
                dictiory[key] = e
        return (dictiory)

    def new(self, obj):
        """ new element in the table """
        self.__session.add(obj)

    def save(self):
        """the change save """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """ isolotion"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ function remove()"""
        self.__session.close()
