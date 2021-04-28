"""empty message

Revision ID: b4dfe8d323e7
Revises: b42ab9aa2554
Create Date: 2020-11-02 19:23:17.625495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4dfe8d323e7'
down_revision = 'b42ab9aa2554'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('posts_ibfk_1', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'languages', ['languageKey'], ['key'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('posts_ibfk_1', 'posts', 'languages', ['languageKey'], ['key'])
    # ### end Alembic commands ###