
#nombre_de_estudiante = input("ingrese el nombre del estudiante: ")
print("bienvenidoa su sistema , un honor trabajar con usted  ")
nombres = []

while True:
   nombre_est = input("ingrese el  nombre deseado   : ")
   #print(list(nombres))
   nombre_est = nombre_est.lower()
   if nombre_est ==  "fin":
      break
   elif nombre_est ==  "repetir" :
      #nombre_est = nombres.sort()
      print(nombres)
      
      # mas_largo = max(nombres,key=len)
      # mas_corto = min(nombres,key=len)
      # print(mas_largo)
      # print(mas_corto)
      # print(f"el nombre mas largo es : {mas_largo}")
      # print(f"el nombre mas corto es : {mas_corto}")
      
   elif nombre_est : 
      nombres.append(nombre_est)
   elif nombre_est :
      nombres.isspace(nombre_est)
   
print("ahora te presentare un menu con opciones que vos quieras seleccionar ")
while True :
   
   opciones = input("op1:nombres ingresados ; op2:Ordenar los nombres ;op3: Análisis de longitud de los nombres ;op4:Contar vocales y consonantes; op5:Contar palabras en cada nombre ; op6:inversión de los nombres; op7:Mostrar solo los nombres que empiezan con una letra en particular; op8:Buscar si un nombre está en la lista;op9:Contar cuántos nombres tienen más de 5 caracteres; op10:Convertir todos los nombres a mayúsculas o minúsculas  ;op11:terminar el sistema : ")   
   opciones = int(opciones)
   if opciones == 1 :
      for nombre_est in nombres:
         print(nombre_est)
   elif opciones == 2:
      nombres.sort()
      print(nombres)
   elif opciones == 3:
      mas_largo = max(nombres,key=len)
      mas_corto = min(nombres,key=len)
      #print(mas_largo)
      #print(mas_corto)
      print(f"el nombre mas largo es : {mas_largo}")
      print(f"el nombre mas corto es : {mas_corto}") 
   elif opciones == 4:
      voc = ["a","e","i","o","u"]
      vocales = 0
      consonantes = 0
      #vocales_finales = 0
      #consonantes_finales = 0
      if nombres == voc  :
         vocales == vocales +1
         
      else :
         consonantes == consonantes +1   
      print (f"la cantidad de vocales es de {vocales} ,  la cantidad de consonantes es de {consonantes}")    
         
      # for nombre in nombres :
      #  for voc in nombre:
      #    if voc == nombre:
      #       vocales += 1
      #       print(vocales)
      #    else :
      #       consonantes += 1 
      #    print (consonantes)       
   elif opciones == 5 :
      for nombre in nombres :
        num_palabras = len(nombre.split())   
        print(f"nombre: {nombre} la cantidad de palabras :{num_palabras}")
   elif opciones == 6:
      
        nombres.reverse()
        print(nombres)
   elif opciones == 7:
      letra = input("ingrese la inicial de los nombres que dese buscar : ").lower()
      for elemento in nombres :
         if elemento.startswith(letra):
            print(elemento)

   elif opciones == 8 :
      nombre_buscar = input("ingrese el nombre a buscar : ").lower()
      if nombre_buscar in nombres :
         print(f"encontrado es : {nombre_buscar}")
      else :
         print("no encontrado")

   elif opciones == 9 :
      for nom_5 in nombres :
         if len(nom_5) > 5:
            print(f"el nombre  {nom_5}  tiene mas de 5 caracters ")
   elif opciones == 10 :
      print("1.convertir a mayuscula")
      print("2.convertir a minuscula")
      eleccion = input("eleccion (1,2)")
      eleccion = int(eleccion)
      if eleccion == 1 :
        for nombre_est in nombres :
         mayuscula = nombre_est.upper() 
         print(mayuscula)
      elif eleccion == 2 :
         for nombre_est in nombres:
          minuscula = nombre_est.lower()
          print(minuscula)
   else: 
    if opciones == 11 :
      break
      

      # nombre_buscar = input("ingrese el nombre a buscar")
      # for elemento in nombres :
      #    if elemento == nombre_buscar :
      #       print(nombre_buscar)         
      #for inicial in nombres :
     # if letra.startswith(letra) :
     #  print(letra)


   #elif nombre_est ==  "long":
      #mas_largo = max(nombres)
      #mas_corto = min(nombres)
      #print(mas_largo)
      #print(mas_corto)
   #  nom_mas_largo = max(nombre_est,key=len)
   #  nom_mas_corto = min(nombre_est,key=len)
   #  print(f"nombre mas largo es {nom_mas_largo} ,  nombre mas corto es {nom_mas_corto}")
   
   
   
   #elif nombres.sort():
      #print(nombre_est)
      
   #elif nombre_est ==  "longitud":
    #nom_mas_largo = max(nombre_est,key=len)
    #nom_mas_corto = min(nombre_est,key=len)
    #print(f"nombre mas largo es {nom_mas_largo} ,  nombre mas corto es {nom_mas_corto}")

   #elif nombre_est or nombre_est.isalpha() or nombre_est.isspace():
      #nombres.append(nombre_est)
         
   #elif nombre_est :
     # nombres.isspace(nombre_est  )
   #elif nombre_est :
      #nombres.isalpha(nombre_est) 
        
   #elif nombre_est or nombre_est.isalpha() or nombre_est.isspace():
      #nombres.append(nombre_est)
   


            # nombre_de_estudiante == "repetir"
            # print("los estudiantes ingresados por el momento es de  : ")
            # for alumnos in  nombre_de_estudiante :
            #     print(alumnos)
       
             
           
         # nombre_de_estudiante.append()
#print(f"programa terminado . Los nombres ingresados son : {nombre_de_estudiante}")        

#print(nombre_de_estudiante)

# while nombre_de_estudiante :
#    pregunta = print(input("desea seguir ingrer nombres"))
#    respuesta1 = "si"
#    respuesta2 = "no"
#  if pregunta = respuesta1 :






