release: python manage.py migrate && python -m nltk.downloader vader_lexicon
web: gunicorn telusko.wsgi --log-file=-
