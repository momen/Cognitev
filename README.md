API users tasks

## Requirements
 - You should install virtualenv first
```$pip install --user virtualenv ```

## Steps: using Virtualenv
```
    $ virtualenv env 
    $ source env/bin activate
    $ cd project/
    $ python3 manage.py makemigrations users
    $ python3 manage.py migrate
    $ python3 manage.py runserver
```

##  Endpoints

1. Task1
`http://127.0.0.1:8000/users/register/[POST]`
``` yaml
    {
        "first_name" : "aaa",
        "last_name" : "aaa",
        "email" : "aaaaa@example.com",
        "country_code" : "EG",
        "phone_number" : "+201002188310",
        "gender" : "male",
        "birthdate" : "1984-10-1",
        "password" : "12345"
    }
```
2. Task2
`http://127.0.0.1:8000/users/token/[POST]`
``` yaml
    {"phone_number": "+201001234589",
    "password": "12345"
    }
```
3. Task3
`http://127.0.0.1:8000/users/user_from_token/[POST]`
``` yaml
    {"token": "c2de07eda5346c2e50eae816de775d4a7a5f58da",
    "phone_number": "+201001234589"
}
```
