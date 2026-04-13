try: from app.database.connections import connect
except: from connections import connect

from psycopg2.extensions import cursor
import random
import os


@connect()
def filler(cur: cursor, generate=False) -> None:
    dir = f'{os.getcwd()}/app/database/scripts'
    with open(f'{dir}/init.sql', 'r') as f:
        cur.execute(f.read())

    try:
        with open(f'{dir}/insert.sql', 'r') as f:
            cur.execute(f.read())
    except:
        pass
    
    if generate == True:
        # try:
        generate_orders(100)    
        # except:
            # print("""oreder duplicate's detected, exception worked""")

    print("database generated succesfully!!")


@connect(debug=True)
def generate_orders(cur: cursor, amount: int) -> None:
    alphabet = list('АБВГДЕЁЖЗОПРСТ')
    
    cur.execute('''SELECT MAX(r.id) FROM restaurant_app.restaurants r;''')
    max_r_id = cur.fetchone()[0]
    
    for i in range(amount):
        order_id = random.randint(1000, 9999)
        terminal_id = random.choice(alphabet)
        restaurant_id = random.randint(1, max_r_id)
        items = []
        to_go = random.choice([True, False])



        cur.execute(""" SELECT item FROM restaurant_app.restaurant_menu rm
                        WHERE rm.restaurant_id = %s      
                    """, (random.randint(1, max_r_id),))

        current_items = cur.fetchall()
        current_items = [item[0] for item in current_items]

        for q in range(random.randint(1,5)):
            items.append(random.choice(current_items))
        
        cur.execute(''' INSERT INTO restaurant_app.orders 
                        (restaurant_id, order_id, terminal_number, items, to_go)
                        VALUES (%s, %s, %s, %s, %s)
                    ''', (restaurant_id, order_id, terminal_id, items, to_go))



if __name__ == "__main__":
    filler(generate=True)