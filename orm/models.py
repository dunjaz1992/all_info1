import peewee
from playhouse.migrate import migrate, PostgresqlMigrator
from main import db 
from datetime import datetime

class Category(peewee.Model):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField(max_length=20, unique=True)
    created_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'categories'
        order_by = ('created_at')

class Products(peewee.Model):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField(max_length=40)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=100)
    category_id = peewee.ForeignKeyField(Category, to_field='id', related_name='products')
    created_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'products'
        order_by = ('created_at')

db.connect()
Category.create_table()
Products.create_table()


#--------------migrate (изменени бд)

migrator = PostgresqlMigrator(db)
migrate(
    migrator.alter_column_type('products', 'title', peewee.TextField())
)