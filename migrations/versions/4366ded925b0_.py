"""empty message

Revision ID: 4366ded925b0
Revises: None
Create Date: 2014-09-15 07:41:58.979280

"""

# revision identifiers, used by Alembic.
revision = '4366ded925b0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('health_goal', sa.Column('id', sa.Integer, primary_key=True))
    op.add_column('health_weight', sa.Column('id', sa.Integer, primary_key=True))
    op.add_column('health_calories', sa.Column('id', sa.Integer, primary_key=True))
    pass


def downgrade():
    pass
