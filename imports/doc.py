#all ways to import a module
#1.import the whole module
import math_utils
print(math_utils.add(2,3))
print(math_utils.PI)

#import just one thing and use directly
from math_utils import square
print(square(4))

from math_utils import * # This imports everything

# alias
import math_utils as mu
print(mu.square(4))
print(mu.hi())

print(mu.hello("Rohan"))