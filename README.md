# Дипломная работа по курсу DJ-12 "Интернет-магазин"

## Задание

Перед Вами проект сайта абстрактного продуктового интернет-магазина "Четвёрочка".

* Проект написан на Django версии 2.2.16

* Дамп базы данных осуществлён в файл 'fixtures.json'.

* Изображения загружены в проект и распологаются в каталоге '/media/'.




## Документация по проекту

#####Для запуска проекта необходимо:

Установить зависимости:
```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py migrate
```

* Команда для загрузки данных из JSON файла
```bash
python manage.py loaddata fixtures.json
```

* Команда для запуска приложения
```bash
python manage.py runserver
```

