"""first migrations

Revision ID: 726f8863e28d
Revises: 
Create Date: 2022-05-29 13:57:51.347280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "726f8863e28d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "articles",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String),
        sa.Column("content", sa.String),
    )


def downgrade():
    pass
