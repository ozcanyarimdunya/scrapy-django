### Scrapy with django and django-channels

#### How to use;

To run scrapyd
```
$ cd {projectRoot}/scrapper/
$ scrapyd
```

To run django
```
$ cd {projectRoot}/
$ python manage.py runserver
```

#### Usage with docker

There is a small issue, currently with docker

Simply run 

```
docker-compose up -d --build
```

After this **scrapyd** will not start automatically, check [run.sh](/run.sh#L4). You need to manually start it

```
docker-compose exec web scrapyd &
```

By adding **&** at the end of command, you run it in background. Because scrapyd it took the terminal up, you need to send it to background if you want, otherwise without **&** you will see the log but after you terminate console, it will stop.
