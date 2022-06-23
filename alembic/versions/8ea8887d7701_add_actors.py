"""add actors

Revision ID: 8ea8887d7701
Revises: 0164afc2d1fa
Create Date: 2022-06-23 14:28:16.312427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8ea8887d7701"
down_revision = "0164afc2d1fa"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "actors",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("uid", sa.String(255), nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("filmography_movie_url", sa.String(255), nullable=True),
        sa.Column("filmography_movie_title", sa.String(255), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("actors")
