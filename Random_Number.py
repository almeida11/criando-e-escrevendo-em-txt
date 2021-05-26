import random
from random import randint
var1 = randint(000, 999)
number = (str(var1))
#CRIANDO E ESCREVENDO EM TXT
arquivo = open("Random_Number.txt", "a")
arquivo.write('# {} \n'.format (number))
print(var1)
