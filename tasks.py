from invoke import task

venv_path = 'source ~/projects/modullux_venv/bin/activate'


@task
def git_pull(c):
    c.run('git pull')


@task(git_pull)
def deploy(c):
    with c.cd('current'):
        with c.prefix(venv_path):
            c.run('pip install -r requirements.txt')
            c.run('python manage.py collectstatic')
            c.run('python manage.py migrate')