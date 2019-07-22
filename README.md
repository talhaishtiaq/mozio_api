# mozio_api 
Mozio API is a Python Django  API for CRUD opertiions of providers polygon jeojsons

## Installation

Use the python and pip to install and deploy.

```bash
git clone https://github.com/talhaishtiaq/mozio_api.git
mkvirtualenv --python=/usr/bin/python3.6 mozio-venv
cd mozio_api
pip install -r requirements.txt
python manage.py runserver
```
access the django admin and api on:
http://localhost:8000/admin/
http://localhost:8000/api/v1/

## CRUD URLs

GET, POST, PUT, DELETE are available on following urls:

http://127.0.0.1:8000/api/v1/providers
http://127.0.0.1:8000/api/v1/jeojsons

## Searching
for searching a specific jeojson polygon of some latitude and longitude following url parameters can be used
lat = X
lng = Y

for example:

http://localhost:8000/api/v1/jeojsons/?lat=1009&lng=1010

this will return all the polygons that contain lat=1009 and lng=1010 in their jeojson structure


