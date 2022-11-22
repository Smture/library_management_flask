"""Removed publication date unique

Revision ID: 7ef2df7667b3
Revises: ea47df4c6a0d
Create Date: 2022-11-14 23:10:17.223348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ef2df7667b3'
down_revision = 'ea47df4c6a0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('publication_date', table_name='books')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('publication_date', 'books', ['publication_date'], unique=False)
    # ### end Alembic commands ###
