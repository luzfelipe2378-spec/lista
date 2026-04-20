lista = []
input('Pressione Enter para começar')
while True:
    print('Digite "sair" para sair')
    nome = str(input('Digite o nome para inserir na lista'))
    lista.append(nome)
    for i in lista:
        print(i)
    if nome == 'sair':
        break
