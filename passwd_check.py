import getpass

def banner():
    banner = '''
                                                                     
,---.                        |    ,---.|              |              
|---',---.,---.,---.. . .,---|    |    |---.,---.,---.|__/ ,---.,---.
|    ,---|`---.`---.| | ||   |    |    |   ||---'|    |  \ |---'|    
`    `---^`---'`---'`-'-'`---'    `---'`   '`---'`---'`   ``---'`    
                                                                 by Astik Rawat\n'''
    print banner

def check_strength(passwd):
    """A strong password must be at least 8 characters long and
    must contain a lower and an upper case letter, and at least 3 digits.
    """
    # check password length
    if len(passwd) < 8:
       return False
    # check password for uppercase, lowercase and numeric chars
    hasupper = False
    haslower = False
    digitcount = 0
    for c in passwd:
                # CHECKING IF UPPER CASE
       if c.isupper():
          hasupper = True
                # CHECKING IF LOWER CASE
       elif c.islower():
          haslower = True
                # CHECKING IF DIGIT AND IF TRUE THEN COUNTING IT
       elif c.isdigit():
          digitcount = digitcount + 1
       else:
          break
        # CHECKING IF ALL CONDITION MATCH
    if hasupper and haslower and digitcount >= 3:
       return True
    else:
       return False

def main():
    # ask user input, then check its strength, 
        # Note: It wont stop until the password is strong.
    result = False
    while result is False:
                # GETPASS - TO HIDE THE ENTERED PASSWORD
       passwd = getpass.getpass('\nEnter your password to check its strength: ')
       result = check_strength(passwd)
       if result:
          print('[*] Password %s is strong' % passwd)
       else:
          print('[*] Password %s is NOT strong' % passwd)
    
if __name__ == '__main__':
    banner()
    main()
                                              
