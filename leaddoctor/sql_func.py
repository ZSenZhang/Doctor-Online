import MySQLdb
import sys
import datetime

#这个函数是用户提交问题时调用
#username为用户名，字符串；symptom为自己描述的症状，字符串；toprivatedoc为选择是否提交给私人医生
#department为用户自己填写的挂哪个科室的医生；imagepath为症状照片的路径
def commit_question(username, symptom, toprivatedoc=False, department=None, imagepath=None):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	cursor.execute('''SELECT MAX(DISTINCT INNUM) FROM INQUIRY''')
	maxid_all = cursor.fetchall()
	# print(maxid_all)

	if maxid_all[0][0] == None:
		this_id = 0
	else:
		this_id = maxid_all[0][0] + 1

	dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	cursor.execute('''INSERT INTO INQUIRY(INNUM,TIME,USERNAME,SYMPTOM,TO_PRIVATEDOCTOR,ISDEALING,DONE) VALUES(\
					{},'{}','{}','{}',{},{},{})'''.format(this_id,dt,username,symptom,toprivatedoc,False,False))

	if department != None:
		cursor.execute('''UPDATE INQUIRY SET CLASS = '{}' WHERE INNUM = {}'''.format(department,this_id))

	if imagepath != None:
		cursor.execute('''UPDATE INQUIRY SET IMAGE = '{}' WHERE INNUM= {}'''.format(imagepath,this_id))

	cursor.close()

	db.commit()
	db.close()

#这个函数用来查询所有问诊表中科别为空且未提交给私人医生的记录并显示给导流医师
#可用下面的函数里的result[n]来访问第n条记录
#result[n][0]表示第n条问诊单的单号，result[n][1]表示第n条记录的时间，result[n][2]表示第n条记录的症状
def selectAllNoClass():
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	cursor.execute('''SELECT INNUM,TIME,SYMPTOM FROM INQUIRY WHERE CLASS IS NULL AND TO_PRIVATEDOCTOR=FALSE ORDER BY TIME ASC''')
	result = cursor.fetchall()

	for data in result:
		innum = data[0] 
		time = data[1]
		symptom = data[2]
		print(innum,time,symptom)
	cursor.close()

	return result

#这个函数用于将导流医师导流的信息更新到数据库
#innum为问诊单的单号，department为导流医师决定的科室
def decideDepartment(innum,department):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	cursor.execute('''UPDATE INQUIRY SET CLASS = '{}' WHERE INNUM = {}'''.format(department,innum))

	cursor.close()
	db.commit()
	db.close()

#这个函数用于私人医生查询某一用户的所有历史问诊信息，按时间顺序降序排列
#username为用户的名字
#返回值final_data为一个列表，列表里的每一个元素为一个元组，表示一条历史问诊信息。元组里的元素依次为问诊单号、时间、症状、症状图片路径、诊断、药品元组
def selectUserHistory(username):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	final_data = []

	cursor.execute('''SELECT INNUM,TIME,SYMPTOM,IMAGE,DIAGNOSES FROM INQUIRY WHERE USERNAME='{}' AND DONE = {} ORDER BY TIME DESC'''.format(username,True))
	result = cursor.fetchall()

	for data in result:
		innum = data[0]
		time = data[1]
		symptom = data[2]
		imagepath = data[3]
		diagnoses = data[4]

		print(innum,time,symptom,imagepath,diagnoses)
		cursor.execute('''SELECT DRUGNAME FROM INQUIRYFORDRUG WHERE INNUM = {}'''.format(innum))
		drugs = cursor.fetchall()

		final_drug = []
		for item in drugs:
			drug = item[0]
			print("drugs for {}: {}".format(innum,drug))
			final_drug.append(drug)

		final_data.append((innum,time,symptom,imagepath,diagnoses,final_drug))

	cursor.close()
	return final_data

#这个函数用于用户查询自己的问诊信息是否被处理完
#username为用户名
#返回值result为一个元组，元组里的每一个元素为一个元组，表示一条历史问诊信息，元组里的元素依次为问诊单号、时间、症状、是否被接诊、是否诊断完成
def displayMyInquiry(username):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	cursor.execute('''SELECT INNUM,TIME,SYMPTOM,ISDEALING,DONE FROM INQUIRY WHERE USERNAME='{}' ORDER BY TIME DESC'''.format(username))
	result = cursor.fetchall()

	for data in result:
		innum = data[0]
		time = data[1]
		symptom = data[2]
		isdealing = data[3]
		isdone = data[4]

		print(innum,time,symptom,isdealing,isdone)

	cursor.close()
	return result

#这个函数用于用户查询自己的问诊单的处置结果
#innum为问诊单的单号
#返回值依次为诊断，三餐建议，和药品（元组）
def displayInquiryResult(innum):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	cursor.execute('''SELECT DIAGNOSES,BREAKFAST,LUNCH,DINNER FROM INQUIRY WHERE INNUM={}'''.format(innum))
	result = cursor.fetchall()

	diagnoses = result[0][0]
	breakfast = result[0][1]
	lunch = result[0][2]
	dinner = result[0][3]

	cursor.execute('''SELECT DRUGNAME FROM INQUIRYFORDRUG WHERE INNUM = {}'''.format(innum))
	drugs = cursor.fetchall()

	for item in drugs:
		drug = item[0]
		print("drugs for {}: {}".format(innum,drug))

	cursor.close()

	return diagnoses,breakfast,lunch,dinner,drugs

#这个函数是用于普通医生查询自己对应科别且是否已被接诊数据为False的记录
#department是医生所属科室
#result[n]来表示第n条记录，result[n][0:3]分别表示第n条问诊单的单号、时间、症状、症状图片路径
def selectInquiry(department=None):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	cursor.execute('''SELECT INNUM,TIME,SYMPTOM,IMAGE FROM INQUIRY WHERE CLASS = '{}' AND ISDEALING = FALSE AND TO_PRIVATEDOCTOR = FALSE ORDER BY TIME ASC'''.format(department))
	result = cursor.fetchall()

	for data in result:
		innum = data[0] 
		time = data[1]
		symptom = data[2]
		imagepath = data[3]
		print(innum,time,symptom,imagepath)
	cursor.close()

	return result
	
#这个函数是用于私人医生查询自己对接的所有用户，且是否已被接诊数据为False、是否提交给私人医生为True的记录
#只显示有问诊单的数据信息，比如有的用户没有问诊信息就不予显示
#doctorName是私人医生姓名
#result[n]来表示第n条记录，result[n][0:3]分别表示第n条问诊单的单号、时间、症状、症状图片路径
def selectInquiryPrimary(doctorName):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()
    
	cursor.execute('''SELECT INNUM,USERNAME,TIME,SYMPTOM,IMAGE FROM USER_PRIVATEDOCTOR INNER JOIN INQUIRY ON USER_PRIVATEDOCTOR.USERNAME=INQUIRY.USERNAME WHERE PDOCTORNAME IS '{}' AND TO_PRIVATEDOCTOR = TRUE AND ISDEALING = FALSE '''.format(doctorName))
	result = cursor.fetchall()
	
	for userData in result:
		innum = userData[0]
		username = userData[1]
		time = userData[2]
		symptom = userData[3]
		imagepath = userData[4]		
		print (innum,username,time,symptom,imagepath)
	cursor.close()

	return result

#（普私共用）这个函数是用于医生确认接诊后更新对应的是否接诊信息
#innum是接诊单号
#result可以用来显示该问诊单基本信息，result[0][0:4]分别表示单号、时间、科室、症状、症状图片路径
def acceptToDiagnose(innum):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()
	
    #显示所接单的基本信息
	# cursor.execute('''SELECT INNUM,TIME,SYMPTOM,IMAGE FROM INQUIRY WHERE INNUM = {}'''.format(innum))
	# result = cursor.fetchall()

	
	# innum = result[0][0] 
	# time = result[0][1]
	# #department = result[0][2] 如果需要将普通医生与私人医生分开，可以将此处注释删除即为普通医生
	# symptom = result[0][2]
	# imagepath = result[0][3]
	# print(innum,time,symptom,imagepath)
		
    #更新INQUIRY表为接诊
	cursor.execute('''UPDATE INQUIRY SET ISDEALING = TRUE WHERE INNUM = {}'''.format(innum))
	
	cursor.close()
	db.commit()
	db.close()
	
	# return result

	
	
#（普私共用）这个函数是用于普通医生填写诊断信息
#innum是接诊单号，diagnose是医生的诊断
def writeDiagnose(innum,diagnose):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	cursor.execute('''UPDATE INQUIRY SET DIAGNOSES = '{}' WHERE INNUM = {}'''.format(diagnose,innum))
    
	cursor.close()
	db.commit()
	db.close()
	
	
	
#（普私共用）这个函数根据医生开药信息更新问诊开药表
#innum是接诊单号，drugname是医生所开药名,usingmethod是使用方法
def decideDrugs(innum,drugname,usingmethod):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	cursor.execute('''UPDATE INQUIRYFORDRUG SET DRUGNAME = '{}' AND USINGMETHOD = '{}' AND INNUM = {}'''.format(drugname,usingmethod,innum))

	cursor.close()
	db.commit()
	db.close()

#这个函数是根据私人医生的饮食建议更新问诊表
#innum是接诊单号,breakfast是早餐建议，lunch是午餐建议，dinner是晚餐建议
def decideFood(innum,breakfast,lunch,dinner):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	cursor.execute('''UPDATE INQUIRY SET BREAKFAST = '{}' AND LUNCH = '{}' AND DINNER = '{}' WHERE INNUM = {}'''.format(breakfast,lunch,dinner,innum))
    
	cursor.close()
	db.commit()
	db.close()
	
#（普私共用）这个函数将“是否完成诊断”更新为TRUE
#innum是接诊单号
def setDoneToTrue(innum):
	db = MySQLdb.connect("52.15.135.11","root","rootsql","doctor",charset="utf8")
	cursor = db.cursor()

	cursor.execute('''UPDATE INQUIRY SET DONE = TRUE WHERE INNUM = {}'''.format(innum))
    
	cursor.close()
	db.commit()
	db.close()


if __name__ == '__main__':

#test part1 : insert inquiry
	# commit_question("陈金坤","发烧，流鼻涕",imagepath="./test.jpg")
	# commit_question("费永寿","胃痛",imagepath="./test1.jpg")
	# commit_question("乐正兴修","心绞痛")
	# commit_question("何鸿雪","疑似骨折了",department="骨科")
	# commit_question("陈金坤","还是发烧，还是流鼻涕",False,department="内科")
	# commit_question("张泽森","失眠，日渐消瘦",toprivatedoc=True)
	# commit_question("费永寿","头晕，全身无力")
	# commit_question("康安怡","轻微抑郁")
	# commit_question("何鸿雪","上次用了加速骨头愈合的药，过敏了",imagepath="./guoming.jpg")
	# commit_question("陈金坤","发烧，流鼻涕,之前的庸医太垃圾了治不好",toprivatedoc=True,imagepath="./test.jpg")
	# commit_question("俞和泰","就想问问有没有长生不老药")

	# selectAllNoClass()

	selectUserHistory('陈金坤')