<<<<<<< HEAD
#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
=======
#!/usr/bin/env python3
"""Generates a .tgz archive from the contents of the web_static folder."""
from fabric.api import *
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    local('sudo mkdir -p versions')
    t = datetime.now()
    t_str = t.strftime('%Y%m%d%H%M%S')
    local("sudo tar -cvzf versions/web_static_{}.tgz web_static".format(t_str))

    f_path = "versions/web_static_{}.tgz".format(t_str)
    f_size = os.path.getsize(f_path)
    print(f"web_static packed: {f_path} -> {f_size}Bytes")
    return f_path
>>>>>>> ab7cc64d1c864ef9e3dfa0d562199b5c2fe56186
