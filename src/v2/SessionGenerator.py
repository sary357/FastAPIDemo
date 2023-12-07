from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
class sessionGenerator:
    _instance = None 
    def __new__(cls, *args, **kwargs): 
        if cls._instance is None: 
            cls._instance = super().__new__(cls) 
        return cls._instance 
         
    def __init__(self): 
        self.engine = create_engine(self.__get_db_conn_str__(), echo=True)
        self.session = None

    def __get_db_conn_str__(self)->str:
        # TODO: please replace this part with your own database connection string
        #       ideally, you should use connection saved in crdentials store like vault
        #return 'postgresql+psycopg2://postgres:CHANGE_ME@db:5432/gogobot_log' # for docker-compose
        return 'postgresql+psycopg2://postgres:CHANGE_ME@localhost:5432/gogobot_log' # for local environment
    
    def get_session(self):
        if self.session is None:
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
        return self.session

