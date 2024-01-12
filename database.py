from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = 'postgres'
pwd = 'postgres'
db = 'postgres'
host = 'db'
port = '5432'
engine = create_engine('postgresql://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)) 

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    
    import model
    Base.metadata.create_all(bind=engine)