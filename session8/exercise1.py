import requests

inventory_response = { 
        "product_code":"le34",
        "product_name":"Magic Bulb - Large",
        "fitting_type": "e14",
        "stock": 2,
        "unit_dimensions_cm": {
                                "width": 20,
                                "height": 40,
                                "depth": 20
                              },
        "upcoming_deliveries": [
                                    {
                                        "date": "01/02/2022",
                                        "quantity": 225
                                    },
                                    {
                                        "date": "01/03/2022",
                                        "quantity": 245
                                    }
                               ],
        "unit_price":24.32,
        "unit_currency":"EUR"
    }

'''
******************************************
print the following values:
1a. The product name of the item
******************************************
'''
print(f"Product Name: {inventory_response['product_name']}")


'''
******************************************
print the following values:
1b. How many deliveries are upcoming
******************************************
'''
print(f"No. of upcoming deliveries: {len(inventory_response['upcoming_deliveries'])}")

'''
******************************************
print the following values:
1c. When the next delivery is
******************************************
'''
print(f"Next delivery date: {inventory_response['upcoming_deliveries'][0]['date']}")


'''
******************************************
print the following values:
1d. The width of the bulb
******************************************
'''
print(f"Bulb width: {inventory_response['unit_dimensions_cm']['width']}cms")


'''
******************************************
print the following values:
1e. The unit price of the bulb and the currency it's in
******************************************
'''
print(f"Unit price: {inventory_response['unit_price']}{inventory_response['unit_currency']}")