"""empty message

Revision ID: 8bea018c9006
Revises: 971384e2a14c
Create Date: 2021-04-24 18:21:45.932123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bea018c9006'
down_revision = '971384e2a14c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('date_posted', sa.DateTime(timezone=True), server_default=sa.text('now(NULL)'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'date_posted')
    # ### end Alembic commands ###
