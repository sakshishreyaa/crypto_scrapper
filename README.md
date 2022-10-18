# crypto_scrapper
steps to deploy locally

create virtual env and install requirements.txt
run the following commands
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

endpoints :
To get data in table format
  http://localhost:8000/get_coin_marketcap/

To update data in postgres database
  http://localhost:8000/update_coin_marketcap/
