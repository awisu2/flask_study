from sqlalchemy import *
from migrate import *

meta = MetaData()

country = Table('users', meta,
                Column('id', Integer, primary_key=True),
                Column('email', String(255)),
                Column('password', String(255), nullable=False)
                )

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    country.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    country.drop()
