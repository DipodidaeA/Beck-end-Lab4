# Lab1

## Локальний запуск застосунку

*НОМЕР У СПИСКУ ГРУПИ: 15*

*15 / 3 = 5 (остача 0)*

*ВАРІАНТ: 0*

1. Зробити форк репозиторії та копіювати на свій пк.
2. У powershell або bash перейти в директорію програми (там де знаходиться docker-compose.yaml)
3. Ввести команду у powershell або bash *docker-compose up --build*

   Ви побачите результат запуску застосунку
   * Running on all addresses (0.0.0.0)
   * Running on http://127.0.0.1:5003
   * Running on http://172.18.0.3:5003
   * Press CTRL+C to quit

4. Далі у powershell або bash можна виконувати такі запити (x та у це числа які потрібно вказати):

   - curl.exe -X GET http://127.0.0.1:5003/               - перевірка життя

   - curl.exe -X GET http://127.0.0.1:5003/user/x         - отримати дані про користувача за Id
   - curl.exe -X GET http://127.0.0.1:5003/users          - отримати дані про користувачів
   - curl.exe -X POST http://127.0.0.1:5003/user          - створити нового користувача та його гаманець
   - curl.exe -X DELETE http://127.0.0.1:5003/user/x      - видалити користувача за Id та його гаманець

   - curl.exe -X GET http://127.0.0.1:5003/user/pocket    - отримати дані про гаманці
   - curl.exe -X GET http://127.0.0.1:5003/user/pocket/x  - отримати дані про гаманець користувача
   - curl.exe -X GET http://127.0.0.1:5003/user/pocket/salary/x-y  - поповнити рахунок користувача(х) на певну суму(у)

   - curl.exe -X GET http://127.0.0.1:5003/category       - отримати дані про категорії
   - curl.exe -X POST http://127.0.0.1:5003/category      - створити нову категорію
   - curl.exe -X DELETE http://127.0.0.1:5003/category/x  - видалити категорію за Id

   - curl.exe -X GET http://127.0.0.1:5003/records        - отримати дані про записи
   - curl.exe -X GET http://127.0.0.1:5003/record/x       - отримати дані про запис за Id
   - curl.exe -X GET http://127.0.0.1:5003/record/x-x     - отримати дані записів з Id користувача та категорії
   - curl.exe -X POST http://127.0.0.1:5003/record/x-y    - створити новий запис для користувача(х) та категорії(у)
   - curl.exe -X DELETE http://127.0.0.1:5003/record/x    - видалити запис за Id