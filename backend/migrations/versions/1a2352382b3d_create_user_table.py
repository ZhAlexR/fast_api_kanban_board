"""Create user table

Revision ID: 1a2352382b3d
Revises: 67c1e5978a24
Create Date: 2023-10-01 13:05:38.258874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a2352382b3d'
down_revision: Union[str, None] = '67c1e5978a24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('roles', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'roles', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'roles', type_='foreignkey')
    op.drop_column('roles', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
