"""add foreign key

Revision ID: 2b5a75a41f33
Revises: 2e75c8378d0b
Create Date: 2022-05-11 11:04:06.938434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b5a75a41f33'
down_revision = '2e75c8378d0b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
    sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table='posts', referent_table='users',
    local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
