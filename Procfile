release: python manage.py migrate
web: gunicorn telusko.wsgi --log-file=- && python -m nltk.downloader vader_lexicon
