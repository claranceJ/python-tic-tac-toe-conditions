blank_board = """
  1   2   3
1   |   | 
 --- --- --
2   |   | 
 --- --- --
3   |   | 
"""

name   = input("What is your name? ")
print("Welcome to Tic Tac Toe, " + name + ". Here is our playing board:")
print(blank_board)
position = input("Enter a position (i.e., 1,1): ")

# tic-tac-toe positions
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "

# Update the correct variable based on the position entered
if position == "1,1":
  a = "X"
elif position == "1,2":
  b = "X"
elif position == "1,3":
  c = "X"
elif position == "2,1":
  d = "X"
elif position == "2,2":
  e = "X"
elif position == "2,3":
  f = "X"
elif position == "3,1":
  g = "X"
elif position == "3,2":
  h = "X"
elif position == "3,3":
  i = "X"
else:
  print(position, "is not valid")

board = f"""
  1   2   3
1 {a} | {b} | {c}
 --- --- ---
2 {d} | {e} | {f}
 --- --- ---
3 {g} | {h} | {i}
"""

print(board)