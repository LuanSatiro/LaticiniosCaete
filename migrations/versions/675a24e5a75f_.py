"""empty message

Revision ID: 675a24e5a75f
Revises: 09265c09bacc
Create Date: 2020-11-20 23:24:40.753117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '675a24e5a75f'
down_revision = '09265c09bacc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('useradm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('password', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('languages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('image', sa.String(length=40), nullable=True),
    sa.Column('key', sa.String(length=20), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['useradm.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('key')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=True),
    sa.Column('subtitle', sa.String(length=30), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('key', sa.String(length=20), nullable=True),
    sa.Column('exercise', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('languageKey', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['languageKey'], ['languages.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['useradm.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('languages')
    op.drop_table('useradm')
    # ### end Alembic commands ###
