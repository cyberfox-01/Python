from sys import *
import re
import math


tokensandlexems =[["Line", "LEXEMS","TOKENS"]]
symbols = [["Type","Variable Name", "Value"]]

def checknumber(number):
	result = str(number).lstrip('-').isdigit()
	if result == True:
		return True
	else:
		return False

def checkUnusedandUnassignedVariable():
	for index, items in enumerate(symbols):
		if symbols[index][2] =="":
			print("Unused or unassigned variable " + symbols[index][1] + " with " +  symbols[index][0] + " type!")

def checkVariable(variablename):
	VarHolder = 0
	varvalueState = False
	for index, items in enumerate(symbols):
		if symbols[index][1] == variablename:
			varvalueState = True
			varHolder = int(symbols[index][2])

	if varvalueState == False and checknumber(variablename) == False:
		print("Did not find the variable " + str(variablename) + " declared. Please check your code. IPOL only accepts integer values, float values are not allowed.")
		quit()
	elif varvalueState == False and checknumber(variablename) == True:
		return int(variablename)
	else:
		return int(varHolder)




def calculateDIST(DISTList):
	expresList1 = DISTList[0].strip()
	#print(expresList1)
	expresList2 = DISTList[1].strip()
	#print(expresList2)

	List1 = expresList1.split(" ")
	List2 = expresList2.split(" ")

	if List1[0].isdigit():
		express1 = int(List1[0].strip())
	else:
		express1 = checkVariable(List1[0].strip())


	if List1[1].isdigit():
		express2 = int(List1[1].strip())
	else:
		express2 = checkVariable(List1[1].strip())


	if List2[0].isdigit():
		express3 = int(List2[0].strip())
	else:
		express3 = checkVariable(List2[0].strip())

	if List2[1].isdigit():
		express4 = int(List2[1].strip())
	else:
		express4 = checkVariable(List2[1].strip())


	dist = math.sqrt((express2 - express1)**2 + (express4 - express3)**2)
	#print(dist)
	return dist

def calculateMEAN(result):
	#print(result)
	num = 0
	sumNum = 0
	i = len(result) -1
	while i > 0:
		#print(result[i])
		if result[i].isdigit():
			num = int(result[i])
		else:
			num = checkVariable(result[i])
		sumNum = sumNum + num
		i-=1
	average = sumNum // len(result)
	return average

def calcNthRoot(calcList):
	varname = ""
	variablename = ""
	#print(calcList)
	nthroot = 1/int(calcList[1])
	nthroot = int(calcList[2]) ** nthroot
	finalRoot = int(nthroot)
	return finalRoot



def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))


def removeTab(items):
	string  = re.sub("\t", "", items)
	return string

def open_file(filename):
	#print(filename)
	data = open(filename, "r").read()
	#print(data)
	return data

def computeExpr(expression):
	#print(expression)

	result = []

	i = len(expression) - 1
	while i >= 0:
		result.append(expression[i])
		if expression[i] == "MINUS":
			if result[1].isdigit():
				result1 = result[1]
			else:
				result1 = checkVariable(result[1])

			if str(result[0]).isdigit():
				result2 = result[0]
			else:
				result2 = checkVariable(result[0])

			output=int(result1) - int(result2)
			result =[]
			if str(output).lstrip('-').isdigit():
				result.append(int(output))
			else:
				result.append(int(output))

		if expression[i] == "PLUS":
			if result[1].isdigit():
				result1 = result[1]
			else:
				result1 = checkVariable(result[1])

			if str(result[0]).isdigit():
				result2 = result[0]
			else:
				result2 = checkVariable(result[0])

			output=int(result1) + int(result2)
			result =[]
			result.append(int(output))


		if expression[i] == "TIMES":
			if result[1].isdigit():
				result1 = result[1]
			else:
				result1 = checkVariable(result[1])

			if result[0].isdigit():
				result2 = result[0]
			else:
				result2 = checkVariable(result[0])

			output=int(result1) * int(result2)
			result =[]
			result.append(int(output))

		if expression[i] == "DIVBY":
			if result[1].isdigit():
				result1 = result[1]
			else:
				result1 = checkVariable(result[1])

			if result[0].isdigit():
				result2 = result[0]
			else:
				result2 = checkVariable(result[0])


			output=int(result1) / int(result2)
			result =[]
			result.append(int(output))

		if expression[i] == "MODU":
			if result[1].isdigit():
				result1 = result[1]
			else:
				result1 = checkVariable(result[1])

			if str(result[0]).isdigit():
				result2 = result[0]
			else:
				result2 = checkVariable(result[0])


			output=int(result1) % int(result2)
			result =[]
			result.append(int(output))

		if expression[i] == "RAISE":
			if result[1].isdigit():
				result1 = result[1]
			else:
				result1 = checkVariable(result[1])

			if str(result[0]).isdigit():
				result2 = result[0]
			else:
				result2 = checkVariable(result[0])


			output=power(int(result1), int(result2))
			result = []
			result.append(int(output))
		i-=1

	finalResult = int(result[0])
	#print(finalResult)
	return finalResult


def evalDINT(items, line):
	items = removeTab(items)
	
	varname =""
	varValue =""
	#print(items, line)
	keywordVar = items.split(" ")
	#print(keywordVar)
	for index, char in enumerate(keywordVar):
		#print(char)
		if char.startswith("DINT"):
			tokensandlexems.append(["[" + str(line) + "]", "DECLARATION_STRING", "DSTR"])
		if char.startswith("WITH"):
			tokensandlexems.append(["[" + str(line) + "]", "DECLARATION_ASSIGN_WITH_KEY", "WITH"])
		if char.startswith("PLUS"):
			tokensandlexems.append(["[" + str(line) + "]", "BASIC_OPERATOR", "PLUS"])
		if char.startswith("MINUS"):
			tokensandlexems.append(["[" + str(line) + "]", "BASIC_OPERATOR", "MINUS"])
		if char.startswith("TIMES"):
			tokensandlexems.append(["[" + str(line) + "]", "BASIC_OPERATOR", "TIMES"])
		if char.startswith("DIVBY"):
			tokensandlexems.append(["[" + str(line) + "]", "BASIC_OPERATOR", "DIVBY"])
		if char.startswith("MODU"):
			tokensandlexems.append(["[" + str(line) + "]", "BASIC_OPERATOR", "MODU"])
		if char.startswith("RAISE"):
			tokensandlexems.append(["[" + str(line) + "]", "ADVANCED_OPERATOR", "RAISE"])
		if char.startswith("ROOT"):
			tokensandlexems.append(["[" + str(line) + "]", "ADVANCED_OPERATOR", "ROOT"])
			meanList = items.split("ROOT")
			meanList[1].strip()
			calcNthRoot(meanList[1].split(" "))
			
		if char.startswith("MEAN"):
			tokensandlexems.append(["[" + str(line) + "]", "ADVANCED_OPERATOR", "MEAN"])
			meanList = items.split("MEAN")
			calculateMEAN(meanList[1].split(" "))
		if char.startswith("DIST"):
			tokensandlexems.append(["[" + str(line) + "]", "ADVANCED_OPERATOR", "DIST"])
			DISTList = items.split("DIST")
			calculateDIST(DISTList[1].split("AND"))

		varname = str(keywordVar[1]).strip()
		varname = varname.strip()
	if len(items.split()) < 3:
		symbols.append(["INTEGER", varname, ""])
	else:
		words = items.replace("WITH", "=")
		evaluateEx = str(words.split("=")[1]).strip()
		expression = evaluateEx.split(" ")
		varvalue = int(computeExpr(expression))
		tokensandlexems.append(["[" + str(line) + "]", "INTEGER", varvalue])
		symbols.append(["INTEGER", varname, varvalue])
	tokensandlexems.append(["[" + str(line) + "]", "IDENTIFIER", varname])


def evalSTORE(items, line):
	items = removeTab(items)
	
	varname =""
	varvalue =""
	keywordVar = items.split(" ")

	for index, char in enumerate(keywordVar):
		#print(char)
		if char.startswith("STORE"):
			tokensandlexems.append(["[" + str(line) + "]", "ASSIGN_KEY", "STORE"])
		if char.startswith("IN"):
			tokensandlexems.append(["[" + str(line) + "]", "ASSIGN_VAR_KEY", "IN"])


	number = str(keywordVar[1])
	for char1 in number:
		if char1.startswith("0") or char1.startswith("1") or char1.startswith("2") or char1.startswith("3") or char1.startswith("4") or char1.startswith("5") or char1.startswith("6") or char1.startswith("7") or char1.startswith("8") or char1.startswith("9"):
			varname = str(keywordVar[3]).strip()
			varname = varname.strip()
			varvalue = str(keywordVar[1]).strip()
			varvalue = varvalue.strip()

			tokensandlexems.append(["[" + str(line) + "]", "VALUE", varvalue])
			tokensandlexems.append(["[" + str(line) + "]", "IDENTIFIER", varname])

			for index, items in enumerate(symbols):
				if varname == symbols[index][1]:
					#print(symbols[index][1])
					symbols[index][2] = varvalue.strip()
					#print(symbols[index][2])
		else:
			string = items.split("]")
			string2 = string[0].split("[")
			getString = str(string2[1]).strip()

			varstring = items.split("IN")
			varstring2 = str(varstring[1]).strip()

			
			varname = varstring2.strip()
			varvalue = getString.strip()
			#print(varname + " " + varvalue)

			for index1, items1 in enumerate(symbols):
				comparison = symbols[index1][1]
				comparison = comparison.strip()
				#print(comparison + "FOUND" + varname)
				if comparison == varname:
					#print(comparison + "FOUND" + varname)
					#print(symbols[index1][1]
					symbols[index1][2] = varvalue
					#print(symbols[index1][2])
				#comparison = symbols[index1][1]
				#comparison = comparison.strip()
				#print(comparison)
				


def evalPRINT(items, line):
	items = removeTab(items)
	keywordVar = items.split(" ")
	for index, char in enumerate(keywordVar):
		#print(char)
		if char.startswith("GIVEYOU!"):
			tokensandlexems.append(["[" + str(line) + "]", "PRINT", "GIVEYOU!"])

	words = items.split(" ")
	#print(words[1])
	for index1, items1 in enumerate(symbols):
		if words[1] == symbols[index1][1]:
			print(str(symbols[index1][2]))

	


def evalPRINTLINE(items, line):
	items = removeTab(items)
	keywordVar = items.split(" ")
	for index, char in enumerate(keywordVar):
		#print(char)
		if char.startswith("GIVEYOU!!"):
			tokensandlexems.append(["[" + str(line) + "]", "PRINT_WITH_LINE", "GIVEYOU!!"])
		
	words = items.split(" ")
	#print(words[1])
	for index1, items1 in enumerate(symbols):
		if words[1] == symbols[index1][1]:
			print(str(symbols[index1][2]) + "\n")



def evalGIVEME(items, line):
	#print(items, line)
	items = removeTab(items)
	keywordVar = items.split(" ")
	for index, char in enumerate(keywordVar):
		#print(char)
		if char.startswith("GIVEME?"):
			tokensandlexems.append(["[" + str(line) + "]", "USER_INPUT", "GIVEME?"])

	words = items.split(" ")
	varname = words[1].strip()

	varvalueState = False
	integerCheck = True
	for index, items in enumerate(symbols):
		if symbols[index][1] == varname:
			varvalueState = True
			typeValue = symbols[index][0]

	if varvalueState == True:
		
		if typeValue == "INTEGER":
			varvalue = input("Enter an INTEGER value for " + varname + " :")
		else:
			varvalue = input("Enter value for " + varname + " :")

		for index, items in enumerate(symbols):
			if symbols[index][1] == varname and symbols[index][0] == "INTEGER" and varvalue.isdigit():
				symbols[index][2] = varvalue
			elif symbols[index][1] == varname and symbols[index][0] == "STRING":
				symbols[index][2] = varvalue
				
	if varvalueState == False:
		print("Did not find the variable "+ str(varname) +" declared. Please check your code.")
		quit()


def evalDSTR(items, line):
	varname =""
	varValue =""
	#print(items, line)
	keywordVar = items.split(" ")
	for index, char in enumerate(keywordVar):
		#print(char)
		if char.startswith("DSTR"):
			tokensandlexems.append(["[" + str(line) + "]", "DECLARATION_STRING", "DSTR"])
		if char.startswith("WITH"):
			tokensandlexems.append(["[" + str(line) + "]", "DECLARATION_ASSIGN_WITH_KEY", "WITH"])
		varname = keywordVar[1]
		varname = varname.strip()
		
	if len(items.split()) < 3:
		symbols.append(["STRING", varname, ""])
	else:
		words = items.replace("WITH", "=")
		
		varValue = str(words.split("=")[1]).strip()
		varValue = varValue[1:]
		varValue = varValue[:-1]
		
		symbols.append(["STRING", varname, varValue])
	tokensandlexems.append(["[" + str(line) + "]", "IDENTIFIER", varname])
	tokensandlexems.append(["[" + str(line) + "]", "STRING", varValue])


	


def lexer(filecontents):
	source = filecontents
	create = False
	rupture = False
	for element in source:
		if re.match("CREATE", element):
			create = True
		if re.match("RUPTURE", element):
			rupture = True
	#print(create)
	#print(rupture)
	#print(source)
	if create and rupture:
		for index, items in enumerate(source, start = 1):
			if items.startswith("CREATE"):
				tokensandlexems.append(["[" + str(index) + "]", "PROGRAM_CREATE", "CREATE"])
			if items.startswith("DSTR"):
				evalDSTR(items, index)
			
			if items.startswith("DINT"):
				evalDINT(items, index)
			if items.startswith("STORE"):
				evalSTORE(items, index)
			if items.startswith("RUPTURE"):
				tokensandlexems.append(["[" + str(index) + "]", "PROGRAM_END", "RUPTURE"])
			if items.startswith("GIVEME?"):
				evalGIVEME(items, index)
				
			if items.startswith("GIVEYOU!"):
				checkPrint = items.split(" ")
				#print(checkPrint)
				if checkPrint[0] == "GIVEYOU!!":
					evalPRINTLINE(items, index)
				else:
					evalPRINT(items, index)
	else:
		print("Check your code. Your code should be enclosed in CREATE and RUPTURE.")




def printTOKENS():
	print("===================================TOKENS AND LEXEMS===========================================================")

	for index, sublist in enumerate(tokensandlexems):
		print(str(tokensandlexems[index][0]) + " " + str(tokensandlexems[index][1]) + "\t\t\t\t\t" + str(tokensandlexems[index][2]))

def printSYMBOLS():
	print("======================================SYMBOLS TABLE===========================================================")
	for index, sublist in enumerate(symbols):
		print(str(symbols[index][1]) + "\t\t\t" + str(symbols[index][0])  + "\t\t\t\t\t" + str(symbols[index][2]))


def run():
	
	# this code is to ask use to input file to be read by interpreter
	user_input = input("Enter the path of your file: ")

	#condition to say that only .ipol file is acceptable
	if user_input[-5:] != ".ipol":
		print("File is invalid! Please enter a file that has .ipol extension.")
		quit()

	data = open_file(user_input)

	toks = data.split("\n")
	lexer(toks)
	checkUnusedandUnassignedVariable()
	printTOKENS()
	printSYMBOLS()
	#removeTab(data)

run()
