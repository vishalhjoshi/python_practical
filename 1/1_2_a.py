milk_carton = {}
milk_expiration = (11, 11, 2019)
milk_carton['expiration_date'] = milk_expiration
milk_carton['fl_oz'] = 32
milk_carton['cost'] = 40
milk_carton['brand_name'] = 'VIKAS'
print("Brand Name : {}".format(milk_carton['brand_name']))
print(f"The expiration date is : {milk_carton['expiration_date'][0]}-{milk_carton['expiration_date'][1]}-{milk_carton['expiration_date'][2]}")
print("The cost for 6 cartons of milk is : {}".format(6 * milk_carton['cost']))