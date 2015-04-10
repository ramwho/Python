__author__ = 'github.com/ramwho'
import os
import sys

numbers_as_text ={
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'hundred',
    1000:'thousand',
    1000000:'million',
    1000000000:'billion',
    1000000000000:'trillion'
}


def text_string_from_numbers(num):
    modulo = 0
    quotient = 0
    if (num < 10):
         return numbers_as_text[num]
    elif(num < 21):
        return numbers_as_text[num]
    elif(num < 100):
        modulo  = num % 10
        if(modulo):
            return numbers_as_text[num - modulo] + ' ' + text_string_from_numbers(modulo)
        else:
            return numbers_as_text[num - modulo]
    elif(num < 1000):
        modulo = num % 100
        quotient = int(num / 100)
        #print(numbers_as_text[quotient] + ' ' + numbers_as_text[100])
        if(modulo):
            return numbers_as_text[quotient] + ' ' + numbers_as_text[100] + ' ' + text_string_from_numbers(modulo)
        else:
            return numbers_as_text[quotient] + ' ' + numbers_as_text[100]
    elif(num < 1000000):
        modulo = num % 1000
        quotient = int(num / 1000)
        #text_string_from_numbers(quotient)
        #print(' ' + numbers_as_text[1000])
        if(modulo):
            return text_string_from_numbers(quotient) + ' ' + numbers_as_text[1000] + ' ' +  text_string_from_numbers(modulo)
        else:
            return text_string_from_numbers(quotient) + ' ' + numbers_as_text[1000]
    elif(num < 1000000000):
        modulo = num % 1000000
        quotient = int(num / 1000000)
        #text_string_from_numbers(quotient)
        #print(' ' + numbers_as_text[1000000])
        if(modulo):
            return text_string_from_numbers(quotient) + ' ' + numbers_as_text[1000000] + ' ' + text_string_from_numbers(modulo)
        else:
            return text_string_from_numbers(quotient) + ' ' + numbers_as_text[1000000]
    elif(num < 1000000000000):
        modulo = num % 1000000000
        quotient = int(num / 1000000000)
        text_string_from_numbers(quotient)
        #print(' ' + numbers_as_text[1000000000])
        if(modulo):
            return text_string_from_numbers(quotient) + ' ' + numbers_as_text[1000000000] + ' ' + text_string_from_numbers(modulo)
        else:
            return text_string_from_numbers(quotient) + ' ' + numbers_as_text[1000000000]
    elif(num < 1000000000000000):
        modulo = num % 1000000000000
        quotient = int(num / 1000000000000)
        text_string_from_numbers(quotient)
        #print(' ' + numbers_as_text[1000000000000])
        if(modulo):
            return text_string_from_numbers(quotient) + ' ' + numbers_as_text[1000000000000] + ' ' + text_string_from_numbers(modulo)
        else:
            return text_string_from_numbers(quotient) + ' ' + numbers_as_text[1000000000000]
    else:
        return "Unexpected error occurred"



while(1):
    num_value = input("Please enter a number to convert to text: ")
    print(text_string_from_numbers(int(num_value)))





