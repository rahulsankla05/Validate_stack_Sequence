user_input=input("enter your email id:").strip()
username=user_input[:user_input.index("@")]
domain=user_input[user_input.index("@")+1:]
print(f"your username is {username} & domain name is {domain}")
