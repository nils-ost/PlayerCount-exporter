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
