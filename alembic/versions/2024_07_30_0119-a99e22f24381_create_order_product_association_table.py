"""create order product association table

Revision ID: a99e22f24381
Revises: f20f3cbba23e
Create Date: 2024-07-30 01:19:57.855350

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'a99e22f24381'
down_revision: Union[str, None] = 'f20f3cbba23e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_product_association',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('order_id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
                    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('order_id', 'product_id', name='idx_unique_order_product')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_product_association')
    # ### end Alembic commands ###
