from daos.product_dao import ProductDAO
from models.product import Product
import mysql.connector
from dotenv import load_dotenv
import time

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, "Oreo", "PepsiCo", 10.0)
    dao.insert(product)
    product_list = dao.select_all()
    brands = [u.brand for u in product_list]
    assert product.brand in brands

def test_product_update():
    product = Product(None, "Oreo", "PepsiCo", 10.0)
    assigned_id = dao.insert(product)

    corrected_brand = "Cream Betweens"
    product.id = assigned_id
    product.brand = corrected_brand
    dao.update(product)

    product_list = dao.select_all()
    brands = [u.brand for u in product_list]
    assert product.brand in brands

    # cleanup
    dao.delete(assigned_id)

def test_product_delete():
    product = Product(None, "Oreo", "OtherCo", 10.0)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)

    new_dao = ProductDAO()
    product_list = new_dao.select_all()
    brands = [u.brand for u in product_list]
    assert product.brand not in brands