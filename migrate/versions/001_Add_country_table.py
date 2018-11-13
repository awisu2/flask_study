from sqlalchemy import *
from migrate import *

meta = MetaData()

country = Table('country', meta,
                Column('id', Integer, primary_key=True),
                Column('country_name', String(32))
                )

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    country.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    country.drop()