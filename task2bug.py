from sympy import latex, TableForm

t = TableForm([[1, 2]])
latex([t])
# orignal buggy code
print('original buggy code:')
print('command: print(latex([t]))')
print(latex([t]))

# simplier buggy code without [] around t
print('\nsimpler issue without [] instance 1')
print('command: latex(t, mode=\'equation\')')
print(latex(t, mode='equation'))

print('\nsimpler issue without [] around t instance 2')
print('command: latex(t, mode=\'inline\')')
print(latex(t, mode='inline'))

print('\noriginal print without [] around t\nprint(latex(t))')
print('command: print(latex(t))')
print(latex(t))
print('\ncommand: print([t])')
print([t])
