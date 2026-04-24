UPDATE restaurant_app.users 
SET name = %s, surname = %s, phone = %s, email = %s, address = %s, payment = %s
WHERE id = %s