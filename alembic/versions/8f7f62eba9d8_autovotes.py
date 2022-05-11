"""autovotes

Revision ID: 8f7f62eba9d8
Revises: 9b626204c8b0
Create Date: 2022-05-11 11:46:15.369986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f7f62eba9d8'
down_revision = '9b626204c8b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.add_column('posts', sa.Column('title', sa.String(), nullable=False))
    op.drop_column('posts', 'Title')
    op.add_column('users', sa.Column('password', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.add_column('posts', sa.Column('Title', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('posts', 'title')
    op.drop_table('votes')
    # ### end Alembic commands ###