from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./project_one.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
#SQLite only allows one thread to communicate with it and each thread will handle an independent request.
#FastAPI, using normal functions more than one thread can interact with the database for the same request,
#so we need to make SQLite know that it should allow that with connect_args={"check_same_thread": False}.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Each instance of the SessionLocal class will be a database session.
#It is called SessionLocal to distinguish it from the Session we are importing from SQLAlchemy.

Base = declarative_base()
#will inherit from this class to create each of the database models or classes
#allows SQLAlchemy to detect and map the class to a database table
