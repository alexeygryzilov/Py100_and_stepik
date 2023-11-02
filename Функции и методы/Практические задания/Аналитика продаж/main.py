def calculate_total_sales(sales_list):
    total_sales_ = 0
    for unit in sales_list:

        total_sales_ += unit.get('quantity') * unit.get('price_per_unit')
    return total_sales_
    for product in sales_data:
        calculate_total_sales(product)
# TODO Вычислите общую стоимость проданных товаров из списка `sales_list`


sales_data = [
    {"product": "Футболка", "quantity": 10, "price_per_unit": 500},
    {"product": "Джинсы", "quantity": 5, "price_per_unit": 1000},
    {"product": "Кроссовки", "quantity": 3, "price_per_unit": 1500},
]


total_sales = calculate_total_sales(sales_data)
print(f"Общая стоимость проданных товаров: {total_sales}")
