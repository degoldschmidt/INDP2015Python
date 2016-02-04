myname = str(input("Type in your name: "))             # Here you input your name
asciidec = []                                          # List of ASCII decimals
asciihex = []                                          # List of ASCII hexadecimals
asciibin = []                                          # List of ASCII binaries
for i in range(len(myname)):                           # Go through all chars in the input string
    asciidec.append(ord(myname[i]))                    # ord() turns char into ASCII decimal
    asciihex.append(hex(asciidec[i]))                  # hex() turns ASCII decimal into hexadecimal
    asciibin.append(bin(asciidec[i]))                  # bin() turns ASCII decimal into binary
print("Your name in decimal ASCII is ", asciidec)      # Final printout of your name
print("Your name in hexadecimal ASCII is ", asciihex)  # Final printout of your name
print("Your name in binary ASCII is ", asciibin)       # Final printout of your name