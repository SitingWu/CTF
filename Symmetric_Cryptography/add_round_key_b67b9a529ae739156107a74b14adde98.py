from Crypto.Util.number import *
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def add_round_key(s, k):
    key = [ [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0], ]
    for i in range(4):
        for j in range(4):
            key[i][j]= s[i][j]^k[i][j]

    return key
#----better answer from others
# import numpy
# def add_round_key(s, k):
#  return map(int,numpy.bitwise_xor(sum(s, []), sum(k, [])))

# def add_round_key(s, k):
#     return [[sss^kkk for sss, kkk in zip(ss, kk)] for ss, kk in zip(s, k)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    # bytes_char=''
    byte_array=""
    for i in range(4):
        for j in range(4):
            byte_array+= (chr(matrix[i][j]))
    return byte_array.encode()

print(add_round_key(state, round_key))
print(matrix2bytes(add_round_key(state, round_key)))
print(list(list(zip(s,k ))for s,k in zip(state, round_key)))



