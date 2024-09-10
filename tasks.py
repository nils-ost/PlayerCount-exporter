from invoke import task


@task(name='build-image')
def build_container_image(c):
    version = c.run('git describe')
    version = version.stdout.strip().replace('v', '', 1).rsplit('-', 1)[0].replace('-', '.')
    c.run('cd app; sudo docker build -t nilsost/playercount-exporter:latest .')
    c.run(f'sudo docker tag nilsost/playercount-exporter:latest nilsost/playercount-exporter:{version}')


@task(name='push-image')
def push_container_image(c):
    version = c.run('git describe')
    version = version.stdout.strip().replace('v', '', 1).rsplit('-', 1)[0].replace('-', '.')
    c.run(f'sudo docker push nilsost/playercount-exporter:{version}')
    c.run('sudo docker push nilsost/playercount-exporter:latest')
