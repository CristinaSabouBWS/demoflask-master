"""create actor table

Revision ID: 88f978842782
Revises: 6efc0f616392
Create Date: 2022-06-24 09:11:28.431584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "88f978842782"
down_revision = "6efc0f616392"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "actors",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False, unique=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("uid", sa.String(10), nullable=False),
        sa.Column("filmography_movie_url", sa.String(500)),
        sa.Column("filmography_movie_title", sa.String(500)),
    )


def downgrade() -> None:
    pass
