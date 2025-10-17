

def getWeekdayNameByNumber(dayNumber):
    match dayNumber:
        case 1:
            return "Segunda-feira"
        case 2:
            return "Terça-feira"
        case 3:
            return "Quarta-feira"
        case 4:
            return "Quinta-feira"
        case 5:
            return "Sexta-feira"
        case 6:
            return "Sábado"
        case 7:
            return "Domingo"
        case _:  # Default case, acts like 'default' in switch statements
            return ""

diaDaSemana = int(input("Digite o dia da semana, sendo: \n\t1- Segunda-feira\n\t2- Terça-feira\n\t3- Quarta-feira\n\t4- Quinta-feira\n\t5- Sexta-feira\n\t6- Sábado\n\t7- Domingo\n"))
diaDaSemanaDigitado = getWeekdayNameByNumber(diaDaSemana)

if(diaDaSemanaDigitado == ""):
    print("Dia Inválido!!")
else:
    print(f"O dia da semana escolhido foi: {diaDaSemanaDigitado}")



def printNameAndAge(nameToBePrinted, ageToBePrinted):
    print(f"{nameToBePrinted}")
    __printAge(ageToBePrinted)
    
def __printAge(ageToBePrinted):
    print(f"{ageToBePrinted}")

printNameAndAge("Rodrigo", 45)