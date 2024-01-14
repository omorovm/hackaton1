## Для начала работы с программой необходимо выполнить в терминале следующие действия

> [!IMPORTANT]
> У вас должен быть установлен **Python** и **Visual Studio Code**.


- [ ] Необходимо скопировать файлы с **Github**.

```
cd Desktop/
git clone {ssh ссылка репозитория}

```

- [ ] Установка Redis

```
cd 
sudo apt-get update
sudo apt-get install redis-server
```

- [ ] Создать и активировать виртуальное окружение.

```
cd {название папки}
python3 venv venv
. venv/bin/activate
```

- [ ] Установить необходимые библиотеки.

```
pip install -r requirements.txt
```

- [ ] Открыть Visual Studio Code

```
code .
```

## Далее необходимо изменить базовые настройки

Открываем файл ```env.txt``` и прописываем свои значения вместо многоточий. Для добаления ```EMAIL_HOST_USER``` и ```EMAIL_HOST_PASSWORD``` посмотрите инструкцию по [ссылке](https://www.youtube.com/watch?v=PC0S1dkRNtg). Сохраняем и переименовываем файл на ```.env```.

## Приступаем к работе с приложением

Открываем 2 терминала в Visual Studio Code. 

>запуск Celery в первом терминале

```
celery -A config worker -l info
```

>запуск локального сервера во втором терминале

```
./manage.py runserver
```

> [!NOTE]
> Для полной информации о запросах перейдите по [ссылке](http://localhost:8000/swagger/).