# -Notes class 1  
#### Lenguajes imperativos:
 Un paradigma imperativo da las ordenes precisas, una por una, se trata de una orden.    
#### Lenguajes declarativos:
##### -Funcional:    
- List  
- Haskell
- Clojure  
- Erlang/Elixir  
  
Los lenguajes de programación modernos tomas las características de lenguajes viejos. Si haces una función siempre es recomendable hacer la función lo mas pequeña posible.  

#### Funcion pura:  
- La fucnion pura tiene argumentos
- No produce efectos secundarios  
- Retorna siempre el mismo valor con la misma entrada.  

#### Funcion impura:  
- No tiene argumentos
- Puede retornar valores distintos.  
  
### Class 25/08/23  
  
## Notes:  
  - type: puedes ver el tipo de dato.  
  - hints o pistas: numero: int = 10, indica que el numero sera de tipo entero.  
  - Notas de jupiter: Funviona muy bien cuando buscas ejecutar partes de codigo. Corre con alt+enter.
  
## Tipos de datos:  
  
- Esta es una buena forma de ejecutar el codigo:  
num = int(input('Dame un numero entero positivo'))
if num%2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')  
  
De esta forma defines el tipo de dato en la misma linea y asi es mas facil leer el codigo.  
  
- Esta linea es mas completa ya que se lee de dentro hacia afuera:

(num := "par" if int(input('Dame un numero entero positivo'))%2 == 0 else "impar")  
  
- Casting o conversion de tipos: Esto funciona para inyectar funciones.

num_str = "3"
num_int = int(num_str)
print(f"num_int: {num_int}") #?fstrings

num_float = 3.14
num_int = int(num_float)

Ejemplo 2:  

num_str = "3."
num_int = int(num_str)
print(f"num_int: {num_int}") #?fstrings

num_float = 3.14
num_int = int(num_float)

num_str = str(num_float)
print(f"num_str: {num_str}")

- Operadores logicos
- Operadores aritmeticos:  

print(5+4) Suma

print(5-4) Resta

print(5*4) Multiplicacion

print(5/4) Division

print(5//4) Division entera

print(5%4) Modulo o residuo

print(5**4)  x a la y 
  
- Operadores logicos: 

print(True and False)

print(True or False)

print(not False)

- Condicionales

n1: int = 30

n2: int = 20

if n1 < n2:
    print(f'{n1>n2}')  
  
#### Clase 05/09/23  
  
Las listas son ordenadas e inmutables.  
  
- Sets o conjuntos:  
Los sets no admiten valores repetidos, por lo cual los eliminaran.  
La funcion 'set' tambien elimina los numeros repetidos, tambien los ordena.  
    
#### Clase 08/09/23  
  ¿Que es un patron decorador? Es una funcion que modifica el comportamiento de otra funcion.




  

  
