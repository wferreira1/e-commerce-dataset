from pyspark.sql.functions import *

class Dataprep():
    def __init__(self,path: str):
        self.path = path
        self.files = [
            'olist_customers_dataset.csv',
            'olist_geolocation_dataset.csv',
            'olist_order_items_dataset.csv',
            'olist_order_payments_dataset.csv',
            'olist_order_reviews_dataset.csv',
            'olist_orders_dataset.csv',
            'olist_products_dataset.csv',
            'olist_sellers_dataset.csv',
            'product_category_name_translation.csv'
        ]

    def process(self):
        pass