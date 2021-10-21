"""empty message

Revision ID: e38f6a1ce90b
Revises: 6a060747730b
Create Date: 2021-10-21 20:36:20.428090

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e38f6a1ce90b'
down_revision = '6a060747730b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fav_character_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('fav_planet_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('fav_vehicle_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['fav_character_id'], ['favoriteCharacter.id'], name='favorite_ibfk_1'),
    sa.ForeignKeyConstraint(['fav_planet_id'], ['favoritePlanet.id'], name='favorite_ibfk_2'),
    sa.ForeignKeyConstraint(['fav_vehicle_id'], ['FavoriteVehicle.id'], name='favorite_ibfk_3'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favorite_ibfk_4'),
    sa.PrimaryKeyConstraint('user_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
