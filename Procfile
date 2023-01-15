release: python manage.py migrate && python nltk.download('vader_lexicon')
web: gunicorn telusko.wsgi --log-file=-
