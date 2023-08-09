# lambda function is an anonymous function 
# defined with the `lambda` keyword instead of `def`
# can have multiple arguments but only one expression
# usually contained to one line of code

# add_two = lambda x: x + 2

# in above example, x is the argument and x + 2 the expression

# add_two()

# why use lambda functions?
    # quick one line function
    # combine with built-in functions such as map(), filter(), apply()

import pandas as pd

df = pd.DataFrame({
    'name': ['Amy', 'Jackie', 'Sue'],
    'grades': [90, 84, 76]
})

# use the lambda function to multiply bump up the values in the grades column by 1.2
df['grades'] = df['grades'].apply(lambda x: x * 1.2)

print(df)


