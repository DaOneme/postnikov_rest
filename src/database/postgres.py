import psycopg2
import os

# для ювикорна, иначе он не видит енв
from dotenv import load_dotenv
load_dotenv()



DIR = f'{os.getcwd()}/src/database/scripts'

db_connection = {"database" : os.environ.get('POSTGRES_DB'),
              "user" : os.environ.get('POSTGRES_USER'),
              "password" : os.environ.get('POSTGRES_PASSWORD'),
              "host" : 'postgres',
              "port" : '5432'
            }



def connect():
    conn_params = db_connection    
    return psycopg2.connect(**conn_params)

def read(script: str, dir: str = DIR, subdir: str = '') -> str:
    '''
    func return's .sql script from src/database/scripts folder\n
    for script you must enter "file_name.sql"\n
    for dir you must enter root dir. Usuall DIR will lead from /root to the main DB dir of project\n
    for subdir you must enter the dir between ../scripts and file_name.sql. This made for dir specification 
    '''
    
    with open(f'{dir}{subdir}/{script}', 'r') as f:
        return f.read()



def init():
    conn = connect()
    
    with conn.cursor() as cur:
        cur.execute(read('init.sql'))
        print("DB inited succesfull ")

        try:
            cur.execute(read('insert.sql'))
            print("DB insert succesfull")
            
        except:
            print("DB insert error, probably duplicated data")



if __name__ == "__main__":
    init()