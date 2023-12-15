"""empty message

Revision ID: 40f9656058f6
Revises: 
Create Date: 2023-12-12 14:53:12.050652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40f9656058f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashedPassword', sa.String(length=255), nullable=False),
    sa.Column('firstName', sa.String(length=40), nullable=False),
    sa.Column('lastName', sa.String(length=40), nullable=False),
    sa.Column('balance', sa.Numeric(precision=12, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('fullAddress', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=50), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=50), nullable=False),
    sa.Column('zipCode', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('state', sa.String(length=100), nullable=False),
    sa.Column('zipCode', sa.String(length=10), nullable=False),
    sa.Column('priceRange', sa.Integer(), nullable=False),
    sa.Column('businessHours', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phoneNumber', sa.String(length=14), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('searchImageUrl', sa.String(length=255), nullable=False),
    sa.Column('coverImageUrl', sa.String(length=255), nullable=False),
    sa.Column('businessImageUrl', sa.String(length=255), nullable=False),
    sa.Column('pickup', sa.Boolean(), nullable=False),
    sa.Column('delivery', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('critters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('species', sa.String(length=255), nullable=True),
    sa.Column('shopId', sa.Integer(), nullable=False),
    sa.Column('price', sa.Numeric(precision=18, scale=2), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('previewImageUrl', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category'], ['categories.name'], ),
    sa.ForeignKeyConstraint(['shopId'], ['shops.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop_categories',
    sa.Column('shopId', sa.Integer(), nullable=False),
    sa.Column('categoryName', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['categoryName'], ['categories.name'], ),
    sa.ForeignKeyConstraint(['shopId'], ['shops.id'], ),
    sa.PrimaryKeyConstraint('shopId', 'categoryName')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop_categories')
    op.drop_table('critters')
    op.drop_table('shops')
    op.drop_table('addresses')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###