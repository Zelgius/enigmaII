import re
import sys
wheelV = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wheelVI = ['a', 'c', 'e', 'd', 'f', 'h', 'g', 'i', 'k', 'j', 'l', 'n', 'm', 'o', 'q', 'p', 'r', 't', 's', 'u', 'w', 'v', 'x', 'z', 'y', 'b']
wheelVII = ['a', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b']
wheels = {"5": wheelV, "6": wheelVI, "7": wheelVII}


def rotate(l, n):
    return l[n:] + l[:n]


def encrypt(order, code, message):
    enc1 = rotate(wheels[order[0]], wheels[order[0]].index(code[0]))
    enc2 = rotate(wheels[order[1]], wheels[order[1]].index(code[1]))
    key = rotate(wheels[order[2]], wheels[order[2]].index(code[2]))

    enc_message = ""
    gear = 0
    num_letters = 1
    for let in message:
        if gear == 0:
            index = key.index(let)
            enc_message += enc1[index]
            gear = 1
        elif gear == 1:
            index = key.index(let)
            enc_message += enc2[-index]
            gear = 0
        if num_letters == 4:
            enc_message += " "
            num_letters = 1
        else:
            num_letters += 1

    return enc_message.upper()


if __name__ == "__main__":
    alpha_regex = re.compile('[^a-zA-Z]')

    # get and validate order
    order = raw_input("Enter order: ")
    if len(order) != 3:
        print "Invalid order"
        sys.exit(1)

    # get and validate code
    code = raw_input("Enter the code: ")
    code = alpha_regex.sub('', code).lower()
    if len(code) != 3:
        print "Invalid code"
        sys.exit(1)

    # get and sanitate message to encrypt
    message = raw_input("Enter the messae to encrypt: ")
    message = alpha_regex.sub('', message).lower()

    print encrypt(order.lower(), code.lower(), message)
