import sympy as s
t=s.Symbol('t')
exp=(3*t**4)-(40*t**3)+(126*t**2)-9
v=s.diff(exp,t)
a=s.diff(v,t)
l=[0,3,5,7,10]
for i in l:
    print("for t =",i)
    print("velocity is",v.subs(t,i))
    print("acceleration is",a.subs(t,i))