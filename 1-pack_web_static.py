from fabric.api import local
from datetime import datetime

def do_pack():
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz.".format(now)
    local('mkdir -p versions')
    result = local('tar -cvzf {} web_static'.format(file_path))
    if (result.succeeded):
        return file_path