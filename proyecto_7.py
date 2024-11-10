class persona():
    def _init_(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
# # def mostrar_info(self):
# #         print(f"Nombre: {self.nombre} {self.apellido}")
class cliente(persona):
     def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
# def mostrar_info_cliente(self):
#         super().mostrar_info()
#         print(f"Número de cuenta: {self.numero_cuenta}")
#         print(f"Balance: ${self.balance}")

def depositar(self,cantidad):
     if cantidad > 0:
          self.balance += cantidad
          print("depositaste ${cantidad} , tu saldo es de ${self.balance}")
     else:
          print("La cantidad a depositar debe ser mayor a cero.")

def retirar (self,cantidad):
     if cantidad  <=  0 :
          print("debes ingresar un valor ")
     elif cantidad > self.balance :
          print("saldo insuficiente")
     else:
          self.balance -= cantidad
          print("la cantidad retirada es de ${cantidad}, tu saldo es de ${self.balance}")
def cliente_banco():
     nombre = input("ingrese su nombre : ")
     apellido = input("ingrese su apellido : ")
     numero_cuenta = input("ingrese el numero de su cuenta : ")
     balance = float(input("porfavor ingrese su saldo : $ "))

     cliente = cliente(nombre, apellido, numero_cuenta, balance)
     return cliente
def inicio():
     print("bienvenido al mejor banco , a continuacion le daremos opciones a seguir ")
     cliente = cliente_banco
     while True : 
          print("\nOpciones disponibles:")
          print("1. Depositar dinero")
          print("2. Retirar dinero")
          print("3. Ver saldo")
          print("4. Salir")
        
          opciones = input("Selecciona una opción (1/2/3/4): ")

        #   opciones = input(""" 1. depositar dinero: $
        #                   2. retirar dinero: $
        #                   3. ver saldo : $
        #                   4. salir : """)
        #   opciones = int(opciones)
#           if opcion == "1":
#             cantidad = float(input("¿Cuánto deseas depositar? $"))
#             cliente.Depositar(cantidad)
        
#         elif opcion == "2":
#             cantidad = float(input("¿Cuánto deseas retirar? $"))
#             cliente.Retirar(cantidad)
        
#         elif opcion == "3":
#             print(cliente)  # Imprime los datos del cliente con su balance
        
#         elif opcion == "4":
#             print("¡Gracias por usar el sistema!")
#             break  # Salir del loop y terminar el programa
        
#         else:
#             print("Opción no válida. Intenta nuevamente.")

# # Ejecutar el programa
# inicio()







#          if opciones == 1 :
#                 cantidad = float(input("¿Cuánto deseas depositar? $"))
#                 print(cantidad)
#           elif opciones == 2 :
#                 cantidad = float(input("¿Cuánto deseas retirar? $"))
#                 print(cantidad)
#           elif opciones == 3 :
#                 print(cliente)
#           elif opciones == 4 :
#                print("¡gracias por elegir nuestro banco ! nos vemos en la proxima")
#                break
#           else:
#                print("por favor seleccione una opcion valida")
# inicio()
               
             
          
    
     

     
