# docker run --rm -v mysql-app_persistence_db_app_rm:/data -v "$(pwd)/mysql-app":/backup busybox tar xzf /backup/mysql-app_persistence_db_app_rm.tar.gz -C /data
# docker run --rm -v supertoken-core-mysql-auth_persistence_db_supertoken_rm:/data -v "$(pwd)/supertoken-core-mysql-auth":/backup busybox tar xzf /backup/supertoken-core-mysql-auth_persistence_db_supertoken_rm.tar.gz -C /data
# docker run --rm -v ntfy-server_persistence_ntfy_cache_rm:/data -v "$(pwd)/ntfy-server":/backup busybox tar xzf /backup/ntfy-server_persistence_ntfy_cache_rm.tar.gz -C /data
# docker run --rm -v ntfy-server_persistence_ntfy_etc_rm:/data -v "$(pwd)/ntfy-server":/backup busybox tar xzf /backup/ntfy-server_persistence_ntfy_etc_rm.tar.gz -C /data
docker images -q alpine-zip | grep -q . || docker build -t alpine-zip -f AlpineZipDockerfile .


docker run --rm -v mysql-app_persistence_db_app_rm:/data -v "$(pwd)/mysql-app":/backup alpine-zip sh -c "cd /backup && unzip mysql-app_persistence_db_app_rm.zip -d /data"
docker run --rm -v supertoken-core-mysql-auth_persistence_db_supertoken_rm:/data -v "$(pwd)/supertoken-core-mysql-auth":/backup alpine-zip sh -c "cd /backup && unzip supertoken-core-mysql-auth_persistence_db_supertoken_rm.zip -d /data"
docker run --rm -v ntfy-server_persistence_ntfy_cache_rm:/data -v "$(pwd)/ntfy-server":/backup alpine-zip sh -c "cd /backup && unzip ntfy-server_persistence_ntfy_cache_rm.zip -d /data"
docker run --rm -v ntfy-server_persistence_ntfy_etc_rm:/data -v "$(pwd)/ntfy-server":/backup alpine-zip sh -c "cd /backup && unzip ntfy-server_persistence_ntfy_etc_rm.zip -d /data"
