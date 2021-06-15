from typing import List


def number_format(number: int, mask: str):

    a: int = 0
    number = str(number)
    ls: List[str] = []
    for hasz in mask:
        if hasz == '#':
            ls.append(number[a])
            a += 1
        else:
            ls.append(hasz)
    return print(''.join(ls))


print(number_format(123456789, '##-##-##'))
print(number_format(123456789, '#,#,#,#,#,#,#,#,#'))
