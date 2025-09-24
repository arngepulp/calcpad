# calcpad
 
tldr: my message to siwen
i have an idea:
thing like desmos, but run locally
it has lines where you can insert equations in math type and define variables
but i can add shortcuts to copy over predefined equations (or basically just functions)
and i can select my pre written equations and use a solver for systems

i can also save each session in a file, so i could have something like berkeley/ae10/hw4/q3

and it saves my work, and i can write it in python so i can call the required matlab and python functions i needsometime that arent supported in desmos
theres things similiar but they are all missing some feature i want and are usually closed

9/23/25 current state is just bad cli desmos, you can declare stuff like this works
y = x+1
x = 3
eval all, y = 4
x = -1
evall all, y = 0
bc y is being stored as x = 1, and whenever evaled it checks for a definition of x in context dict

Main plans:
add support for pycalor, solving and other tools
add gui

want to add something like
1: m = 145
2: g = 9.81
3: 3mg + 2*3/sqrt(10)Fb = 0 # solve(Fb) #
(# indiciates function to be applied on line, and will edit 3 to be), 2nd # confirms end of input
3: Fb = -3mg/(sqrt10 / 6)