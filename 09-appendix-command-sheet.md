# 09. Appendix — Command Sheet

```bash
bench new-app <app_name>
bench --site <site> install-app <app_name>
bench --site <site> migrate
bench start
bench restart

bench drop-site <sitename>
bench drop-site <sitename> --no-backup

bench export-fixtures
bench set-config -g server_script_enabled 1

docker compose -p pwd -f docker-compose.yml up
docker compose -p pwd -f docker-compose.yml down
sudo docker stop $(sudo docker ps -q)
docker start $(docker ps -a -q)
sudo docker system prune --all --force --volumes
```
