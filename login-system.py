import time
# correct credentials
correct_username = "admin"
correct_password = "password123"

#tittle
print("="*30)
print("🔐 LOGIN SYSTEM")
print("="*30)
#attempts
attempts =0
max_attempts =3
#loop condition
while attempts < max_attempts:
    username = input("\n👤 Enter username: ")
    password = input("🔑 Enter password: ")
    # checking credentials take little time
    print("\n⏳ Checking credentials...")
    time.sleep(1)

    if username == correct_username and password  == correct_password:
        print("-"*30)
        print("🎉Login successful!")
        print("Welcome, " + username + "!")
        print("-"*30) 
        break
    else:
        attempts += 1
        print(f"\n❌Login failed! you have {max_attempts - attempts} attempts left.")
        if attempts == max_attempts:
            print("⚠️Too many attempts are failed. please try later.")
        time.sleep(1)
if attempts == max_attempts:
    print("\n" + "="*30)
    print("🚫 ACCESS DENIED")
    print("="*30)