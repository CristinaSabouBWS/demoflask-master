"""add age to actors

Revision ID: 6cd86d0fcad4
Revises: 8ea8887d7701
Create Date: 2022-06-23 14:35:32.875232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6cd86d0fcad4"
down_revision = "8ea8887d7701"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("actors", sa.Column("birth_year", sa.Integer()))


def downgrade() -> None:
    pass
