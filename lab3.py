# 18.1
def print_shrug_smile():
    print('¯\_(ツ)_/¯')


def print_ktulhu_smile():
    print('{:€')


def print_happy_smile():
    print('(͡°ʖ ͡°)')


# 18.2
def ask_password():
    for i in range(3):
        print('Введите пароль')
        password = input()
        if password == 'password':
            print('Пароль принят')
            break
        elif i == 2:
            print('В доступе отказано')


# 19.1
def month_name(num, lenguage):
    if lenguage == 'en':
        months = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        return months[num]
    if lenguage == 'ru':
        months = {
            1: "Январь",
            2: "Февраль",
            3: "Март",
            4: "Апрель",
            5: "Май",
            6: "Июнь",
            7: "Июль",
            8: "Август",
            9: "Сентябрь",
            10: "Октябрь",
            11: "Ноябрь",
            12: "Декабрь"
        }
        return months[num]


# 19.4
def palindrome(line):
    line = line.replace(' ', '').lower()
    if line == line[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'


# 20.1
translatedText = ''


def translate(text):
    global translatedText
    delete_letter = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
                     'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
                     '.', ',', '-']
    for i in range(len(text)):
        if text[i] not in delete_letter:
            translatedText += text[i]
    translatedText = ' '.join(translatedText.split())
    return translatedText


# 20.3
old_messages = []


def print_only_new(message):
    global old_messages
    if message not in old_messages:
        old_messages.append(message)
        print('Новые сообщения', message)


# 21.2
def from_string_to_list(string, container):
    line = ''
    string += ' '
    for i in range(len(string)):
        if string[i] != ' ':
            line += string[i]
        else:
            container.append(line)
            line = ''


# 21.3
def swap(first, second):
    first[:], second[:] = second[:], first[:]


# 22.1
def encrypt_caesar(msg, shift):
    cipher_text = ''
    for i in msg:
        if i.isalpha():
            letter = ord(i) + shift
            if letter > ord('я'):
                letter -= 32
            cipher_text += chr(letter)
        elif i == ' ':
            cipher_text += ' '
        else:
            cipher_text += '!'
    return cipher_text


def decrypt_caesar(msg, shift):
    cipher_text1 = ''
    for i in msg:
        if i.isalpha():
            letter = ord(i) - shift
            if letter > ord('я'):
                letter += 32
            cipher_text1 += chr(letter)
        elif i == ' ':
            cipher_text1 += ' '
        else:
            cipher_text1 += '!'
    return cipher_text1


# 22.2
def partial_sums(*argument):
    list_ = [0]
    res = 0
    for i in argument:
        res += i
        list_.append(res)
    return list_


# 23.1
transformation = lambda x: x


def transformation_():
    values = [1, 23, 42, 'asdfg']
    transformed_values = list(map(transformation, values))
    if values == transformed_values:
        print('ok')
    else:
        print('fail')


# 23.3
def rhythm():
    print('Введите стихотворение')
    poem = input().split()
    count_vowels = lambda inp: inp.count('а')
    counts = set(map(count_vowels, poem))
    if len(counts) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')


# 24.1
def matrix():
    table = []
    rows = int(input())
    for i in range(rows):
        line = input().split()
        table.append(line)
    if any('0' in i for i in table):
        print('True')
    else:
        print('False')


# 24.2
def num_code(letter):
    letter = letter.upper()
    return ord(letter) - ord('A') + 1


words = []
print('Введите число слов')
n = int(input())
print('Введите слова на английском')
for i in range(n):
    words.append(input())

print(*sorted(words, key=lambda x: (sum([num_code(j) for j in x]), x)), sep="\n")


# if __name__ == '__main__':
    # print_shrug_smile()
    # print_ktulhu_smile()
    # print_happy_smile()

    # ask_password()

    # print(month_name(3, "en"))
    # print(month_name(3, "ru"))

    # print(palindrome('12321'))
    # print(palindrome('Палиндром'))
    # print(palindrome('А роза упала на лапу Азора'))

    # print(translate('Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. '
    #                 'Достаточно небольшой тренировки - и вы сможете это делать.'))

    # print_only_new('Шутка номер 15')
    # print_only_new('Шутка номер 23')
    # print_only_new('Шутка номер 24')
    # print_only_new('Шутка номер 24')
    # print_only_new('Шутка номер 100')
    # print_only_new('Шутка номер 24')
    # print_only_new('Шутка номер 99')
    # print_only_new('Шутка номер 15')
    # print_only_new('Шутка номер 100')

    # a = [1, 2, 3]
    # from_string_to_list('1 3 99 52', a)
    # print(*a)
    # a = [77, 'abc']
    # from_string_to_list("", a)
    # print(*a)

    # first = [1, 2, 3]
    # second = [4, 5, 6]
    # first_content = first[:]
    # second_content = second[:]
    # swap(first, second)
    # print(first, second_content, first == second_content)
    # print(second, first_content, second == first_content)

    # msg = 'Да здравствует салат Цезарь!'
    # shift = 3
    # encrypted = encrypt_caesar(msg, shift)
    # print(encrypted)
    # decrypted = decrypt_caesar(encrypted, shift)
    # print(decrypted)

    # print(partial_sums(1, 0.5, 0.25, 0.125))

    # transformation_()

    # rhythm()

    # matrix()
