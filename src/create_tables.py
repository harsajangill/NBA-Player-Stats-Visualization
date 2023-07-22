from models import Base, engine_writer

if __name__ == '__main__':
    Base.metadata.create_all(engine_writer)
