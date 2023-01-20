## bkuepfer-site

Hello, my personal website and vulgar display of power. 

Powered with: 
- Python 
- Django 
- Tensorflow 
- ~~Heroku~~ Rail

### How to run

# Localy

- Install Python >= 3.6.1
- Install dependencies on `requirements.txt`. Use pip command: `pip install -r requirements.txt`.
- Run Django server with `python manage.py runserver 8000`
- Open `localhost:8000` on your browser.

# Docker 
`docker build -t bsite .`
`docker run -p 9090:8080 bsite`
