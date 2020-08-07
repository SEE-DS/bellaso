
def bellaso_decrypt(msg, key):
    ''' INPUT: str (encrypted), key (used w tabula recta to decrypt)
        OUTPUT: str (decrypted)
    '''
    decrypted = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    offset = 0
    # for-loop over every position in the message
    for ix in range(len(msg)):
        # and if it's not an alpha w correspondence
        if msg[ix] not in alph:
            # just return the original character (whitespace or punctuation)
            output = msg[ix]
            # increment var to reflect offset that this step creates over time
            offset += -1
        # otherwise if the position wraps longer than len(alpha),
        elif (alph.find(msg[ix])) > (len(alph) - 
                            # modulo to get proper position in alphabet key
                            (alph.find(key[((ix + offset) % len(key))])) - 1):
            # then check to get our corresponding letter based on keyword
            output = alph[(alph.find(msg[ix]) - 
                            (alph.find(key[((ix + offset) % len(key))]))) % 26]
        # else is same as previous case, but no wrapping so no modulo operation
        else:
            output = alph[alph.find(msg[ix]) - 
                                (alph.find(key[((ix + offset) % len(key))]))]
        # put it all together and
        decrypted += output
    # what does that spell?
    return decrypted
# hooray!

def bellaso_encrypt(msg, key):
    ''' INPUT: str (unencrypted), key (used w tabula recta to encrypt)
        OUTPUT: str (encrypted)
    '''
    encoded = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    offset = 0
    # for-loop over every position in the message
    for ix in range(len(msg)):
        # and if it's not an alpha w correspondence
        if msg[ix] not in alph:
            # just return the original character (whitespace or punctuation)
            output = msg[ix]
            # increment var to reflect the offset this step creates over time
            offset += -1
        # otherwise if the position wraps longer than length of alphabet,
        elif (alph.find(msg[ix])) > (len(alph) - 
                            # modulo to get proper position in alphabet key
                            (alph.find(key[((ix + offset) % len(key))])) - 1):
            # then check to get our corresponding letter based on keyword
            output = alph[(alph.find(msg[ix]) + 
                            (alph.find(key[((ix + offset) % len(key))]))) % 26]
        # else is same as previous case, but no wrapping so no modulo operation
        else:
            output = alph[alph.find(msg[ix]) + 
                                (alph.find(key[((ix + offset) % len(key))]))]
        # put it all together and
        encoded += output
    # what does that spell?
    return encoded
# hooray!