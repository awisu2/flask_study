#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='.', url='mysql+pymysql://user:password@127.0.0.1/mydb?charset=utf8mb4', debug='False')
