"""empty message

Revision ID: 011c3ffd66ab
Revises: f42aee5b8a9e
Create Date: 2021-04-28 16:39:05.430031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '011c3ffd66ab'
down_revision = 'f42aee5b8a9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=20), nullable=True),
    sa.Column('subtitle', sa.String(length=30), nullable=True),
    sa.Column('img', sa.String(length=60), nullable=True),
    sa.Column('prices', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('password', sa.String(length=30), nullable=True),
    sa.Column('contato', sa.String(length=60), nullable=True),
    sa.Column('city', sa.String(length=60), nullable=True),
    sa.Column('street', sa.String(length=60), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('units', sa.Integer(), nullable=True),
    sa.Column('date_posted', sa.DateTime(timezone=True), nullable=False),
    sa.Column('status', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('users')
    op.drop_table('products')
    # ### end Alembic commands ###
