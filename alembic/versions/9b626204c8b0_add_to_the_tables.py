"""add to the tables

Revision ID: 9b626204c8b0
Revises: 2b5a75a41f33
Create Date: 2022-05-11 11:15:09.601143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b626204c8b0'
down_revision = '2b5a75a41f33'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
    sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts',
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
