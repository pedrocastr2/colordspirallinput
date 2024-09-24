import turtle #pag77      # importa os graficos tartaruga
t = turtle.Pen()
turtle.bgcolor("black") 
#Cria uma lista com 8 nomes de cores válidos quaisquerem python
colors =["red","yellow","blue","green","orange","purple","white","gray"]

#Pede ao usuário o número de lados ,entre 1 e 8,com default igual a 4
sides = int(turtle.numinput("Numeros de lados","quantos lados você quer",4,1,8))

#desenhe uma espiral colorida com o número de lados especificado pelo usuário
for x in range(360):
 t.pencolor(colors[x%sides])   #utiliza somente a quantidade certa de cores
 t.forward(x*3/sides + x)      #muda o tamanho para que corresponde ao número de lados
 t.left(360 / sides+1)         #Gira 360 / número de lados,mais 1 aumenta a largura da caneta á medida
 t.width(x*sides/200)          #que avançamos para a parte mais externa