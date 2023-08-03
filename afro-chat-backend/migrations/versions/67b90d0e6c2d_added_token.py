"""added token

Revision ID: 67b90d0e6c2d
Revises: c223436ff1af
Create Date: 2023-08-03 12:49:43.334473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67b90d0e6c2d'
down_revision = 'c223436ff1af'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ask', sa.Column('token_usage', sa.INTEGER(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ask', 'token_usage')
    # ### end Alembic commands ###