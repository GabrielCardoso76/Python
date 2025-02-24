import csv

def obter_dados_usuarios():
    nome = input("Digite seu Nome: ")
    idade = input("Digite a sua idade: ")
    cidade = input("Digite sua Cidade: ")
    return [nome, idade, cidade]

def salvar_dados_no_csv(dados):
    with open('usuario.csv' ,mode='a' ,newline='' ,encoding='utf-8')as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(dados)
    print("Dados salvos com sucesso !")

def exibir_dados_csv():
    try:
        with open('usuarios.csv' , mode='r' ,newline='' ,encoding='utf-8')as arquivo:
            leitor = csv.reader(arquivo)
            print("\nDados armazenados com sucesso no csv")
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("O arquivo ainda não foi criado")

while True:
    