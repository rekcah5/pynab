"""change uniques to sha1 keys

Revision ID: 41996f6d756
Revises: 54672c4d904
Create Date: 2015-03-27 21:22:02.796920

"""

# revision identifiers, used by Alembic.
revision = '41996f6d756'
down_revision = '54672c4d904'

from alembic import op
import sqlalchemy as sa
from pynab.db import Release, windowed_query
import hashlib
from sqlalchemy.orm import sessionmaker

def upgrade():
    # drop duplicate pres
    conn = op.get_bind()

    conn.execute('''
        delete from pres
        where id not in
        (
            select min(id)
            from pres
            group by requestid, pretime, requestgroup
        )
    ''')

    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('pres_name_key', 'pres', type_='unique')
    op.create_unique_constraint('pres_uniq', 'pres', ['requestid', 'pretime', 'requestgroup'])
    op.add_column('releases', sa.Column('uniqhash', sa.String(length=40), nullable=True))
    op.drop_constraint('releases_name_group_id_posted_key', 'releases', type_='unique')
    op.create_unique_constraint('releases_uniq', 'releases', ['uniqhash'])

    session = sessionmaker(bind=conn)()
    # update the hashes
    q = session.query(Release.id, Release.name, Release.group_id, Release.posted)
    for release in windowed_query(q, Release.id, 1000):
        release.uniqhash = hashlib.sha1(
            '{}.{}.{}'.format(
                release.name,
                release.group_id,
                release.posted,
            ).encode('utf-8')).hexdigest()

    session.commit()
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('releases_uniq', 'releases', type_='unique')
    op.create_unique_constraint('releases_name_group_id_posted_key', 'releases', ['name', 'group_id', 'posted'])
    op.drop_column('releases', 'uniqhash')
    op.drop_constraint('pres_uniq', 'pres', type_='unique')
    op.create_unique_constraint('pres_name_key', 'pres', ['name'])
    ### end Alembic commands ###
