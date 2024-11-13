
######### 3. Mastering Tuple Packing and Unpacking in Python

def process_orders(orders):
    for order in orders:
        customer_name, product, quality = order
        print(f"Customer: {customer_name} ordered {quality} {product}(s).")

## Sample ordred data 
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Bdada", "Headphone", 1)
]

process_orders(orders)