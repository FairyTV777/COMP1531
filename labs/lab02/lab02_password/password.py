def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''

    horrible_password = ["password", "iloveyou", "123456"]
    string = ''

    num = False
    upper = False
    lower = False

    for char in list(password):
        if char.isdigit():
            num = True
        elif char.isupper():
            upper = True
        elif char.islower():
            lower = True

    if password in horrible_password:
        string = "Horrible password"
    elif len(password) >= 12 and num and upper and lower:
        string = "Strong password"
    elif len(password) >= 8 and num:
        string = "Moderate password"
    else:
        string = "Poor password"
    
    return string


if __name__ == '__main__':
    print(check_password("ihearttrimesters"))
    # What does this do?
    # if run this file, run this part as main()
    # if import this file, ignore this part