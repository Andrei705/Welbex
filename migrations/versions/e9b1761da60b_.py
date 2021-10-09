"""empty message

Revision ID: e9b1761da60b
Revises: 0a95ba66ac2c
Create Date: 2021-10-01 12:51:53.488997

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e9b1761da60b'
down_revision = '0a95ba66ac2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('objects', sa.Column('date', sa.DateTime(), nullable=False))
    op.add_column('objects', sa.Column('name', sa.String(length=50), nullable=False))
    op.add_column('objects', sa.Column('quantity', sa.Integer(), nullable=False))
    op.add_column('objects', sa.Column('distance', sa.Integer(), nullable=False))
    op.drop_column('objects', 'Дата')
    op.drop_column('objects', 'Рссстояние')
    op.drop_column('objects', 'Количество')
    op.drop_column('objects', 'Название')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('objects', sa.Column('Название', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.add_column('objects', sa.Column('Количество', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('objects', sa.Column('Рссстояние', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('objects', sa.Column('Дата', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('objects', 'distance')
    op.drop_column('objects', 'quantity')
    op.drop_column('objects', 'name')
    op.drop_column('objects', 'date')
    # ### end Alembic commands ###
