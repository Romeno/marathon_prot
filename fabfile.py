from fabric import task
import server_keys


@task(hosts=[{
    "host": server_keys.HOST,
    "user": server_keys.USER_NAME,
    "connect_kwargs": {
        "password": server_keys.PASSWORD
    }
}])
def deploy(c):
    # change directory to project dir
    with c.cd(server_keys.APP_DIR):
        # pull changes from git
        c.run("git pull")

        # activate virtual env
        with c.prefix("source " + server_keys.VIRTUALENV):
            # install/upgrade new packages if any
            c.run(server_keys.PIP + " install -r ./requirements.txt")

            # collect static files
            c.run(server_keys.PYTHON + " ./manage.py collectstatic --noinput")

            # migrate DB if any there are any changes
            c.run(server_keys.PYTHON + " ./manage.py migrate")

            # restart uwsgi
            c.run(server_keys.RESTART_UWSGI)

            # # restart nginx
            # c.run(server_keys.RESTART_NGINX_CMD)

