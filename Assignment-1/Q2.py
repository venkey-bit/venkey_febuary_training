#Online ShoppingDiscount System

#1.Taking inputs
coustmer_name=input("Enter coustmer name: ")
product_price=float(input("Enter product price: "))
is_premium=input("Is the custmer a premium member?(True/Flase): ")
copun_code=input("Enter coupen code: ")

#convet string to boolean
is_premium= True if is_premium=="True"else Flase

#Initialize discount
discount = 0

#2. Apply discounts rules
if product_price > 5000 and is_premium:
    discount = 0.20  # 20%
elif coupon_code == "SAVE10" or is_premium:
    discount = 0.10  # 10%

# Calculate final price
discount_amount = product_price * discount
final_price = product_price - discount_amount

# Print results
print("\n----- BILL DETAILS -----")
print(f"Customer Name: {customer_name}")
print(f"Original Price: ₹{product_price}")
print(f"Discount Applied: {discount * 100}%")
print(f"Final Price: ₹{final_price}")

if is_premium:
    print("Premium benefits applied")

Enter customer name: Venkey
Enter product price: 6000
Is the customer premium? (True/False): True
Enter coupon code: ABC

----- BILL DETAILS -----
Customer Name: Venkey
Original Price: ₹6000.0
Discount Applied: 20.0%
Final Price: ₹4800.0
Premium benefits applied