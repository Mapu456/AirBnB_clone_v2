#!/usr/bin/python3
"""new class"""

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (create_engine)
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage():
    """new engine"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor with atributtes to connect with db"""
        host = getenv('HBNB_MYSQL_HOST')
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_MYSQL_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, passwd, host, db),
            pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """select all objs"""
        new_dictionary = {}
        query = None
        if cls is None:
            tables_list = [State, City, User, Place, Review, Amenity]
            for table in tables_list:
                query += self.__session.query(table).all()
            for new_object in query:
                typ_obj = str(cls).split(" ")[1].split(".")[-1][:-2]
                new_dictionary[typ_obj + '.' +
                               new_object.id] = new_object
        else:
            query = self.__session.query(cls).all()
            typ_obj = str(cls).split(" ")[1].split(".")[-1][:-2]
            for new_object in query:
                new_dictionary[typ_obj + '.' + new_object.id] = new_object
        return new_dictionary

    def new(self, obj):
        """add obj to session"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """save changes in the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete objects saved in the session"""
        if obj is not None:
            self.__session.delete(obj)
        self.save()

    def reload(self):
        """reload the session"""
        from models.base_model import BaseModel, Base
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.user import User
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """close session"""
        self.__session.close()
