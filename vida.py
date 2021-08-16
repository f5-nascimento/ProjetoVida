#FUNÇÃO DE ENTRADA DE DADOS
nome           = input("Digite o seu nome: ")
from datetime import date, datetime
dataNascimento = datetime.strptime(input("Digite a sua data de nascimento: "),'%d/%m/%Y').date()
#print(dataNascimento.strftime('%d/%m/%Y'))
peso           = float(input("Digite o seu peso: "))
altura         = float(input("Digite o sua altura: "))
tipo           = int(input("Escolha o seu tipo sanguíneo: " + "\n" +
                       "1 - Tipo A"  + "\n" +
                       "2 - Tipo B" + "\n" +
                       "3 - Tipo AB" + "\n" +
                       "4 - Tipo O: "))

#FUNÇÃO DE SAÍDA DE DADOS
print(nome + "\n" +
      str(dataNascimento.strftime('%d/%m/%Y')) + "\n" +
      str(peso) + "\n" +
      str(altura) + "\n" +
      str(tipo))

#FUNÇÃO TYPE - TIPO DE DADOS
print(type(nome), "\n",
      type(dataNascimento), "\n",
      type(peso), "\n",
      type(altura), "\n",
      type(tipo))

