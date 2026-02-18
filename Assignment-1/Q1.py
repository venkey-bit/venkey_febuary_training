#Smart student Eligibility checker

#1.Taking inputs from the user 
student_name=input("Enter a student name:")
age=int(input("Enter age: "))
percentage=float(input("Enter a percentage: " ))
family income=float(input("Enter family income: "))
is_rural=input("Is the student from a rural area? (true/flase): ")

#convert string into boolean 
is_rural=True if is_rural =="True" else flase

#2.Eligibility logic using short-circuting
#Eligibility if :
#(percentage> 85 AND income< 300000)
#OR percentage>90(income not checked due to short cirtuting)

elibility =(percentage > 85 and family_income< 300000) or (percentage > 90)

#3. Printing all student details (formatted string)
print("\n--- Student Details---")
print(f"name: {student_name}")
print(f"Age: {student_Age}")
print(f"percentage :{percentage}%")
print(f"family Income: {family_income}")
print(f"From rural area: {is_rurl}")

#4. Final Eligubility message
if Eligibile:
    print("\nResult: Eligible for scholarship")
    else:
        print("\nResult : Not Eligible")



#example:
Enter student name=veneky
Enter age:18
Enter percentage=92
Enter family income=50000
Is the student from the rural area?(True/Flase) 

#Out put:
Result: Eligble for scholarship