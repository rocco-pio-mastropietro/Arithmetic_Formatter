## funzione che riceve una lista di stringhe che sono problemi aritmetici
#  @param problems lista di problemi aritmetici
#  @param showResults [opzionale] valore booleano True (mostra i risultati di ciascun problema) / False
#  @return arranged_problems restituisce i problemi disposti verticalmente e fianco a fianco
#
def arithmetic_arranger(problems, showResults = False) :

  arranged_problems = ""  # inizializzazione della variabile di return
  
  import re  # importa il modulo che interpreta le Espressioni Regolari

  # ciclo che estrate gli operandi di ciascun problema e li raccoglie in operands
  operands = []
  i = 0
  while i < len(problems) :
    operands.append(re.split(r'\s\W\s', problems[i]))
    i += 1
  
  # situazioni che devono restituire un errore
  if len(operands) > 5 :  # ciclo che verifica se ci sono troppi problemi. il limite è cinque
    arranged_problems = "Error: Too many problems."
  else:
    for p in problems :  # moltiplicazione e divisione devono dare un errore
      if '*' in p or '/' in p :
        arranged_problems = "Error: Operator must be '+' or '-'."
        break
    else :
      for i in range(len(operands)) :  # ogni operando deve contenere solo cifre
        if re.search(r"\D", operands[i][0]) != None or re.search(r"\D", operands[i][1]) != None :
          arranged_problems = "Error: Numbers must only contain digits."
          break
      else:
        for i in range(len(operands)) :  # ogni operando ha una lunghezza di massimo 4 cifre
          if len(operands[i][0]) > 4 or len(operands[i][1]) > 4 :
            arranged_problems = "Error: Numbers cannot be more than four digits."
            break
        else:
          
          # ciclo che visualizza la prima riga degli operandi
          firstRow = ""
          for i in range(len(operands)) :
            if len(operands[i][0]) < len(operands[i][1]) :
              firstRow += " " * 2 + " " * (len(operands[i][1]) - len(operands[i][0])) + operands[i][0]
            else :
              firstRow += " " * 2 + operands[i][0]
            if i != len(operands) - 1 : firstRow += " " * 4
          
          # ciclo che visualizza la seconda riga degli operandi
          secondRow = ""
          for i in range(len(operands)) : 
            if "+" in problems[i] :  # condizione che verifica l'operatore matematico
                                     # di ciascun problema e lo assegna ad operator
              operator = "+"
            else :
              operator = "-"
              
            if len(operands[i][0]) < len(operands[i][1]) :
              secondRow += operator + " " + operands[i][1]
            else :
              secondRow += operator + " " + " " * (len(operands[i][0]) - len(operands[i][1])) + operands[i][1]
            if i != len(operands) - 1 : secondRow += " " * 4
          
          # ciclo che visualizza le linee tratteggiate
          dashedLine = ""
          for i in range(len(operands)) :
            dashedLine += "-" * (max(len(operands[i][0]), len(operands[i][1])) + 2)
            if i != len(operands) - 1 : dashedLine += " " * 4

          # ciclo che visualizza la riga dei risultati
          resultsRow = ""
          results = []
          for i in range(len(operands)) :
            if "+" in problems[i] :  # condizione che verifica l'operatore matematico
              results.append(int(operands[i][0]) + int(operands[i][1]))
            else :
              results.append(int(operands[i][0]) - int(operands[i][1]))
            resultsRow += " " * ((max(len(operands[i][0]), len(operands[i][1])) + 2) - len(str(results[i]))) + str(results[i])
            if i != len(operands) - 1 : resultsRow += " " * 4

          # compilazione della soluzione in arranged_problems
          if showResults == True :
            arranged_problems = firstRow + "\n" + secondRow + "\n" + dashedLine + "\n" + resultsRow
          else:
            arranged_problems = firstRow + "\n" + secondRow + "\n" + dashedLine
          
  return arranged_problems

## test della funzione arithmetic_arranger()
print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']))
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
