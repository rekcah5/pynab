"""change segment/part sequences/ids to bigint so we don't run out

Revision ID: 49dd0ca86e1
Revises: 19d4d950784
Create Date: 2014-09-25 11:46:10.636654

"""

# revision identifiers, used by Alembic.
revision = '49dd0ca86e1'
down_revision = '19d4d950784'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column(table_name='segments', column_name='id', type_=sa.types.BigInteger)
    op.alter_column(table_name='segments', column_name='part_id', type_=sa.types.BigInteger)
    op.alter_column(table_name='parts', column_name='id', type_=sa.types.BigInteger)


def downgrade():
    op.alter_column(table_name='segments', column_name='id', type_=sa.types.Integer)
    op.alter_column(table_name='segments', column_name='part_id', type_=sa.types.Integer)
    op.alter_column(table_name='parts', column_name='id', type_=sa.types.Integer)
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
