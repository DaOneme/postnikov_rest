from typing import Callable, Any
from functools import wraps
import psycopg2
from psycopg2.extensions import cursor
import os


def connect(debug: bool = False):
    """Decorator for DB connections with support for additional arguments"""
    def decorator(sql_func: Callable) -> Callable:
        @wraps(sql_func)
        def wrapper(*args, **kwargs) -> None:
            with psycopg2.connect(
                database=os.environ.get('POSTGRES_DB'),
                user=os.environ.get('POSTGRES_USER'),
                password=os.environ.get('POSTGRES_PASSWORD'),
                host='localhost',
                port='5432'
            ) as conn:
                with conn.cursor() as cur:
                    if debug:
                        print('connected succesfully')
                    
                    # Передаем курсор и все аргументы в функцию
                    result = sql_func(cur, *args, **kwargs)
                    
                    if debug:
                        print('disconnected succesfully')
                    
                    return result
        return wrapper
    return decorator

@connect
def random(cur: cursor) -> None:
    cur.execute("select * from restaurant_app.orders")
    print(cur.fetchall())
