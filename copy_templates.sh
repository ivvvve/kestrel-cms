WEB_ID=$(docker ps -aqf name=kestrel-cms_web);

docker exec kestrel-cms_web_1 rm -rf /app/home/templates;
docker cp ./home/templates $WEB_ID:/app/home/templates;
docker exec kestrel-cms_web_1 rm -rf /app/home/static;
docker cp ./home/static $WEB_ID:/app/home/static;
