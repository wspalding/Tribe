"""empty message

Revision ID: 12b36a3c7841
Revises: a4dfa057e0d4
Create Date: 2020-12-09 22:39:14.385958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12b36a3c7841'
down_revision = 'a4dfa057e0d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'tribe', ['Id'])
    op.create_unique_constraint(None, 'user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'tribe', type_='unique')
    # ### end Alembic commands ###
