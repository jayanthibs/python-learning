# packages - Built in and External

#pattern1
import math
math.sqrt(16)

#Pattern2
from math import sqrt, pi
sqrt(25)

#random

import random

number = random.randint(1,10)
choice = random.choice(["apple", "banana", "orange"])

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

from datetime import datetime
print(datetime.now())

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)