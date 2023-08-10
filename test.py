import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

Str_A = 'brigham young university--provo'
Str_B = 'brigham young university (2)' 
ratio = fuzz.ratio(Str_A.lower(), Str_B.lower())
print('Similarity score: {}'.format(ratio))