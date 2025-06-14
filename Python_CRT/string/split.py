"""WAPP to read Mail ID as input from the user and print user name and organization name based on mail ID (name@orgname.com)"""
Mail_ID=input("Enter the Mail ID:")
name,domain=Mail_ID.split("@")
orgname=domain.split(".")[0]
print(f"Username is: {name}")
print(f"orgname is: {orgname}")