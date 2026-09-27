"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | token, n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# alembic/env.py
from app.db.base import Base  # Import your Base metadata
from app.models.task import Task  # Import models so SQLAlchemy registers them

# Assign target_metadata
target_metadata = Base.metadata

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    ${downgrades if downgrades else "pass"}