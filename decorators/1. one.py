user = {"username": "Jose", "access_level": "guest"}

def get_admin_password():
    return "1234"
# direct call: password is not secure as it is accessible

def make_secure_auth(func):
    def secure_auth():
        if user["access_level"] == "admin":
            # 3. checks if the user has admin access: if yes, then
            #    calls the get_admin_password function
            return func()
        else:
            return f"No admin access for user: {user["username"]}"
    # 1. returns secure_auth function in line 18
    return secure_auth

get_admin_password = make_secure_auth(get_admin_password) # type: ignore
# 2. get_admin_password = secure_auth()

print(get_admin_password())
