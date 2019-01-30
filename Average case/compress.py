def fix_line():
	global file_reader,f_line,l_count
	f_line=f_reader.readline()
	l_count+=1

f_name="test.txt"
f_line=""
l_count=0
c_count=0

with open(f_name) as f_reader:
	f_content=f_reader.read()

s_writer=open("testsign.lbk","w")
f_writer=open("test.lbk","w")
z_writer=open("test.ttxt","w")
repeat=""
index=""
index_set=0
line_set=0

with open(f_name) as f_reader:	
	fix_line()
	while(f_line!=""):
		f_line=list(f_line)
		for i in range(len(f_line)-1):
			c_count+=1
			if(f_line[i]==f_line[i+1]):
				if(line_set==0):
					s_writer.write(str(l_count)+".")
					line_set=1								
				if(index_set==0):
					index=str(c_count+1)
					index_set=1
				repeat+=f_line[i+1]				
			else:		
				f_writer.write(f_line[i])
				z_writer.write(f_line[i])
				if(repeat!=""):
					s_writer.write(str(index)+"."+repeat+"\n")
					if(len(repeat)>2):
						z_writer.write("`"+str(len(repeat))+f_line[i]+"\n")										
					else:
						z_writer.write(repeat+"\n")
				index=""
				index_set=0
				repeat=""		
		f_writer.write("\n")
		z_writer.write("\n")
		c_count=0
		line_set=0
		fix_line()

s_writer.close()
f_writer.close()	
z_writer.close()
