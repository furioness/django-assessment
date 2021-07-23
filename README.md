# Django test assessment app
Requirements: https://www.notion.so/Python-test-assessment-by-DevelopsToday-901e35b8314d4ddc962bebf5041871d6

## Where to try
A Heroku instance (takes a while to wake up) https://floating-retreat-00950.herokuapp.com/api/

Postman workspace (by an invitational link) https://app.getpostman.com/join-team?invite_code=a86c947d48649487124a63d3b3b2012e&ws=5e09efa8-9925-493f-b0c6-bd438de54abb

## How to run locally
After `cd` to a project's folder there are 2 ways:

### Using docker-compose
Just run `docker-compose up` and check http://127.0.0.1:5000/


### Using python's venv
1) Activate the environment `source env/bin/activate` (for bash)
1) Install the requirements `pip install -r requirements.txt`   
1) Apply the migrations (to create local db.sqlite3 file) `./manage.py migrate`
1) Run the developer server `./manage.py runserver` and check http://127.0.0.1:8000/

# Additional notes
- The recurring job (scheduling) for post upvotes resetting is done via Heroku Scheduler addon that activates every 10 minutes (for effect visibility).
- Migrations on Heroku made via heroku-cmd as `./manage.py migrate` by hands
- If `DJANGO_PRODUCTION` isn't defined in environment variables, `DEBUG` sets to `True`, `SECRET_KEY` to a predefined value, database to `db.sqlite3`.
  
