

def update_stock(product_id, qty, stock_dict):
    """
    Updates the stock quantity for a given product after an order is placed.

    Parameters:
        product_id (str): The unique identifier of the product to update.
        qty (int): The quantity ordered to subtract from stock.
        stock_dict (dict): Dictionary mapping product IDs to their current stock levels.

    Returns:
        dict: The updated stock dictionary after processing the order.

    Edge Cases:
        - If product_id is not present in stock_dict, no update is performed.
        - Stock levels are never allowed to go negative; if subtraction results in a negative value, stock is set to zero.
    """
    # Check if the product exists in the stock dictionary
    if product_id in stock_dict:
        # Subtract the ordered quantity from the current stock
        stock_dict[product_id] -= qty
        # If stock goes negative, reset it to zero to prevent negative inventory
        if stock_dict[product_id] < 0:
            stock_dict[product_id] = 0
    # If product_id not found, no update is performed (silent fail)
    return stock_dict

print(update_stock("P01", 3, {"P01": 5}))
