"""empty message

Revision ID: 8af6879e92b4
Revises: d68bbfa6f410
Create Date: 2020-12-31 17:45:16.764981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8af6879e92b4'
down_revision = 'd68bbfa6f410'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Tribe', ['id'])
    op.create_unique_constraint(None, 'User', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User', type_='unique')
    op.drop_constraint(None, 'Tribe', type_='unique')
    # ### end Alembic commands ###
