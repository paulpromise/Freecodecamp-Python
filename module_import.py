from module_script import multiply


multiply_two_num = multiply(4, 6)

print(multiply_two_num)

import re

pattern = r'\d+'
text = " THere are 3 apples and 5 oranges"

matches = re.findall(pattern, text)

print(matches)
from math import radians, sin, cos

print(sin(30))