import re

print("Finding answers...")

RESULT = """[31m [34m-l[31m to specify the language.[39m
example: $ how2 [34m-l python[39m search text

|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|[4m[32mHow can I implement a tree in Python? - Stack Overflow[39m[24m
[4m[32m[39m[24m
## anytree
I recommend https://pypi.python.org/pypi/anytree (I am the author)

### Example

   from anytree import Node, RenderTree

   udo = Node("Udo")
   marc = Node("Marc", parent=udo)
   lian = Node("Lian", parent=marc)
   dan = Node("Dan", parent=udo)
   jet = Node("Jet", parent=dan)
   jan = Node("Jan", parent=dan)
   joe = Node("Joe", parent=dan)

   print(udo)
   Node('/Udo')
   print(joe)
   Node('/Udo/Dan/Joe')

   for pre, fill, node in RenderTree(udo):
       print("%s%s" % (pre, node.name))
   Udo
   ├── Marc
   │   └── Lian
   └── Dan
       ├── Jet
       ├── Jan
       └── Joe

   print(dan.children)
   (Node('/Udo/Dan/Jet'), Node('/Udo/Dan/Jan'), Node('/Udo/Dan/Joe'))

### Features
anytree (http://anytree.readthedocs.io/en/latest/) has also a powerful API with:


    * simple tree creation
    * simple tree modification
    * pre-order tree iteration
    * post-order tree iteration
    * resolve relative and absolute node paths 
    * walking from one node to an other.
    * tree rendering (see example above)
    * node attach/detach hookups


([4m[34mhttps://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python/39292920#39292920[39m[24m)


----------
"""

RESULT = re.sub('You should use the option', '', RESULT)
re.sub('to specify the language.', '', RESULT)
RESULT = re.sub('Press SPACE for more choices, any other key to quit.', '', RESULT)
RESULT = re.sub('<0x1b>', '', RESULT)
print(RESULT)

