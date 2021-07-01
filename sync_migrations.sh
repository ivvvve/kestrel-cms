WEB_ID=$(docker ps -aqf name=kestrel-cms_web)
docker cp $WEB_ID:/app/home/ ./home
