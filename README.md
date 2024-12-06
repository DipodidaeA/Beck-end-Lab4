# Lab4

## Локальний запуск застосунку

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

   - curl.exe -X GET http://127.0.0.1:5003/user/x -H "Authorization: Bearer TOKEN"     - отримати дані про користувача за Id
   - curl.exe -X GET "http://127.0.0.1:5003/users" -H "Authorization: Bearer TOKEN"    - отримати дані про користувачів
   - curl.exe -X GET "http://127.0.0.1:5003/user/register/NAME-PASSWORD"               - створити нового користувача та його гаманець
   - curl.exe -X GET "http://127.0.0.1:5003/user/login/NAME-PASSWORD"                  - створити нового користувача та його гаманець
   - curl.exe -X DELETE http://127.0.0.1:5003/user/x -H "Authorization: Bearer TOKEN"  - видалити користувача за Id та його гаманець

   - curl.exe -X GET http://127.0.0.1:5003/user/pocket -H "Authorization: Bearer TOKEN" - отримати дані про гаманці
   - curl.exe -X GET http://127.0.0.1:5003/user/pocket/x -H "Authorization: Bearer TOKEN" - отримати дані про гаманець користувача
   - curl.exe -X GET http://127.0.0.1:5003/user/pocket/salary/x-y -H "Authorization: Bearer TOKEN" - поповнити рахунок користувача(х) на певну суму(у)

   - curl.exe -X GET http://127.0.0.1:5003/category -H "Authorization: Bearer TOKEN" - отримати дані про категорії
   - curl.exe -X POST http://127.0.0.1:5003/category -H "Authorization: Bearer TOKEN" - створити нову категорію
   - curl.exe -X DELETE http://127.0.0.1:5003/category/x -H "Authorization: Bearer TOKEN" - видалити категорію за Id

   - curl.exe -X GET http://127.0.0.1:5003/records -H "Authorization: Bearer TOKEN" - отримати дані про записи
   - curl.exe -X GET http://127.0.0.1:5003/record/x -H "Authorization: Bearer TOKEN" - отримати дані про запис за Id
   - curl.exe -X GET http://127.0.0.1:5003/record/x-x -H "Authorization: Bearer TOKEN" - отримати дані записів з Id користувача та категорії
   - curl.exe -X POST http://127.0.0.1:5003/record/x-y -H "Authorization: Bearer TOKEN" - створити новий запис для користувача(х) та категорії(у)
   - curl.exe -X DELETE http://127.0.0.1:5003/record/x -H "Authorization: Bearer TOKEN" - видалити запис за Id