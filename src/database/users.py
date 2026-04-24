from src.database.postgres import connect, read
from psycopg2.extras import RealDictCursor

from src.models.users import UserAdd


def select_all():
    conn = connect()

    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        query = read(script='select_all.sql', subdir='/users')
    
        cursor.execute(query)
        return cursor.fetchall()


def select_by_id(id):
    conn = connect()

    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        query = read(script='select_by_id.sql', subdir='/users')
    
        cursor.execute(query, (id,))
        return cursor.fetchone()
    

def insert(user: UserAdd):
    conn = connect()
    
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        query = read(script='insert.sql', subdir='/users')
    
        cursor.execute(query, (user.name,
                                user.surname,
                                user.phone,
                                user.email, 
                                user.address, 
                                user.payment))
        user_id = cursor.fetchone()


    conn.commit()
    return user_id


def delete(user_id: int) -> bool:
    '''
    returns True/False if row was/wasn't deleted\n
    '''
    
    conn = connect()
    
    with conn.cursor() as cursor:
        query = read(script='delete.sql', subdir='/users')
        
        cursor.execute(query, (user_id,))
        if cursor.rowcount == 0:
            return False
        
        conn.commit()
        return True
    

def update(user_id, user: UserAdd):
    '''
    returns True/False if row was/wasn't updated\n
    '''
    
    conn = connect()
    
    with conn.cursor() as cursor:
        query = read(script='update.sql', subdir='/users')

        cursor.execute(query, (user.name,
                                user.surname,
                                user.phone,
                                user.email, 
                                user.address, 
                                user.payment,
                                user_id))
        if cursor.rowcount == 0:
            return False
        
        conn.commit()
        return True