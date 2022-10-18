print('PYTRASH\n')
print('=' * 40)

print('Olá, seja bem-vinde ao programa que vai te ajudar a calcular algumas coisas.')
print('=' * 40)

question_one = float(input(('Você é aluno IFCE? Digite [1] para SIM e [2] para NÃO\n')))
if question_one == 1:
    print('Olá ifano!')
else:
    print('Se você é servidor, estamos preparando algo para vocês.')
print('=' * 40)

question_two = int(input('Você utiliza o Restaurante Universitário? Digite [1] para SIM e [2] NÃO\n'))
if question_two == 1:
    quantify = float(input('Você vai almoçar quantas vezes no IFCE na semana? '))
    print('=' * 40)
    print('Vamos para algumas informações interessantes')
    print('=' * 40)
    print('O copo utilizado no IF é de 200ml')
    result = (quantify * (0.160))
    print('=' * 40)
    print('Você gasta na semana {} kg de plástico, com os copos utilizados no IFCE'.format(result))
    print('=' * 40)
    month_cup = print('Se você almoçar todos os dias em um mês é gasto {} kgs de plástico'.format(21 * 0.160))
    print('=' * 40)
    year_cup = print('Se você almoçar todos os dias em um ano é gasto {} kgs'.format(252 * 0.160))
    print('=' * 40)
    print('Um pacote de 100 copos de 200 ml, custa R$ 9,19. Ou seja,um copo custa 0,0919.')
    print('=' * 40)
    student_money = (quantify * (0.0919))
    print(student_money)
    ticket = (student_money / 1.80)
    percent = (ticket * 100)
    print('Isso equivale a {} % da sua passagem do mêtro'.format(percent))
else:
    print('Certo! Se conhece alguém que usa, chama ela aqui!')
print('=' * 40)


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
