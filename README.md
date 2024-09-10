# PlayerCount-exporter
Grafana-Prometheus exporter to get PlayerCount of diffent GameServers

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

## Starting Exporter

The easiest way is to start one exporter on each GameServer via Docker. Just take the `docker-compose.yml` from this repo and start it with `docker compose up -d`. Now add a config like the one below to your Prometheus Server, and that's it...

## Example Prometheus Config

```
scrape_configs:
  - job_name: 'playercount'
    static_configs:
      - targets: ['192.168.0.21:8080']
        metrics_path: /bf2
        labels:
          server: 'bf2-server1'
      - targets: ['192.168.0.22:8080']
        metrics_path: /bf2
        labels:
          server: 'bf2-server2'
      - targets: ['192.168.0.23:8080']
        metrics_path: /bf2
        labels:
          server: 'bf2-server3'
      - targets: ['192.168.0.241:8080']
        metrics_path: /ut2k4
        labels:
          server: 'ut2k4-server1'
      - targets: ['192.168.0.242:8080']
        metrics_path: /ut2k4
        labels:
          server: 'ut2k4-server2'
```
