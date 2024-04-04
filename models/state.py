#!/usr/bin/python3
""" State class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ Attributes:
        for the name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        v = models.storage.all()
        l = []
        res = []
        for k in v:
            city = k.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                l.append(v[k])
        for e in l:
            if (e.state_id == self.id):
                res.append(e)
        return (res)
