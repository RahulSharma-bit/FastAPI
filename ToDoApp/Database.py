from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'  #for SQLITE3 DB
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost/TodoApplicationDatabase' #for postgres
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:password@127.0.0.1:3306/todoapplicationdatabase'

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}) #For SQLITE 3 DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #for postgres and mysql both

Base = declarative_base()


