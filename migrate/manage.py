#!/usr/bin/env python
from migrate.versioning.shell import main
import os

# db's url list
urls = {
  'dev': 'mysql+pymysql://user:password@db/mydb?charset=utf8mb4',
  'local': 'mysql+pymysql://user:password@127.0.0.1/mydb?charset=utf8mb4'
}

def get_url_runmode(runmode):
    if RUNMODE == 'prod':
        return os.getenv('DB_URL', 'dev')

    return urls[RUNMODE]

if __name__ == '__main__':
    RUNMODE = os.getenv('RUNMODE', 'dev')
    url = get_url_runmode(RUNMODE)
    main(repository='.', url=url, debug='False')
