WEB_ID=$(docker ps -aqf name=kestrel-cms_web);

docker exec kestrel-cms_web_1 rm -rf /app/home;
docker cp ./home $WEB_ID:/app/home;
docker exec kestrel-cms_web_1 python3 manage.py makemigrations --dry-run -v 3;
docker cp $WEB_ID:/app/home/migrations ./home;
