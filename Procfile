release: python manage.py migrate
web: gunicorn telusko.wsgi --log-file=-
web: python nltk.downloader vader_lexicon
