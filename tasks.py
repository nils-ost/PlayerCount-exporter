from invoke import task

image = 'nilsost/playercount-exporter'


@task(name='container-image-build', aliases=['cib', ])
def build_container_image(c):
    version = c.run('git describe')
    version = version.stdout.strip().replace('v', '', 1).rsplit('-', 1)[0].replace('-', '.')
    tags = f' -t {image}:{version}'
    tags += f' -t {image}:latest'
    c.run(f'cd app; sudo docker buildx build --platform linux/arm64,linux/amd64,linux/arm/v7{tags} --load .')


@task(name='container-image-push', aliases=['cip', ])
def push_container_image(c):
    version = c.run('git describe')
    version = version.stdout.strip().replace('v', '', 1).rsplit('-', 1)[0].replace('-', '.')
    tags = f' -t {image}:{version}'
    tags += f' -t {image}:latest'
    c.run(f'cd app; sudo docker buildx build --platform linux/arm64,linux/amd64,linux/arm/v7{tags} --push .')
