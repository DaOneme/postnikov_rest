from psycopg2.extensions import cursor
import matplotlib.pyplot as plt
from database.connections import connect



@connect()
def show1(cur: cursor) -> None:
    cur.execute("""
                SELECT restaurant_size from restaurant_app.restaurants r 
                ORDER BY restaurant_size ASC
                """)
    restaurant_size = cur.fetchall()
    restaurant_size = [i[0] for i in restaurant_size]

    cur.execute("""
                SELECT terminals_amount from restaurant_app.restaurants r 
                ORDER BY terminals_amount ASC
                """)
    terminals_amount = cur.fetchall()
    terminals_amount = [i[0] for i in terminals_amount]


    return restaurant_size, terminals_amount

@connect()
def show2(cur: cursor) -> None:
    cur.execute("""
                SELECT c.franchise_name, count(r.id) FROM restaurant_app.companies c
                JOIN restaurant_app.restaurants r on c.id = r.company_id 
                GROUP BY c.franchise_name 
                """)
    slayer = cur.fetchall()
    slayer = [list(i) for i in slayer]

    return slayer

@connect()
def show3(cur: cursor) -> None:
    cur.execute("""
                SELECT r.id, count(o.restaurant_id) FROM restaurant_app.orders o
                JOIN restaurant_app.restaurants r ON r.id = o.restaurant_id 
                GROUP BY r.id
                ORDER BY r.id ASC
                """)
    slayer = cur.fetchall()
    slayer = [list(i) for i in slayer]

    return slayer




def main():
    figure, axes = plt.subplots(1, 3, figsize=(15, 5))

    id = [i[0] for i in show3()]
    orders_amount = [i[1] for i in show3()]
    axes[0].bar(id, orders_amount)
    axes[0].set_title('Нагрузка на рестораны')
    axes[0].set_xlabel('ID ресторана')
    axes[0].set_ylabel('Количество заказов')

    names = [i[0] for i in show2()]
    amounts = [i[1] for i in show2()]
    axes[1].pie(amounts, labels=names, shadow=True, autopct='%1.1f%%')
    axes[1].set_title('Распределение по названиям')

    terminals, size = show1()
    axes[2].plot(terminals, size)
    axes[2].set_title("Отношение кол-ва терминалов к размеру заведения")
    axes[2].set_xlabel("Терминалы")
    axes[2].set_ylabel("Размер заведения")

    plt.tight_layout()
    plt.show()

