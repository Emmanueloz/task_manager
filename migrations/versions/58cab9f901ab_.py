"""empty message

Revision ID: 58cab9f901ab
Revises: 
Create Date: 2024-10-15 23:03:23.976283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58cab9f901ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=False))
        batch_op.alter_column('fecha_creacion',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=False)
        batch_op.alter_column('fecha_modificacion',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=False)
        batch_op.create_foreign_key('fk_usuario_id', 'users', ['usuario_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notas', schema=None) as batch_op:
        batch_op.drop_constraint('fk_usuario_id', type_='foreignkey')
        batch_op.alter_column('fecha_modificacion',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=False)
        batch_op.alter_column('fecha_creacion',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=False)
        batch_op.drop_column('usuario_id')

    # ### end Alembic commands ###
