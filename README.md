# Lab1

## Локальний запуск застосунку

1. Зробити форк репозиторії та копіювати на свій пк.
2. У powershell або bash перейти в директорію програми (там де знаходиться \_\_init\_\_.py)
3. Ввести команду flask --app \_\_init\_\_ run -h 127.0.0.1 -p 5000

   Ви побачите результат запуску застосунку
   * Running on http://127.0.0.1:5000
   * Press CTRL+C to quit

4. Далі у powershell або bash можна виконувати такі запити (x це число яке потрібно вказати):

   - curl.exe -X GET http://127.0.0.1:5000/user/x         - отримати дані про користувача за Id
   - curl.exe -X GET http://127.0.0.1:5000/users          - отримати дані про користувачів
   - curl.exe -X POST http://127.0.0.1:5000/user          - створити нового користувача
   - curl.exe -X DELETE http://127.0.0.1:5000/user/x      - видалити користувача за Id

   - curl.exe -X GET http://127.0.0.1:5000/category       - отримати дані про категорії
   - curl.exe -X POST http://127.0.0.1:5000/category      - створити нову категорію
   - curl.exe -X DELETE http://127.0.0.1:5000/category/x  - видалити категорію за Id

   - curl.exe -X GET http://127.0.0.1:5000/records        - отримати дані про записи
   - curl.exe -X GET http://127.0.0.1:5000/record/x       - отримати дані про запис за Id
   - curl.exe -X GET http://127.0.0.1:5000/record/x-x     - отримати дані записів з Id користувача та категорії
   - curl.exe -X POST http://127.0.0.1:5000/record        - створити новий запис
   - curl.exe -X DELETE http://127.0.0.1:5000/record/x    - видалити запис за Id