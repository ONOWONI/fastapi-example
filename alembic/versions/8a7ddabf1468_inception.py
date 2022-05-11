"""inception

Revision ID: 8a7ddabf1468
Revises:
Create Date: 2022-05-08 17:42:41.397208

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


# revision identifiers, used by Alembic.
revision = '8a7ddabf1468'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    pass
    # op.create_table('postsd',
    # sa.Column('id', sa.Integer, primary_key=True, nullable=False),
    # sa.Column('title', sa.String, nullable=False),
    # sa.Column('content', sa.String, nullable=False),
    # sa.Column('published', sa.Boolean, server_default="True", nullable=False),
    # sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')),
    # sa.Column('owner_id',sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
    # # sa.Column('owner' , relationship("User"))
    # ),
    # op.create_table('usersd',
    # sa.Column('id', sa.Integer, primary_key=True, nullable=False),
    # sa.Column('email', sa.String, nullable=False, unique=True),
    # sa.Column('password', sa.String, nullable=False),
    # sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')),
    # ),
    # op.create_table('votesd',
    # sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True),
    # sa.Column('post_id', sa.Integer, sa.ForeignKey('posts.id', ondelete='CASCADE'), primary_key=True)
    # )


def downgrade():
    pass
    # op.drop_constraint
    # op.drop_table('postsd')
    # op.drop_table('usersd')
    # op.drop_table('votesd')
