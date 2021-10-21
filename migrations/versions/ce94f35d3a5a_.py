"""empty message

Revision ID: ce94f35d3a5a
Revises: a6b95d11080f
Create Date: 2021-10-21 00:53:17.182194

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ce94f35d3a5a'
down_revision = 'a6b95d11080f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favoriteCharacter', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('favoriteCharacter', 'character_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favoriteCharacter', 'character_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('favoriteCharacter', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
