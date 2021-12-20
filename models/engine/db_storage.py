#!/usr/bin/python3
"""new class"""

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (create_engine)
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
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
        new_dictionary = {}
        query = None
        if cls is None:
            tables_list = [User, State, City, Amenity, Place, Review]
            for table in tables_list:
                query += self.__session.query(table).all()
            for new_object in query:
                new_dictionary[new_object.to_dict()['__class__'] + '.' +
                                    new_object.id] = new_object
        else:
            query = self.__session.query(cls).all()
            for new_object in query:
                new_dictionary[new_object.to_dict()['__class__'] + '.' +
                                    new_object.id] = new_object

    def new(self, obj):
        self.__session.add(obj)
        self.save()
    def save(self):
         self.__session.commit()
    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)
        self.save()
    def reload(self):
        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.review import Review
        from models.user import User
        Base.metadata.create_all(self.engine)
        session_factory = sessionmaker(
            bind=self.engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
