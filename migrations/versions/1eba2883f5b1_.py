"""empty message

Revision ID: 1eba2883f5b1
Revises: c4e1070ac418
Create Date: 2021-04-23 19:09:01.957304

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1eba2883f5b1'
down_revision = 'c4e1070ac418'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'prices')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('prices', mysql.FLOAT(), nullable=True))
    # ### end Alembic commands ###