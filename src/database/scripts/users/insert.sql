INSERT INTO restaurant_app.users (name, surname, phone, email, address, payment) 
VALUES (%s, %s, %s, %s, %s, %s)
RETURNING id