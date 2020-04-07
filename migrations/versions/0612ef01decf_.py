"""empty message

Revision ID: 0612ef01decf
Revises: 
Create Date: 2020-04-07 16:26:22.958407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0612ef01decf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('likes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'likes')
    # ### end Alembic commands ###