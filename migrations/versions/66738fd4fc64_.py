"""empty message

Revision ID: 66738fd4fc64
Revises: b839526f3b56
Create Date: 2020-11-25 15:18:53.301055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66738fd4fc64'
down_revision = 'b839526f3b56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('screen_name', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('followers', sa.Integer(), nullable=True),
    sa.Column('latest_tweet_id', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tweet',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('full_text', sa.String(length=500), nullable=True),
    sa.Column('embedding', sa.PickleType(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweet')
    op.drop_table('user')
    # ### end Alembic commands ###
