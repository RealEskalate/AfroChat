"""changed total_token to total_toekns

Revision ID: 3e2d933fa0e9
Revises: 29ae4356a08c
Create Date: 2023-08-08 10:34:39.106978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e2d933fa0e9'
down_revision = '29ae4356a08c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conversation', sa.Column('total_tokens', sa.INTEGER(), server_default='0', nullable=False))
    op.drop_column('conversation', 'total_token')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conversation', sa.Column('total_token', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.drop_column('conversation', 'total_tokens')
    # ### end Alembic commands ###
