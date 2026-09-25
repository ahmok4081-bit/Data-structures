#list: An ordered, mutable collection that allows duplicate elements. Created using square brackets []
# .tuple: An ordered, immutable (unchangeable) collection that allows duplicate elements. Created using parentheses ().
# set: An unordered, mutable collection of unique elements (no duplicates allowed). Created using curly braces {} or set().
# dict: An ordered (as of Python 3.7), mutable collection of key-value pairs. Keys must be unique.
#  Created using curly braces with colons {'key': 'value'}
#lidt can be mix with mutiple datatype
fruits = ["apple", "orange", "banana", "coconunt"]
print(fruits[:3])
print([fruits[::-1]])
print([fruits[::2]])
#or fruit in fruits:ßß
 #   print(fruit)
sakada = list("adafa")
print(sakada)
print(fruits.count("banana"))
fruits.append("sakada like vatey")
fruits.remove('sakada like vatey')
fruits[0] = "kdmv"
fruits.sort()
fruits.clear()
print(fruits)