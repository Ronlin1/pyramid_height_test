# so the blocks increase size by 1, 3, 6, 10, 15, 21 --> 1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5 each being a level

# method 1 --> this uses the triangular formular number to determine the height
blocks_ = int(input('Enter an integer to represent the number of blocks: '))
Triangular_Nos = []
for i in range(1, blocks_):
    # method to calculate triangular numbers
    No = (i ** 2 + i) // 2
    if No > blocks_:
        break
    Triangular_Nos.append(No)
height_ = len(Tria)
print(f'The height is {height_}')


# Method 2 - using just a while loop with an incrementer and decrementer
blocks = int(input("Enter the number of blocks: "))
height = 0
while height < blocks:
    height += 1
    blocks -= height

print(f'The height is {height}')


# Method 3 -- simple for loop without any calculation
blocks__ = int(input('Enter number of blocks:'))
j = 0
height__ = 0
for i in range(1, blocks__):
    j = j + i
    # if we exceed n blocks, break
    if j > blocks__:
        i = i - 1
        break
    height__ = i
print("The height of the pyramid:", height__)

# if you can, put these in their own function definitions to avoid confusion
