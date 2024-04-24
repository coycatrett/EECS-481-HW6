from sympy import Mul, Pow, Symbol, Integer, Add, latex

print(Mul(Pow(Symbol('x', real=True), Integer(2)), Add(Mul(Integer(2),
                                                           Symbol('x', real=True)), Integer(1))))

print(latex(Mul(Pow(Symbol('x', real=True), Integer(2)), Add(Mul(Integer(2),
                                                           Symbol('x', real=True)), Integer(1)))))

x = Symbol('x', real=True)

print(latex(Mul(Pow(x, Integer(2)), Add(Mul(Integer(3), x), Integer(1)), evaluate=False)))

print(latex(Mul(Pow(Add(Pow(x, Integer(2)), Integer(5)), Integer(2)), Add(Mul(Integer(1), Integer(3)), Integer(1), evaluate=False), evaluate=False)))

# x**2*2 (x3 + 1)
# issue with cdot between expression with exponent and polynomial expression with more than two non-zero terms
# x**(y**2 (3y + 1)) (3x + 1)





