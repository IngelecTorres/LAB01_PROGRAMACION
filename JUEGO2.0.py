from random import randint
def Evaluate_Questions(question,answer,Questions_answers,option,name,eliminate_casilla_lista_option_1_2,fin_juego,correct):
 
#En esta función se evalua si la opción escogida por el usuario es la correcta, SÍ esto sucede,
#El indice de la pregunta se guardará el la lista correspondiete a "ELIMINAR" Y/O DESCARTAR DICHA PREGUNTA,
# PARA QUE NO SE VUELVA A PREGUNTAR DURANTE EL JUEGO
#SI ESTO NO SUCEDE, EL INDICE "CONTINUA SIENDO PARTE DEL JUEGO", ES DECIR, LA PREGUNTA PROBABLEMENTE APARECERÁ DE NUEVO
 if (option == 1):
    if (answer == Questions_answers[question][5]):
        print(f"Great {name}, your answer was right")
        correct[0] += 1  # SE LE SUMA 1 AL PUNTAJE, este se inicaliza en una lista debido a que si la dejamos como variable en el main generaba error debido a que se mantenía cambiando el valor a 0
        eliminate_casilla_lista_option_1_2[0][question] = question
    else:
        print(f"\nSorry, {name}, that isn't the answer, we hope you can answer it better later\n")

 if (option == 2):
    if (answer == Questions_answers[question][5]):
        print(f"Great {name}, your answer was right")
        correct[0] += 1  # SE LE SUMA 1 AL PUNTAJE
        eliminate_casilla_lista_option_1_2[1][question - 10] = question
    else:
        print(f"Sorry, {name}, that isn't the answer, we hope you can answer it better later")
    
        # Imprimir la puntuación final cuando termine el juego
 if (fin_juego == 20):
    print(f"Hey, {name}, you answered {correct[0]}/20 questions correctly in this round:)")
    print(f"Your final score is: {correct[0]} points!")
    end = int(input("Do you want to continue playing? If your answer is yes: click on '1', if your answer is no, click on '0' "))
    while (end != 1 and end != 0):
     end = int(input("Do you want to continue playing? If your answer is yes: click on '1', if your answer is no, click on '0' "))
    if (end == 0):
        return Categories
    else:
     return main()

#aqui se le pregunta al usuario si desea continuar jugando, Si la respuesta es SÍ, se inicia de nuevo el juego, Si la respuesta es NO,
#El programa se cierra automáticamente

def Questions_and_answers(Questions_answers,option,name,eliminate_casilla_lista_option_1_2,fin_juego,correct):
    if ((eliminate_casilla_lista_option_1_2[1][0]==10 and eliminate_casilla_lista_option_1_2[1][1]==11) and (eliminate_casilla_lista_option_1_2[1][2]==12 and eliminate_casilla_lista_option_1_2[1][3]==13) and (eliminate_casilla_lista_option_1_2[1][4]==14 and eliminate_casilla_lista_option_1_2[1][5]==15) and (eliminate_casilla_lista_option_1_2[1][6]==16 and eliminate_casilla_lista_option_1_2[1][7]==17) and (eliminate_casilla_lista_option_1_2[1][8]==18 and eliminate_casilla_lista_option_1_2[1][9]==19)):
        option=1
    if ((eliminate_casilla_lista_option_1_2[0][0]==0 and eliminate_casilla_lista_option_1_2[0][1]==1) and (eliminate_casilla_lista_option_1_2[0][2]==2 and eliminate_casilla_lista_option_1_2[0][3]==3) and (eliminate_casilla_lista_option_1_2[0][4]==4 and eliminate_casilla_lista_option_1_2[0][5]==5) and (eliminate_casilla_lista_option_1_2[0][6]==6 and eliminate_casilla_lista_option_1_2[0][7]==7) and (eliminate_casilla_lista_option_1_2[0][8]==8 and eliminate_casilla_lista_option_1_2[0][9]==9)):
        option=2
    #Los if anteriores corresponden a que si ya el usuario ha respondido 
    #correctamente las preguntas de una de la categorías, el programa continue mostrando las preguntas de la otra categoría
    if (option==1):
     question=randint(0,9)
     while (question==eliminate_casilla_lista_option_1_2[0][question]):
        question=randint(0,9)
     print(f"Question #{question+1} from the sports section")
    if (option==2):
     question=randint(10,19)
    
     while (question==eliminate_casilla_lista_option_1_2[1][question-10]):
        question=randint(10,19)
     print(f"Question #{question-9} from the Geography section")
    #Los if y while controlan que, si ya una de las preguntas de la categoría correspondiente se ha respondido correctamente, 
    # esta no se vuelva a repetir y se escoja, en su defecto, otra de las preguntas dentro de la misma categoría 
            
    answer=str(input(f"{Questions_answers[question][0]}\n Options:\n a. {Questions_answers[question][1]}\n b. {Questions_answers[question][2]}\n c. {Questions_answers[question][3]}\n d. {Questions_answers[question][4]}\n")).lower()
    
    while (answer!="a" and answer!="b" and answer!="c" and answer!="d"): 
        answer=str(input("Choose a, b, c or d, any other letter or character isn't permitted")).lower()
    #Se muestra la pregunta y se lee la respuesta del usuario, y se garantiza que el usuario escoja una de las opciones válidas:
    # a, b, c o d. Donde, cabe resaltar que la función lower permite también que se evite un error en el programa si el usuario
    #responde con mayúsculas, ya que la respuesta correcta se guardó en la tupla de las preguntas, con su equivalente en minúscula
        
    Evaluate_Questions(question,answer,Questions_answers,option,name,eliminate_casilla_lista_option_1_2,fin_juego,correct)
        
def Categories(name,eliminate_casilla_lista_option_1_2,fin_juego,correct):
        
    Questions_answers = ()

    while (fin_juego!=20):
        fin_juego+=1
        
        option=randint(1,2)
        Questions_answers=[["¿Who was the best goalkeeper at the World Cup Italy 90?","Sergio Goycochea","David Ospina","Walter Zenga","René Higuita","c"],
                           ["¿How many America's Cup has Brazil won?",1,5,6,3,"d"], 
                           ["How long is extra time in a football match?",15,30,45,90,"b"],
                           ["¿Where did the second Olimpycs Game take place?","Colombia","Italia","Ecuador","Grecia","d"],
                           ["In which country was volleyball invented?","Spain","Nordway","New Zeland","United States","d"],
                           ["Who won four consecutive Formula 1 world championships?","Sebastián Vettel","Rafael Nadal","Juan Pablo Montoya","Max Verstappen","a"],
                           ["What is the name of the sport in which weightlifting is done?","Lifting weights","halterofilia","Kick Boxing","Mr Olimpia","b"],
                           ["What sport is played in the NFL?","Rugby","Tenis","Basketball","American Football","d"],
                           ["What is a goal scored called in American football?","Point","Hollo in one", "Touchdown", "Goal","c"],
                           ["How often does the Olympic Games take place?","4 years","2 years","3 years","1 year","a"],

                           ["What is the smallest country in the world?","Vatican State","Groenlandia","Austria","Bolivia","a"],
                           ["How many oceans are there on Earth?",4,7,5,3,"c"],
                           ["Which country is the largest in the world?","India","Japan","United States","Rusia","d"],
                           ["Which river passes through the most countries?","Danube","Nilo","Amazonas","Rio magdalena","a"],
                           ["What is the most popular city in the world?","Bangkok","New York", "Tokyo","Dubai","c"],   
                           ["What is the country where there is never a night?","Nunavut","Normandy","Nordway","Iceland","d"],
                           ["Where is the blue and yellow river located?","Africa","America","Asia","Oceania","c"],
                           ["In which country are there the highest number of pyramids?","Peru","Sudan","Egypt","Mexico","b"],
                           ["Which country has the highest number of volcanoes?","United States","Japan","Chile","Rusia","a"],
                           ["What is the capital of Switzerland?","Lucerna","Berna","Ginebra","Basilea","b"]]

        ##Las preguntas de las dos secciones quedaron dentro de la una misma tupla
        ##Principlamente, Se utilizó una tupla ya que no se modificarán los datos allí almacenados, por otro lado, 
        # este tipo de dato ocupa menos espacio de memoria que una lista
        #Se Quitaron las variables y el match case, y se manejan los indices de 0 a 9 para la primera categoría (Donde cada indice tiene almacenada 6 espacios más 
        # que corresponden a la pregunta, opciones de respuesta y opción correcta)y de 10 a 19 para la segunda categoría
        #into the list "Questions_answers" the program keeps all the questions and answers (and especially the correct answer) it will ask to the user
        Questions_and_answers(Questions_answers,option,name,eliminate_casilla_lista_option_1_2,fin_juego,correct)


def main():
    
    name=str(input("¡¡Welcome to Trivia Crack -- Clon!!\nPlease enter a playful nickname\n"))
    #the user enter its profile name
    fin_juego=0; correct=[0]*1
    
    eliminate_casilla_lista_option_1_2=[[-1]*10,[-1]*10]
    
    #Se Inicializa la lista eliminate_casilla_lista_option_1_2 con -1, dicha lista contiene dos filas, donde:
    #A cada fila le corresponderá guardar los indices de las preguntas que el usuario ya hay respondido correctamente
    #las cuales estarán almacenadas en una lista, se podrá encontrar en la función "Categories"
    
    Categories(name,eliminate_casilla_lista_option_1_2,fin_juego,correct)
       

if __name__ == "__main__":
    main()


