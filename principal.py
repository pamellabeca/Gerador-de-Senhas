#Primeiro foi necessária a importação do módulo "random". Ele vai ser usado para gerar números aleatórios
import random
import string
#Importado o módulo de String para poder utilizar as constantes do mesmo e assim, facilitar o trabalho
#Foram definidas nossas strings
Minusculas = string.ascii_lowercase
Maiusculas = string.ascii_uppercase
Numeros = string.digits
Caracteres = string.punctuation


print("Gerador de Senhas")
print("Insira o tamanho da sua senha")
tamanho = int(input())

#Foi adicionado um menu simples para que o fique mais otimizado quando o usuário for escolher a estrutura da senha
print("Escolha a estrutura da sua senha") 
print("Para escolher Minúsculas, digite 1")
print("Para escolher Maiúsculas, digite 2")
print("Para escolher Números,    digite 3")
print("Para escolher Caracteres, digite 4")
print("Para finalizar escolhas,  digite 0")

#Através do for, será armazenado dados de entrada referente à escolha(s) feita(s) do menu e armazenadas na variável "estrutura"
#Caso a escolha seja igual a zero, acontecerá um break e o programa irá seguir para as próximas linhas
estrutura = ""
for i in range(4):
    escolha = str(input())
    if escolha == "0":
        break
    estrutura += escolha
   

#Caso essas opções estejam presentes na variável "estrutura" que está armazenando os dados de entrada do usuário, por "combinação" e as demais variáveis serem string, vão concatenar.
combinacao = ""
if "1" in estrutura:
    combinacao += Minusculas
else:
    pass

if "2" in estrutura:
    combinacao += Maiusculas
else:
    pass

if "3" in estrutura:
    combinacao += Numeros
else:
    pass

if "4" in estrutura:
    combinacao += Caracteres
else:
    pass
#Usado "join" para combinar uma lista de strings em uma única string
#Adicionada a função "sample()" que vai retornar uma lista de comprimento particular
senha = "".join(random.sample(combinacao,tamanho))

print("Sua Senha é: " + senha)


