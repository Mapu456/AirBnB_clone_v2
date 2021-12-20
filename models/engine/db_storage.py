#!/usr/bin/python3
"""new class"""

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import (create_engine)
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
