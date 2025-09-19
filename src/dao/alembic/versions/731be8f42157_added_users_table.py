"""Added users table

Revision ID: 731be8f42157
Revises: 72698a74d4ea
Create Date: 2025-09-20 02:46:50.194519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '731be8f42157'
down_revision: Union[str, Sequence[str], None] = '72698a74d4ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass