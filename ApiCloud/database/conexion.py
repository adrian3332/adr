from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:F19982428a@localhost:3306/api_estudiante")
meta = MetaData()
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()