https://github.com/nodesource/distributions
(
    sudo apt update
sudo apt install -y curl
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
)
install postgressql for linux (https://www.postgresql.org/download/linux/ubuntu/)
[
sudo sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
install sudo apt  install postgresql,postgis 
]

create database[
    https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-22-04
]
details [
postgres=# CREATE DATABASE ######;
CREATE DATABASE                                                ^
postgres=# ALTER ROLE postgres WITH PASSWORD '#######';
ALTER ROLE
postgres=# GRANT CONNECT ON DATABASE maseno TO postgres;
GRANT
postgres=# \c maseno
You are now connected to database "maseno" as user "postgres".
maseno=# CREATE EXTENSION postgis;
CREATE EXTENSION
maseno=# CREATE EXTENSION postgis_topology;
CREATE EXTENSION
maseno=# \q

]
then you use ogrinspect to generate your layer mapping and models[

    python manage.py ogrinspect --geom-name geom --srid 4326 --mapping "myproject/Data/Data.gpkg" MyModel
]
create git ignore file using [ npx gitignore python] only when you have installed nodejs
