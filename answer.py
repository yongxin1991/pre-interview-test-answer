#File Name: answer/answer.py
#	Author: Zhao Yongxin
#	  Mail: yongxin1991@hotmail.com
#	Created Time: 12:00 pm 2/4/2017 - 16:00 pm 2/4/2017
#This program is for the pre-interview test of iGRAD programe
#Edit by Python 2.7.12
#Need Dependance PyRTF-0.45 and pyth-0.6.0 for .RTF document operation

from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter
import string

 
key_0 = []
key_1 = []
key_2 = ['a','b','c']
key_3 = ['d','e','f']
key_4 = ['g','h','i']
key_5 = ['j','k','l']
key_6 = ['m','n','o']
key_7 = ['p','q','r','s']
key_8 = ['t','u','v']
key_9 = ['w','x','y','z']
keyboard = (key_0,key_1,key_2,key_3,key_4,key_5,key_6,key_7,key_8,key_9)

def power(x, n=2):
	s=1
	while n>0:
		n= n-1
		s = s * x

	return s 

		
	
choice = raw_input('Enter the Question number(1 to 4): ')	

if (choice == '1'):
	word = raw_input('Enter the input word: ')
	#word = 'hello'
	count = 0
	press_count = 0
	while(count<len(word)):
	
		for key in keyboard:
			letter_count = 1
			for letter in key:		
				if word[count] == letter:
					press_count = press_count + letter_count
				letter_count = letter_count +1
		count = count +1 
						
	print press_count
	
elif (choice == '2'):
	sum = 0
	count_2 = 0
	
	word = raw_input('Enter the input word: ')		
	while(count_2<len(word)):
		key_number = 0
		for key in keyboard:

			for letter in key:		
				if word[count_2] == letter:				
					#print key_number
					sum = sum + key_number * power(10,len(word)-count_2-1)
			key_number = key_number +1	
		count_2 = count_2 +1 
	
	print sum
	
elif (choice == '3'):
	intput = raw_input('Enter number: ')
	reverse = intput[::-1]
	input_num = int(reverse)
	print input_num
	result_list=[]
	def A(x):
		global result_list
		if (x == 0):
			return result_list;
		else:
			b = x%10
			if ( not result_list):
				result_list = keyboard[b]
			else:
				temp=[]
				for i in result_list:
					for j in keyboard[b]:
						temp.append(i+j)				
				result_list = temp
		
			return A(x/10)	
				
	result = A(input_num)
	print result
	
elif (choice == '4'):
	input = raw_input('Enter number: ')
	reverse = input[::-1]
	input_num = int(reverse)
	result_list=[]

	def A(x):
		global result_list
		if (x == 0):
			return result_list;
		else:
			b = x%10
			if ( not result_list):
				result_list = keyboard[b]
			else:
				temp=[]
				for i in result_list:
					for j in keyboard[b]:
						temp.append(i+j)				
				result_list = temp
		
			return A(x/10)	
				
	result_1 = A(input_num)
	set_a = set(result_1)
	result_2 = []
	for word in result_1:
		result_2.append(word.capitalize())  
	set_b = set(result_2)
	set_c = set_a | set_b
	#read document
	#doc = Rtf15Reader.read(open('/Users/shiyue/Desktop/WordsRTF.RTF'),'r')
	doc = Rtf15Reader.read(open('./WordsRTF.RTF'),'r')
	list = PlaintextWriter.write(doc).getvalue()
	#make a set of word database
	words = list.split("\n")
	list_word = []
	for word in words:
		list_word.append(word)   
	list_word_dic = set(list_word)
	set_final = set_c & list_word_dic
	print set_final
	
else:
	print 'chioce is not in the list'