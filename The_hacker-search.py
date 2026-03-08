login=["user12","admin99","hackerX","guest","johndoe"]
for user in login:
    if user=="hackerX":
        print("Intruder detected! Shutting down system.")
        break
    else:
        print(f"Login checked:{user}")
