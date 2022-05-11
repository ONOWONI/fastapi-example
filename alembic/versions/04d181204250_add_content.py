"""add content

Revision ID: 04d181204250
Revises: f39a54146420
Create Date: 2022-05-11 10:49:13.698750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04d181204250'
down_revision = 'f39a54146420'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
    sa.Column('content', sa.String(), nullable=False))



def downgrade():
    op.drop_column('posts', 'content')
    pass
