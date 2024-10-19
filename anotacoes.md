Tipos de dados:
int
float
str
bool

métodos de strings:
len(exemplo) = tamanho da string
exemplo.split(delimeter) = Divide a string com base em um delimitador
exemplo.upper()
exemplo.lower()
exemplo.strip() = retira os espaços em branco
exemplo.startswith('xyz')
exemplo.endswith('xyz')
exemplo.find('xyz')
exemplo.replace('old', 'new')

operador de exponenciação é: **
operador de divisão para número inteiro é: //
operador de módulo de uma divisão é: %

comparativos: ==, !=, >, <, <=, >=

concatenar = 'teste' + ' William'

blocos de código
nos blocos de código o python sempre executa a última linha

//comentários #

para printar o tipo da variável é possível usar o método type(variableName)

exemplo de print:

print('Seu nome completo é {} e você tem {} anos.' .format(nome_completo, idade))

print(f'Seu nome completo é {nome_completo} e você tem {idade} anos')

formatar um float: 
print(f'O resultado da multiplicacação é : {v8:.3f}')

não dá para somar strings com outros tipos de dados

para transformar string em float ou int, é possível usar as seguinntes funções:
print(int(x) + y)
print(float(x) + y)

#usada para documentar
docstrings:
str1 = """Das utopias
teste
teste
"""

#slicing com strings
str2[0]
str2[1:6] #contabiliza até o anterior
//1 = posicao inicial 
//número de elementos que vou percorrer

str2[1:6:2] //com o último parâmetro ele vai percorrendo de 2 em 2

#input = serve para pedir para o usuário digitar algo no console

str2.split()
str2.split('')

exemplo.replace('old', 'new')



