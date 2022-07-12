#Программа переделывает строку из кириллицы в латиницу!

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def get_strip(de):
    def strip1(h):
        h = de(h)
        while '--' in h:
            h = h.replace('--', '-')
        return h

    return strip1


c = []


@get_strip
def get_string(str):
    for i in str:
        for j in i:
            if j in t:
                c.append(t[j])
            elif j in ': ;.,_':
                c.append('-')
            else:
                c.append(j)
    Z = ''.join(c)
    return Z


s = input().lower()
f = get_string(s)
print(f)