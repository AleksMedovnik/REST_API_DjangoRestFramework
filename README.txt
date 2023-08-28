USER

Registration
POST:
http://127.0.0.1:8000/users/auth/users/
{
    "username": "Ritchie",
    "email": "blackmore@gmail.com",
    "password": "jkjsdkjhjkhueihfslah3159",
    "first_name": "Ritchie",
    "last_name": "Blackmore",
    "phone_number": "+79593112751",
    "date_birth": "1945-04-14",
    "country": "England",
    "city": "Weston-super-Mare",
    "district": "Somerset"
}

###########################################

Login in Browser
# GET:
http://127.0.0.1:8000/users/api-auth/login/


Logout in Browser
# GET:
http://127.0.0.1:8000/users/api-auth/logout/


# Get token
POST:
http://127.0.0.1:8000/users/auth/token/login/
{
    "password": "jkjsdkjhjkhueihfslah3159",
    "username": "Ritchie"
}

# Output:
{
    "auth_token": "80a6c591b8661fd1a712d1bd99e74265368298d8"
}

# Logout token
POST:
http://127.0.0.1:8000/users/auth/token/logout/

######################################

PRODUCT

POST:
http://127.0.0.1:8000/products/

Body:
{
    "title": "HONOR 70",
    "info": "Смартфон HONOR 70 5G 12/512 ГБ CN, Dual nano SIM",
    "price": 37799.0,
    "screen_diagonal": 6.67,
    "battery_capacity": 4800,
    "resolution_main_camera": 54.0,
    "maker": 4,
    "os": 1,
    "color": 6,
    "ram": 9
}


PUT:
http://127.0.0.1:8000/products/1/

Body:
{
    "title": "HONOR 70",
    "info": "Смартфон HONOR 70 5G 12/512 ГБ CN, Dual nano SIM",
    "price": 37799.0,
    "screen_diagonal": 6.67,
    "battery_capacity": 4800,
    "resolution_main_camera": 54.0,
    "maker": 4,
    "os": 1,
    "color": 5,
    "ram": 6
}


PATCH:
http://127.0.0.1:8000/products/1/

Body:
{
    "resolution_main_camera": 54.0
}


DELETE:
http://127.0.0.1:8000/products/1/


GET:
http://127.0.0.1:8000/products/

http://127.0.0.1:8000/products/1/

http://127.0.0.1:8000/products?pk=1

http://127.0.0.1:8000/products?id=1

http://127.0.0.1:8000/products?title=Xiaomi POCO M5s

http://127.0.0.1:8000/products?title_like=xiaomi

http://127.0.0.1:8000/products?info=xiaomi

http://127.0.0.1:8000/products?title=Apple iPhone 11&color=3

http://127.0.0.1:8000/products?price_min=20000.0

http://127.0.0.1:8000/products?price_min=20000.0&price_max=50000.0

http://127.0.0.1:8000/products?screen_diagonal_min=6.6

http://127.0.0.1:8000/products?battery_capacity_max=5000

http://127.0.0.1:8000/products?resolution_main_camera_min=50

http://127.0.0.1:8000/products?_limit=3

http://127.0.0.1:8000/products?_page=2&_limit=3

http://127.0.0.1:8000/products?_sort=-price

http://127.0.0.1:8000/products?title_ne=Realme 11 Pro


######################################

ORDER