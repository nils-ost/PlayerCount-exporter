# PlayerCount-exporter
Grafana-Prometheus exporter to get PlayerCount of different GameServers

## Starting Exporter

The easiest way is to start one exporter on each GameServer via Docker. Just take the `docker-compose.yml` from this repo and start it with `docker compose up -d`. Now add a config like the one below to your Prometheus Server, and that's it...

## Example Prometheus Config

```
scrape_configs:
  - job_name: 'pc-bf2'
    static_configs:
      - targets: ['192.168.0.21:8080']
        labels:
          server: 'bf2-server1'
      - targets: ['192.168.0.22:8080']
        labels:
          server: 'bf2-server2'
      - targets: ['192.168.0.23:8080']
        labels:
          server: 'bf2-server3'
    metrics_path: /bf2

  - job_name: 'pc-ut2k4'
      - targets: ['192.168.0.241:8080']
        labels:
          server: 'ut2k4-server1'
      - targets: ['192.168.0.242:8080']
        labels:
          server: 'ut2k4-server2'
    metrics_path: /ut2k4

  - job_name: 'pc-ut3'
      - targets: ['192.168.0.33:8080']
        labels:
          server: 'ut3-server1'
    metrics_path: /ut3

  - job_name: 'pc-mc'
      - targets: ['192.168.0.31:8080']
        labels:
          server: 'mc-server1'
      - targets: ['192.168.0.32:8080']
        labels:
          server: 'mc-server2'
    metrics_path: /mc

  - job_name: 'pc-cod2'
      - targets: ['192.168.0.41:8080']
        labels:
          server: 'cod2-server1'
    metrics_path: /cod2

  - job_name: 'pc-cod4'
      - targets: ['192.168.0.51:8080']
        labels:
          server: 'cod4-server1'
    metrics_path: /cod4
```

## Setup Dev-Environment

On your workstation check-out this repo, `cd` into it and execute the following commands:

```
sudo apt update; sudo apt install python3 virtualenv direnv
virtualenv -p /usr/bin/python3 venv
venv/bin/pip install -r requirements.txt
venv/bin/pre-commit install
sed -nr '/direnv hook bash/!p;$aeval "\$(direnv hook bash)"' -i ~/.bashrc
source ~/.bashrc
echo -e "source venv/bin/activate\nunset PS1" > .envrc
direnv allow
```

## Setup Build-Environment

If not allready created for an other project

```
sudo docker buildx create --name multi-arch --platform "linux/arm64,linux/amd64,linux/arm/v7" --driver "docker-container"
sudo docker buildx use multi-arch
sudo docker buildx inspect --bootstrap
```