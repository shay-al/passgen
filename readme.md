# passgen

passgen is a python module for generating passwprds

## Installation

add the file anywhere your import looks for modules or copy the code to any module you like
it just one class with no dependencies


## Usage

```python
from passgen import Passgen
gen=Passgen(10,True,True,True)
#returns a 10 characters password with lower and upper English alphabet and decimal numbers
str_new_password = gen.gen()
