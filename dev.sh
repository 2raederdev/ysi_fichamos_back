# export DB_URL="postgres+psycopg2://postgres:ysi2019@35.195.21.243:5432/products?client_encoding=utf8";

gunicorn --bind 127.0.0.1:8080 --reload main:app