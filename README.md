# A BOT TELEGRAM SEND `N` IMAGES EVERY 2 HOURS 

## DEPENDENCIES
- python 3.8
- Celery
- pyTelegramBotAPI
- python-dotenv

## INSTALLATION
### Install requirements
`pip install -r requirements.txt`
or
`poetry add requirements.txt`

### Make ```.env``` file and add your configure

#### Short config:
```
#telegram
GROUP_ID=
TOKEN=

#unsplash
URL=
CLIENT_ID=
COUNT=
QUERY=
ORIENTATION=
```

``Now just run rabbitmq server => BOT is working``

#### Long Config:
```
#telegram
GROUP_ID=
TOKEN=

#unsplash
URL=
CLIENT_ID=
COUNT=
QUERY=
ORIENTATION=

#schedule
MINUTES=
HOUR=
DAY_OF_MONTH=
MONTH=
DAY_OF_WEEK=

#rabbitmq
RABBITMQ=
```

### Run rabbitmq
`sudo rabbitmq-server`

# RUN
`python3 src/main.py`
or
`poetry run python3 src/main.py` (if you use `poetry`)