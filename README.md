# ProjectFlorianK
Project : 
Create a Docker cluster which is used to host a website. The website should have 3 components:
 
1)      Database with a simple table (PostrgreSQL, MySQL, etc)
2)      Python WSGI server (Flask, Django, etc)
3)      Proxy server (Nginx)
 
The server should have a single page that shows the output for a simple select query from the table.

Technologies chosen and specificities: 
NGINX/FLASK/GUNICORN/POSTGRE
3 containers will be created and orchestrated by docker-compose:
  -web
  -nginx
  -db
HEALTHCHECK will be performed on each container using curl and a shell for postgre.
The database is automatically created and initialize (created_db and seed_db launch in entry_point.sh file)
The front is done by index.html file. The data displayed come from the postgre database.
The database is a list of the best players in the world.



 

