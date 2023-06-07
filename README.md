Пример работы (Postman):

GET http://127.0.0.1:8000/test/ -------> получаем {"login": "KtrjzUYpvk"} #получили логин к тестам<br/>    
POST http://127.0.0.1:8000/iq/ -------> передаем в form-data score:30, login:KtrjzUYpvk #отправили результаты iq-теста<br/>
POST http://127.0.0.1:8000/eq/ -------> передаем в form-data letters:абвгд, login:KtrjzUYpvk #отправили результаты eq-теста<br/>
POST http://127.0.0.1:8000/test/ -------> передаем в form-data login:KtrjzUYpvk #получили результаты по двум тестам по указанному логину<br/>
