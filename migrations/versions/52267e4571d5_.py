"""empty message

Revision ID: 52267e4571d5
Revises: 0612ef01decf
Create Date: 2020-04-07 16:35:11.107832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52267e4571d5'
down_revision = '0612ef01decf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('contacts', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'contacts')
    # ### end Alembic commands ###
