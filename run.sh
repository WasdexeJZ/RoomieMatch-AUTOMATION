docker compose -f ./backend/docker-compose.yaml up -d
docker compose -f ./ntfy-server/docker-compose.yaml up -d
docker compose -f ./mysql-app/docker-compose.yaml up -d
docker compose -f ./supertoken-core-mysql-auth/docker-compose.yaml up -d