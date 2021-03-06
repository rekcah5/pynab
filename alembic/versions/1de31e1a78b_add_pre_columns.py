"""add pre columns

Revision ID: 1de31e1a78b
Revises: 3821d174074
Create Date: 2015-01-18 19:51:20.345279

"""

# revision identifiers, used by Alembic.
revision = '1de31e1a78b'
down_revision = '91a9b24e98'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pres',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('pretime', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('searchname', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('requestid', sa.BigInteger(), nullable=True),
    sa.Column('requestgroup', sa.String(), nullable=True),
    sa.Column('filename', sa.String(), nullable=True),
    sa.Column('nuked', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('releases', sa.Column('pre_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'releases', 'pres', ['pre_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'releases', type_='foreignkey')
    op.drop_index(op.f('ix_releases_pre_id'), table_name='releases')
    op.drop_column('releases', 'pre_id')
    op.drop_index(op.f('ix_pres_name'), table_name='pres')
    op.drop_table('pres')
    ### end Alembic commands ###
