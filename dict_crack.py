import hashlib
import string
import os.path
import datetime

def banner():
    banner = '''                                                                            
,--. o     |    o                             ,---.|    |              |    
|   |.,---.|--- .,---.,---.,---.,---.,   .    |---||--- |--- ,---.,---.|__/ 
|   |||    |    ||   ||   |,---||    |   |    |   ||    |    ,---||    |  \ 
`--' ``---'`---'``---'`   '`---^`    `---|    `   '`---'`---'`---^`---'`   `
                                     `---'                              by Astik Rawat'''
    print (banner)

def check(passwd_hash): 
    for letter in passwd_hash: 
      if letter not in string.hexdigits: 
        print ('[*] %s is not a Hex Digit! Please Check again: ' % passwd_hash)
        return False
    return True

def hashes(hashtype):
    global hashmethod
    hashmethod = hashtype.lower()
    if hashmethod == 'md5' or hashmethod == 'sha1' or hashmethod == 'sha256' or hashmethod == 'sha512':
#        hashmethod = getattr(hashlib, hashmethod)
        return hashmethod
    else:
        print("\nError! Please select a known hashing algorithm - MD5/SHA1/SHA256/SHA512")
        exit()

def dict_attack(passwd_hash,hashmethod):
    """Dictionary attack, checks password hash against a wordlist file.
    Prints the password if found, or 'not recovered'.
   """
    print('\n[*] Cracking hash: %s' % passwd_hash)
    print('[*] Hash type: %s' % hashmethod)
    m = (getattr(hashlib, hashmethod)) 
    now = datetime.datetime.now()
    passwd_found = None
    file.seek(0)
    for word in file:
      # REMOVE ANY SPACE IF PRESENT
      word = word.strip()
      if word.islower():
        cap_word = (word.upper()) # MAKE THE WORD/PASSWORD ALL UPPERCASE
        cap_hashes = m(cap_word) # HASHING THE WORD
        cap_hash = cap_hashes.hexdigest() # CONVERTING HASH TO HEX FORMAT
        capstart_word = (word.capitalize()) # MAKE THE WORD/PASSWORD FIRST LETTER CAPITAL
        capstart_hashes = m(capstart_word)
        capstart_hash = capstart_hashes.hexdigest()
        if passwd_hash == cap_hash: # CHCEKING IF THE HASH IS SAME
           passwd_found = cap_word # IF SAME THEN PUT THE WORD IN PASSWD_FOUND
        if passwd_hash == capstart_hash:
           passwd_found = capstart_word
      hashes = m(word)
      hashes = hashes.hexdigest()
      if passwd_hash == hashes:
        passwd_found = word
    if passwd_found:
      print('[+] Password recovered: %s' % passwd_found)
      if os.path.exists('recovered.txt'):
         print ("\nSaving the progress in recovered.txt")
         recover = open("recovered.txt", "a")  # append mode
         now = now.strftime('%H:%M:%S on %A, %B the %dth, %Y')
         recover.write("\nHashes Recovered on %s\n" % now)
         recover.write("Hash: %s\nHash Type: %s\nRecovered: %s" % (passwd_hash,hashmethod.upper(),passwd_found))
         recover.write("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         recover.close()
      else:
         print ("\nCreating recovered.txt file and saving the progress")
         recover = open("recovered.txt", "w")  # write mode
         recover.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         now = now.strftime('%H:%M:%S on %A, %B the %dth, %Y')
         recover.write("\nHashes Recovered on %s\n" % now)
         recover.write("Hash: %s\nHash Type: %s\nRecovered: %s" % (passwd_hash,hashmethod.upper(),passwd_found))
         recover.write("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         recover.close()
    else:
      print('[-] Password not recovered')


def main():
        # MAKING FILE A GLOBAL VARIABLE 
    global file
        # IMPORTING WORDLIST FILE AND READ IT
    file = open("rockyou.txt", "r") 
    passwd_hash = raw_input('\nEnter the Hash to crack it: ') 
    if check(passwd_hash): # IF THE HASH PROVIDED IS HEX THEN THE DICTIONARY ATTACK WILL START ELSE SAY THE PROVIDED HASH IS NOT HEX 
        hashtype = raw_input('Enter the Hash Type [MD5/SHA1/SHA256/SHA512] : ') 
        hashes(hashtype)
        dict_attack(passwd_hash,hashmethod)
    
if __name__ == '__main__':
    banner()
    main()
