import ast

tree=ast.parse("print('helolo World')")
exec(compile(tree, filename="<ast>", mode = "exec"))
print(ast.dump(tree))


