from invoke import task


@task(name='build-image', aliases=['ib', ])
def build_container_image(c):
    version = c.run('git describe')
    version = version.stdout.strip().replace('v', '', 1).rsplit('-', 1)[0].replace('-', '.')
    c.run(f'cd app; sudo docker buildx build --platform linux/arm64,linux/amd64,linux/arm/v7 -t nilsost/playercount-exporter:{version} .')
    c.run('cd app; sudo docker buildx build --platform linux/arm64,linux/amd64,linux/arm/v7 -t nilsost/playercount-exporter:latest .')


@task(name='build-push-image', aliases=['ibp', ])
def push_container_image(c):
    version = c.run('git describe')
    version = version.stdout.strip().replace('v', '', 1).rsplit('-', 1)[0].replace('-', '.')
    c.run(f'cd app; sudo docker buildx build --platform linux/arm64,linux/amd64,linux/arm/v7 -t nilsost/playercount-exporter:{version} --push .')
    c.run('cd app; sudo docker buildx build --platform linux/arm64,linux/amd64,linux/arm/v7 -t nilsost/playercount-exporter:latest --push .')
