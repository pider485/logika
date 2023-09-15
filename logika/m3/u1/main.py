with open ('da.txt', 'r', encoding='utf-8') as file:
    red=file.read()
    print(red)

with open ('da.txt', 'a', encoding='utf-8') as file:
    da1=input("впеши назву письменника")
    file.write(f'({da1})')
