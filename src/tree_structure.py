from rich.tree import Tree
from rich import print

tree = Tree("Parent")
tree.add("Son_1")
tree.add("Son_2")

# Adding sons of the node but with different colors
tree2 = Tree("Authors")
tree2.add("[blue]Isaac Asimov")
tree2.add("[white]Charles Darwin")
tree2.add("[red]Haruki Murakami")


print(tree)
print(tree2)