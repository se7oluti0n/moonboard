#!/usr/bin/python

ROWS = 18
COLS = 11

led_number = 0
led_spacing = 3

rows, cols = (ROWS, COLS) 
arr = [[0]*cols]*rows 
print(arr) 

for c in range (1,COLS+1):
    #print ("[", end="")
    for r in range(1,ROWS+1):
        led_number = led_number+led_spacing
        #print (" ",led_number, end=", ")
    #print ("],")

"""
'gz': [
       [ 17,  18,  53,  54,  89,  90, 125, 126, 161, 162, 397], # GZ LAYOUT
       [ 16,  19,  52,  55,  88,  91, 124, 127, 160, 163, 396],
       [ 15,  20,  51,  56,  87,  92, 123, 128, 159, 164, 395],
       [ 14,  21,  50,  57,  86,  93, 122, 129, 158, 165, 394],
       [ 13,  22,  49,  58,  85,  94, 121, 130, 157, 166, 393],
       [ 12,  23,  48,  59,  84,  95, 120, 131, 156, 167, 392],
       [ 11,  24,  47,  60,  83,  96, 119, 132, 155, 168, 391],
       [ 10,  25,  46,  61,  82,  97, 118, 133, 154, 169, 390],
       [  9,  26,  45,  62,  81,  98, 117, 134, 153, 170, 389],
       [  8,  27,  44,  63,  80,  99, 116, 135, 152, 171, 388],
       [  7,  28,  43,  64,  79, 100, 115, 136, 151, 172, 387],
       [  6,  29,  42,  65,  78, 101, 114, 137, 150, 173, 386],
       [  5,  30,  41,  66,  77, 102, 113, 138, 149, 174, 385],
       [  4,  31,  40,  67,  76, 103, 112, 139, 148, 175, 384],
       [  3,  32,  39,  68,  75, 104, 111, 140, 147, 176, 383],
       [  2,  33,  38,  69,  74, 105, 110, 141, 146, 177, 382],
       [  1,  34,  37,  70,  73, 106, 109, 142, 145, 178, 381],
       [  0,  35,  36,  71,  72, 107, 108, 143, 144, 179, 380]
"""