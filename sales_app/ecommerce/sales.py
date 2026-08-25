def process_sales(sales_data):
    processed_sales = []
    for sale in sales_data:
        processed_sale = {
            'product': sale['product'],
            'quantity': sale['quantity'],
            'total': sale['price'] * sale['quantity']
        }
        processed_sales.append(processed_sale)
    return processed_sales


