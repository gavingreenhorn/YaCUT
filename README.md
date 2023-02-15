# "Укоротитель ссылок YaCut"
## Автор
[Злобин Иван](https://github.com/gavingreenhorn)
## Стек
- Python 3.9
- [Scrapy](https://docs.scrapy.org/)
## Развертывание
>`git clone git@github.com:gavingreenhorn/yacut`

>`cd yacut`

>`python -m venv venv`

>`. venv/bin/activate`

>`python -m pip install -r requirements.txt`
## Запуск
>`flask run`
## Возможности
- создание коротких ссылок по адресу http://localhost:5000
- переадресация к полной ссылке при переходе по короткой
- взаимодействие с api по адресу http://localhost:5000/api/id/