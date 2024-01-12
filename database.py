from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database connection parameters
db_params = {
    'user': 'postgres',
    'password': 'postgres',
    'host': 'db',
    'port': '5442',
    'database': 'postgres',
}

# Create the database engine
engine = create_engine(
    f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
)

# Create a scoped session
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Create a declarative base
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Importing the model module where SQLAlchemy models are defined
    import model
    
    # Create tables based on the defined models
    Base.metadata.create_all(bind=engine)
