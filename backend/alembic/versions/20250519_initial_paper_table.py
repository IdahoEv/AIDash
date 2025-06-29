"""initial paper table

Revision ID: 20250519_initial
Revises: 
Create Date: 2025-05-19 15:23:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '20250519_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create papers table
    op.create_table(
        'papers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('authors', sa.JSON(), nullable=False),
        sa.Column('abstract', sa.String(), nullable=False),
        sa.Column('categories', sa.JSON(), nullable=False),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('doi', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_papers_id'), 'papers', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_papers_id'), table_name='papers')
    op.drop_table('papers') 