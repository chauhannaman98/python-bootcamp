def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    print(kwargs["name"])
    for key, item in kwargs.items():
        print(f"{key}: {item}")

print_nicely(name="Naman", age=25)