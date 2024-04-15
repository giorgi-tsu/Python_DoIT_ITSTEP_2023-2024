from sqlalchemy import create_engine, text

engine = create_engine("mysql+mysqlconnector://root:\Mob@598592572@localhost/it_step")
connection = engine.connect()


