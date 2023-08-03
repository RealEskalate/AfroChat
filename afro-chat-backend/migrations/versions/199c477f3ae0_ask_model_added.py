"""Ask Model Added

Revision ID: 199c477f3ae0
Revises: 1e8e9e1f2a15
Create Date: 2023-08-03 07:38:39.235037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '199c477f3ae0'
down_revision = '1e8e9e1f2a15'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'telegram_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('user', 'telegram_id',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###