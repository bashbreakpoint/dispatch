"""Adds task plugin metadata to incident type

Revision ID: d0ee41ea14f5
Revises: 1f4dc687945d
Create Date: 2024-09-27 20:00:11.028438

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "d0ee41ea14f5"
down_revision = "1f4dc687945d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "incident_type",
        sa.Column("task_plugin_metadata", sa.JSON(), nullable=True, server_default="[]"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("incident_type", "task_plugin_metadata")
    # ### end Alembic commands ###
