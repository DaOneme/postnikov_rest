from app.database.connections import connect
from psycopg2.extensions import cursor
import random
import os


@connect()
def filler(cur: cursor) -> None:
    dir = f'{os.getcwd()}/app/database/scripts'
    with open(f'{dir}/init.sql', 'r') as f:
        cur.execute(f.read())

    try:
        with open(f'{dir}/insert.sql', 'r') as f:
            cur.execute(f.read())
    except:
        pass
    
    try:
        generate_orders(100)    
    except:
        print("""oreder duplicate's detected, exception worked""")


@connect(debug=True)
def generate_orders(cur: cursor, amount: int) -> None:
    alphabet = list('АБВГДЕЁЖЗОПРСТ')
    
    cur.execute('''SELECT MAX(r.id) FROM restaurant_app.restaurants r;''')
    max_r_id = cur.fetchone()[0]
    
    for i in range(amount):
        order_id = random.randint(1000, 9999)
        terminal_id = random.choice(alphabet)
        restaurant_id = random.randint(1, max_r_id)
        items = ['item']
        to_go = random.choice([True, False])
        
        cur.execute(''' INSERT INTO restaurant_app.orders 
                        (restaurant_id, order_id, terminal_number, items, to_go)
                        VALUES (%s, %s, %s, %s, %s)
                    ''', (restaurant_id, order_id, terminal_id, items, to_go))



if __name__ == "__main__":
    filler()