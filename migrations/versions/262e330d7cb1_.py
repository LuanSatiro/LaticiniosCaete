"""empty message

Revision ID: 262e330d7cb1
Revises: 70cc3e95dc03
Create Date: 2021-04-24 15:09:40.261056

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '262e330d7cb1'
down_revision = '70cc3e95dc03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'prices')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('prices', mysql.VARCHAR(length=60), nullable=True))
    # ### end Alembic commands ###
