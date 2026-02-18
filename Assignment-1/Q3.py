# Smart Login System with Security Rules

# 1. Store predefined values
correct_username = "admin"
correct_password = "1234"
account_active = True   # Change to False to test account disabled case

# 2. Ask user to enter details
username = input("Enter Username: ")
password = input("Enter Password: ")

# 3. Use logical conditions with AND (short-circuit behavior)
if username == correct_username and password == correct_password and account_active:
    print("Login Successful")

elif username == correct_username and password == correct_password and not account_active:
    print("Account Disabled")

else:
    print("Wrong Credentials")

#correct login :
Enter Username: admin
Enter Password: 1234
Login Successfull

#wrong user name
Enter Username: user
Enter Password: 1234
Wrong Credentials