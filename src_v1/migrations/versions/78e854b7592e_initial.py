"""initial

Revision ID: 78e854b7592e
Revises: 
Create Date: 2025-02-25 09:48:19.145305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78e854b7592e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.Column('is_activate', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('level', sa.Integer(), server_default='100', nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.CheckConstraint('LENGTH(name) > 0', name='name_length_check'),
    sa.CheckConstraint('LENGTH(slug) > 0', name='slug_length_check'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'level', name='uq_category_name_level'),
    sa.UniqueConstraint('slug', name='uq_category_slug')
    )
    op.create_table('seasonal_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.CheckConstraint('LENGTH(name) > 0', name='seasonal_event_name_length_check'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='uq_seasonal_event_name')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pid', sa.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('slug', sa.String(length=220), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_digital', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('stock_status', sa.Enum('oos', 'is', 'obo', name='status_enum'), server_default='oos', nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('seasonal_id', sa.Integer(), nullable=True),
    sa.CheckConstraint('LENGTH(name) > 0', name='product_name_length_check'),
    sa.CheckConstraint('LENGTH(slug) > 0', name='product_slug_length_check'),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['seasonal_id'], ['seasonal_event.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='uq_product_name'),
    sa.UniqueConstraint('pid', name='uq_product_pid'),
    sa.UniqueConstraint('slug', name='uq_product_slug')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('seasonal_event')
    op.drop_table('category')
    # ### end Alembic commands ###
