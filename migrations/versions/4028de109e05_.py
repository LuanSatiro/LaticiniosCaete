"""empty message

Revision ID: 4028de109e05
Revises: 6bca393edb2b
Create Date: 2020-11-26 16:50:50.262763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4028de109e05'
down_revision = '6bca393edb2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('languages_ibfk_1', 'languages', type_='foreignkey')
    op.create_foreign_key(None, 'languages', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'languages', type_='foreignkey')
    op.create_foreign_key('languages_ibfk_1', 'languages', 'users', ['user_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###