# Calculating Simple Interest and Amount
# SI = (P * R * T) / 100


print("Welcome to the Simple Interest Calculator.")

P = float(input("Enter Pricipal Amount: \n"))
R = float(input("Enter Rate % (in digits): \n"))
T = float(input("Enter Time (in years): \n"))

SI = (P*R*T)/100
FA = P + SI
print(f"The Simple Interest on {P} for {T} years at {R}% p.a. is {SI}.")
print(f"The Final Amount is {FA}.")

print("Thank You!")
