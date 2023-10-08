"""Added rest of models

Revision ID: 09bedba28caf
Revises: f4f601c44739
Create Date: 2023-10-07 19:44:24.817649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09bedba28caf'
down_revision: Union[str, None] = 'f4f601c44739'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('boards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=63), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=63), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('board_project',
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['boards.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], )
    )
    op.create_table('board_team',
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['boards.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], )
    )
    op.create_table('team_project',
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], )
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=63), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('expired_at', sa.DateTime(), nullable=True),
    sa.Column('priority', sa.Enum('URGENT', 'MAJOR', 'MINOR', name='taskpriority'), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('assigned_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assigned_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'permissions', ['name'])
    op.add_column('users', sa.Column('team_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'teams', ['team_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'team_id')
    op.drop_constraint(None, 'permissions', type_='unique')
    op.drop_table('tasks')
    op.drop_table('team_project')
    op.drop_table('board_team')
    op.drop_table('board_project')
    op.drop_table('teams')
    op.drop_table('projects')
    op.drop_table('boards')
    # ### end Alembic commands ###