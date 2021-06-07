# Image Hosting - простейший сервис хранения картинок

Cтраницы:

1. Главная страница "/". На главной странице отображены загруженные картинки. 
У каждой загруженной картинки отображается её заголовок, а так же дата и время её загрузки.
Также, для каждой картинки есть возможность её удаления.

2. Страница загрузки новой картинки "/upload/". На этой станице:
- форма загрузки картинки, которая содержит:
  - текстовое поле для ввода заголовка картинки.
  - поле для выбора файла.
  - кнопка "Загрузить". После загрузки картинки происходит редирект на главную страницу. 

Структура проекта:
- /imghost - пакет конфигурации
- /picture - основное приложение
- requirements.txt - список внешних зависимостей
