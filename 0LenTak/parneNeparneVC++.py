i =  int(input("Zadaj hodnotu i: "))#2**8


with open("main.cpp", "w", encoding="utf-8") as f:
    f.write('#include <iostream>\nusing namespace std;\n\nint main() {\n')
    f.write('    int cislo;\n    cin >> cislo;\n\n')

    for j in range(1, i + 1):
        typ = "parne" if j % 2 == 0 else "neparne"
        f.write(f'    if (cislo == {j}) cout << "{typ}";\n')

    f.write('\n    return 0;\n}')
