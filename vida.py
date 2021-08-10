#FUNÇÃO DE ENTRADA DE DADOS
nome = input("Digite o seu nome: ")
dataNascimento = input("Digite a sua data de nascimento: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite o sua altura: "))
tipo = input("Digite o seu tipo sanguíneo: ")

#FUNÇÃO DE SAÍDA DE DADOS
print(nome + "\n" +
      dataNascimento + "\n" +
      str(peso) + "\n" +
      str(altura) + "\n" +
      tipo)

#UTILIZANDO A FUNÇÃO TYPE
print(type(nome), "\n",
      type(dataNascimento), "\n",
      type(peso), "\n",
      type(altura), "\n",
      type(tipo))
