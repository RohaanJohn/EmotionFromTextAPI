release: python manage.py migrate
release: python -m nltk.downloader vader_lexicon
web: gunicorn telusko.wsgi --log-file=-
