#import re
#b = re.compile(r'\d+\.\d+\.\d+.*?')
#e = 'Ross McFluff: 834.345.1254 155'
#c = b.search(e)
#print c.group()
#text = "Python for beginner is a very cool website"
#p = re.split('cool',text, flags=re.IGNORECASE)
#print p


#import os
#pwd = os.getcwd()
#for roots,dirs, files in os.walk("/Users/deepeshk/Documents"):
	#print files
	#print dirs	
	#print roots
#	for f in dirs:
#		print os.path.join(roots,f)

#import sys,os
#print 'sys.argv[0] =', sys.argv[0]            
#pathname = os.path.dirname(sys.argv[0])        
#print 'path =', pathname
#print 'full path =', os.path.abspath(pathname)


#def y(*args):
#	print type(args)


#def x(** kwargs):
#	print type(kwargs)


#x()
#y()



#def fnc2(arg1, arg2, *args, **kwargs):
 #  print('{} {} {} {}'.format(arg1, arg2, args, kwargs))

#print('fnc2()')
#fnc2() # error
#fnc2(1,2)
#fnc2(1,2,3,'haystack')
#fnc2(arg1=1, arg2=2, c=3)
#fnc2(arg1=1, arg2=2, c=3, d='Spark')
#fnc2(1,2,3, a=1, b=2)
#fnc2(*lst, **dct)
#fnc2(*tpl, **dct)
#fnc2(1,2,*tpl)
#fnc2(1,*tpl,d='nltk')
#fnc2(1,2,*tpl,d='scikit')






		#print output
		#print output1

#def main():
#	hosts = ['10.195.169.132', '10.195.169.133','10.195.169.134','10.195.169.135']
#	t1 = threading.Thread(target=device_connect, args=(hosts,))
#	t1.start()

#if __name__ == "__main__":
#	main()

#host = ['10.195.169.132', '10.195.169.133','10.195.169.134','10.195.169.135']
#device_connect(host)





with open('store.txt','r+') as f:
	a =f.readlines()
	b = []
	for i in a:
		b.append(i.strip())
	print b
	for j in b:
		print j
	#print len(a)
	#for i in a:
	#	print i
	##b = ' '.join(a)
	#print b


























































































