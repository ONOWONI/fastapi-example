"""f39a54146420

Revision ID: f39a54146420
Revises: 8a7ddabf1468
Create Date: 2022-05-08 18:02:49.423383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f39a54146420'
down_revision = '8a7ddabf1468'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('Title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
