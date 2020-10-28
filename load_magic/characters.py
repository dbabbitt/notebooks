
def outline_chars(text_str):
    ord_list = []
    for char in list(text_str):
        i = ord(char)
        if i >= ord('a'):
            i += (ord('𝕒') - ord('a'))
        elif i >= ord('A'):
            i += (ord('𝔸') - ord('A'))
        #print(f'{char} or {ord(char)}: {i} or {chr(i)}')
        ord_list.append(i)
        
    return ''.join([chr(i) for i in ord_list])