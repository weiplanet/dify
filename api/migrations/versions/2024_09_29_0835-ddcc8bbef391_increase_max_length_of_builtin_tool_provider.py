"""increase max length of builtin tool provider

Revision ID: ddcc8bbef391
Revises: d57ba9ebb251
Create Date: 2024-09-29 08:35:58.062698

"""
from alembic import op
import models as models
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddcc8bbef391'
down_revision = 'a91b476a53de' # HEAD OF PLUGIN BRANCH
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tool_builtin_providers', schema=None) as batch_op:
        batch_op.alter_column('provider',
               existing_type=sa.VARCHAR(length=40),
               type_=sa.String(length=256),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tool_builtin_providers', schema=None) as batch_op:
        batch_op.alter_column('provider',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=40),
               existing_nullable=False)

    # ### end Alembic commands ###
