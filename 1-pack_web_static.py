#!/usr/bin/python3
from fabric import task
from datetime import datetime
import os


@task
def do_pack(c):
    """Generates a .tgz archive from the contents of the web_static folder."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = os.path.join("versions", archive_name)
    c.local("mkdir -p versions")
    result = c.local("tar -cvzf {} web_static".format(archive_path))
    if result.failed:
        return None
    else:
        return archive_path
