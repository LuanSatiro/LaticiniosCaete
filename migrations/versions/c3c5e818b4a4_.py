"""empty message

Revision ID: c3c5e818b4a4
Revises: 92ed35dde180
Create Date: 2021-04-24 18:18:11.773196

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c3c5e818b4a4'
down_revision = '92ed35dde180'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'date_posted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('date_posted', mysql.DATETIME(), nullable=False))
    # ### end Alembic commands ###