"""empty message

Revision ID: 6efc0f616392
Revises: 
Create Date: 2022-06-08 12:58:20.680463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6efc0f616392"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "movies",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("genre", sa.String(255)),
        sa.Column("date_of_scraping", sa.String(12)),
        sa.Column("directors", sa.String(255)),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("rating", sa.Integer),
        sa.Column("release_year", sa.Integer),
        sa.Column("top_cast", sa.String(300)),
        sa.Column("url", sa.String(255), nullable=False),
        sa.Column("uid", sa.String(9), nullable=False),
        sa.Column("image_url", sa.String(250)),
        sa.Column("image_path", sa.String(250)),
    )


def downgrade() -> None:
    op.drop_table("movies")
