# News portal:
Website for uploading news.

### How to add more news?
- Move to the admin panel of your website (`127.0.0.1:8000`)
add `/admin` at the end of your website address.

- After login go to News;

- Then you can add new news.

After all this steps you can manage news, note that only admin can add new news.

### How to execute:

- Download or clone [repo](https://github.com/Ash2803/news_site.git)
- You must have Python 3.9 or higher already installed;
- Create the virtual environment using command:
```
python3 -m venv venv
```
- Install the requirements using command:
```
pip install -r requirements.txt
```
Create `.env` file and set environment variables:
- `SECRET KEY` - your project secret key:
- `DEBUG` = default is `False`. To enable debug mode set value to `True`;
- `MEDIA_ROOT` = you can set your path where the media files will be stored, default = `media/`;
- `MEDIA_URL` = default = `/media/`;
- `STATIC_URL` = default = `/static/`;

Then create a DB by running `makemigrations` and `migrate` command:
```
python manage.py makemigrations
python manage.py migrate
```
- Create superuser and put your login, email and password:
```
python manage.py createsuperuser
```
- Run the server:
```
python manage.py runserver
```

Read the section ["How to add more news?"](#how-to-add-more-news) to find out how to add new data to website.

### Project Goals

The project made for educational purposes.
