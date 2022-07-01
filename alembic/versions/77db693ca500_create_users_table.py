"""create users table

Revision ID: 77db693ca500
Revises: 88f978842782
Create Date: 2022-06-27 10:38:40.036356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "77db693ca500"
down_revision = "88f978842782"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False, unique=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("email", sa.String(200), nullable=False, unique=True),
        sa.Column("password", sa.String(200), nullable=False),
    )


def downgrade() -> None:
    pass
