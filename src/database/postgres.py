import psycopg2
from psycopg2.extras import LoggingConnection

import os
import logging



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

dir = f'{os.getcwd()}/src/database/scripts'

db_connection = {"database" : os.environ.get('POSTGRES_DB'),
              "user" : os.environ.get('POSTGRES_USER'),
              "password" : os.environ.get('POSTGRES_PASSWORD'),
              "host" : 'localhost',
              "port" : '5432'
            }



def init():
    with psycopg2.connect(**db_connection, connection_factory=LoggingConnection) as conn:
        conn.initialize(logger)
        
        with conn.cursor() as cur:
            with open(f'{dir}/init.sql', 'r') as f:
                cur.execute(f.read())

            with open(f'{dir}/insert.sql', 'r') as f:
                cur.execute(f.read())




if __name__ == "__main__":
    init()