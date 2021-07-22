until python manage.py migrate; do
  sleep 2
  echo "Retry!";
done

gunicorn -w 1 -b 0.0.0.0:5000 news_api.wsgi --log-file -
