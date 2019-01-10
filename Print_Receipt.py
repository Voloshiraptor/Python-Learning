# Simple application of the basics to print out a receipt for a customer

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. " \
                              "32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00
stylish_sette_description = "Stylish Settee. Faux leather on birch. " \
                            "29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_sette_price = 180.50
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15
sales_tax = .088
customer_one_total = 0
customer_one_itemization = ""

customer_one_itemization += lovely_loveseat_description
customer_one_total += lovely_loveseat_price
customer_one_total += luxurious_lamp_price
customer_one_itemization += "\n"
customer_one_itemization += luxurious_lamp_description

# checkout customer one
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("\nCustomer One Items:")
print(customer_one_itemization)
print("\nCustomer One Total:")
print(customer_one_total)

# customer two
customer_two_total = 0
customer_two_itemization = ""

customer_two_total += stylish_sette_price
customer_two_itemization += stylish_sette_description
customer_two_total += luxurious_lamp_price
customer_two_itemization += "\n"
customer_two_itemization += luxurious_lamp_description

customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

print("\nCustomer Two Items:")
print(customer_two_itemization)
print("\nCustomer Two Total:")
print(customer_two_total)
