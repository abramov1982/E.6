# E.6
Docker-compose

build app container:
  ./sudo docker build -t flask_in_docker:v0.1 .

build docker-compose
  ./docker-compose build
  
run application:
  docker-compose up
  
Для быстрой проверки кэширования можно использовать доступ к пустой страницу по порту 8081
localhost:8081 На странице генерируется случайное число, время кеширования - 10 секунд

Для кеширования используется Redis в отдельном контейнере.

Для получения числа Фибоначчи по его номеру
localhost:8081/fib/"число". Время кеширования 600 секунд.
Опытным путём заметил что заметный эффект начинается примерно от 1000000

Домашнее задание развёрнуто в Yandex Cloud по адресу: http://ilya-abramov.ru:8081/
