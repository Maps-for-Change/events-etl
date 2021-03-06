# Events ETL (a map-for-change racket)

Start of ETL for all events for progressive applications.

# Norms

* Please use GitFlow if possible, and send PR to `develop` **not `master`**

# Setting up Local Heroku
The following is based on the [Heroku Python Getting Started Guide](https://devcenter.heroku.com/articles/getting-started-with-python#run-the-app-locally)

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

# Setting Up ETL

## Environment Variables

| key | description |
|--- |--- |
| `AWS_ACCESS_KEY_ID` | Access Key for S3 bucket |
| `AWS_SECRET_ACCESS_KEY` | Secret AccessKey for Indivisible bucket |
| `AWS_HOST` | AWS Host for S3 |
| `S3_BUCKET` | Name of the bucket we're going to put the data in |
| `CLOUDFRONT_ID` | Cloudfront instance dedicated to the S3 instance |


# Usage per CRM

## NationBuilder

```
scraper = nb.EventsScraper("https://website.nationbuilder.com", \
              access_token="access_token", \
              calendar_id=1, \ #optional
              slug="slug",
              event_types={"Phonebank": "phonebank"},
              supergroup="SuperGroup") 

```

| key | description |
|--- |--- |
| `access_token` | Token used for NationBuilder apps |
| `calendar_id` | Optional. Id for target campaign |
| `slug` | Slug for the website |
| `event_types` | `Dict`. Optional. Key is the substring to search for in the intro and title, while the value is the event type it will be imbibed with. Since Nationbuilder doesn't have event types|
| `supergroup` | "Group name associated with the event" |


## BlueStateDigital

```
# source_url = "http://go.website.com/page/event/search_results"
# scraper = bsd.EventsScraper(source_url, supergroup="SuperGroup")
```
