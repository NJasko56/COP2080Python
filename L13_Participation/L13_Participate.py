import hashlib
'''
h = hashlib.new('md5', b'cat').hexdigest()
print(f'initial hash is {h}')
for letter in 'abcdefghijklmnopqrstuvwxyz':
    best_guess = 'ca' + letter
    ha = hashlib.new('md5', best_guess.encode('UTF8')).hexdigest()
    if  (ha == h):
        print(best_guess)
        '''

letters = 'ca'
for letter1 in letters:
    for letter2 in letters:
        xx = letter1 + letter2
        print(xx)