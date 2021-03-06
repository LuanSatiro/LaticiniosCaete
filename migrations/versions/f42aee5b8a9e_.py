"""empty message

Revision ID: f42aee5b8a9e
Revises: 3b98030686fc
Create Date: 2021-04-28 16:38:18.112065

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f42aee5b8a9e'
down_revision = '3b98030686fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('key', table_name='languages')
    op.drop_table('languages')
    op.drop_table('response')
    op.drop_table('forum')
    op.drop_table('posts')
    op.drop_table('comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('content', mysql.TEXT(), nullable=True),
    sa.Column('post_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('forum_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['forum_id'], ['forum.id'], name='comments_ibfk_2'),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='comments_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('posts',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('subtitle', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('text', mysql.TEXT(), nullable=True),
    sa.Column('key', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('exercise', mysql.TEXT(), nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('languageKey', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('img1', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('img2', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('img3', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('text2', mysql.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['languageKey'], ['languages.key'], name='posts_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='posts_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('forum',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('response',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('content', mysql.TEXT(), nullable=True),
    sa.Column('comments_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['comments_id'], ['comments.id'], name='response_ibfk_1', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('languages',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=120), nullable=True),
    sa.Column('image', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('key', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='languages_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('key', 'languages', ['key'], unique=True)
    # ### end Alembic commands ###
