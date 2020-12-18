from operations import MyPlexer


@MyPlexer
def login():
    import re
    email = input("please enter your email_id: ")
    password = input("please enter your password: ")
    if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z", email, re.IGNORECASE):
        return "successfully logged_in"
    else:
        return "login failed"


@MyPlexer
def evenOdd():
    num = int(input("Enter a number: "))
    if (num % 2) == 0:
        return "{0} is Even".format(num)
    else:
        return "{0} is Odd".format(num)


print(login())
print(evenOdd())
