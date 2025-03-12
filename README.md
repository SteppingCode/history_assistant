# History assistant

> History assistant it is a Django application that helps people to study history of
> WW2 (World War 2) and history of [PJSC Tatneft](https://www.tatneft.ru/)

My project uses AI to make it more efficient to study history,
if there is no something about any event in history, it will help you to discover this topic!

First of all you need to make `.env` file and write into it your specific data
like `SECRET_KEY` and `DEBUG`. Django uses this data to run project.

To run my project you need run following commands.

```bash
pip install -r requirements.txt
```

To use database in Django you need to "make migration".

```bash
python manage.py makemigrations
python manage.py migrate
```

If you set `DEBUG` to `False` or `0` in env file, you need to open terminal with
activated virtual enviroment and write following command.

```bash
python manage.py collectstatic
```

And then you can run project by this command

```bash
python manage.py runserver
```

## Happy usage!