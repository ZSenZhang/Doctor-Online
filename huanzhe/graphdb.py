from py2neo import Graph,Node,Relationship

def insertSympAndDisease(symptom_name,disease_name):
	graph=Graph(host="52.15.135.11",username="neo4j",password="rootneo4j")

	#test if the symptom exist
	symptom = graph.run("MATCH (a) WHERE a.name={x} AND a.label={y} RETURN *", x=symptom_name,y="Symptom").evaluate()
	if symptom == None:
		symptom = Node(label="Symptom", name=symptom_name)
		graph.create(symptom)

	#test if the disease exist
	disease = graph.run("MATCH (a) WHERE a.name={x} AND a.label={y} RETURN *", x=disease_name,y="Disease").evaluate()
	if disease == None:
		disease = Node(label="Disease", name=disease_name)
		graph.create(disease)

	symptom2disease = graph.match_one(start_node=symptom, end_node=disease)
	if symptom2disease == None:
		symptom2disease = Relationship(symptom,"CALL",disease)
		symptom2disease['count'] = 1
		graph.create(symptom2disease)
	else:
		symptom2disease['count'] += 1
		graph.push(symptom2disease)

def insertDiseaseAndDrug(disease_name,drug_name):
	graph=Graph(host="52.15.135.11",username="neo4j",password="rootneo4j")

	#test if the disease exist
	disease = graph.run("MATCH (a) WHERE a.name={x} AND a.label={y} RETURN *", x=disease_name,y="Disease").evaluate()
	if disease == None:
		disease = Node(label="Disease", name=disease_name)
		graph.create(disease)

	#test if the drug exist
	drug = graph.run("MATCH (a) WHERE a.name={x} AND a.label={y} RETURN *", x=drug_name,y="Drug").evaluate()
	if drug == None:
		drug = Node(label="Drug", name=drug_name)
		graph.create(drug)

	disease2drug = graph.match_one(start_node=disease, end_node=drug)
	if disease2drug == None:
		disease2drug = Relationship(disease,"CALL",drug)
		disease2drug['count'] = 1
		graph.create(disease2drug)
	else:
		disease2drug['count'] += 1
		graph.push(disease2drug)

#search the drug for a diseases
#the type of disease_name should be string
def search_drug(disease_name):
	graph=Graph(host="52.15.135.11",username="neo4j",password="rootneo4j")

	disease = graph.run("MATCH (a) WHERE a.name={x} AND a.label={y} RETURN *", x=disease_name,y="Disease").evaluate()
	if disease == None:
		print("There is no such disease")
		### add some action to deal with the error, use return now
		return

	match_relation = graph.match(start_node=disease)
	drug_list=[]
	for i in match_relation:
		drug_name = i.end_node()["name"]
		count = i["count"]
		drug_list.append({"name":drug_name, "use_time":count})

	drug_list_sort_by_count = sorted(drug_list, key=lambda e:e.__getitem__("use_time"), reverse=True)
	print("The most probobal drugs for {}: (Sorted by the using frequency from high to low)".format(disease_name))
	for drug in drug_list_sort_by_count:
		print(drug["name"])

	return drug_list_sort_by_count

#search the most probobal disease for the symptoms
#the input type should be a list
def search_disease_and_drug(symptom_list):
	graph=Graph(host="52.15.135.11",username="neo4j",password="rootneo4j")

	disease_list_total = []

	for symptom_name in symptom_list:
		symptom = graph.run("MATCH (a) WHERE a.name={x} AND a.label={y} RETURN *", x=symptom_name,y="Symptom").evaluate()
		if symptom == None:
			print("There is no such disease")
			### add some action to deal with the error, use continue now
			continue

		match_relation = graph.match(start_node=symptom)
		disease_list = []
		for i in match_relation:
			disease_name = i.end_node()["name"]
			count = i["count"]
			disease_list.append({"name":disease_name, "use_time":count})

		disease_list_sort_by_count = sorted(disease_list, key=lambda e:e.__getitem__("use_time"), reverse=True)

		n = 0
		for dis in disease_list_sort_by_count:
			disease_list_total.append(dis["name"])
			n += 1
			if n == 3:##could be larger
				break

	final_disease_dict = {}

	for item in disease_list_total:
		final_disease_dict.update({item:disease_list_total.count(item)})

	disease_final_sort = sorted(final_disease_dict.items(), key=lambda d: d[1], reverse=True)
	print(disease_final_sort)

	prob_rank = 1
	for (dis,val) in disease_final_sort:
		print("The probability disease rank {}: {}".format(prob_rank,dis))
		most_prob = dis
		break

	drug_list = search_drug(most_prob)
	return most_prob,drug_list
		

if __name__ == '__main__':
	graph=Graph(host="52.15.135.11",username="neo4j",password="rootneo4j")
	graph.delete_all()

	#[(a,d),A,(001,002)] * 5
	for n in range(5):
		insertSympAndDisease("发烧","胃炎")
		insertSympAndDisease("胃疼","胃炎")
		insertDiseaseAndDrug("胃炎","肠胃康")
		insertDiseaseAndDrug("胃炎","阿莫西林")

	#[d,A,002] * 2
	for n in range(2):
		insertSympAndDisease("胃疼","胃炎")
		insertDiseaseAndDrug("胃炎","阿莫西林")

	#[(a,b,c),B,(001,003,004)] * 10
	for n in range(10):
		insertSympAndDisease("发烧","感冒")
		insertSympAndDisease("流鼻涕","感冒")
		insertSympAndDisease("咳嗽","感冒")
		insertDiseaseAndDrug("感冒","阿莫西林")
		insertDiseaseAndDrug("感冒","感冒灵")
		insertDiseaseAndDrug("感冒","一清颗粒")

	#[(c,e),C,(004,005)] * 3
	for n in range(3):
		insertSympAndDisease("咳嗽","肺炎")
		insertSympAndDisease("呼吸困难","肺炎")
		insertDiseaseAndDrug("肺炎","急支糖浆")
		insertDiseaseAndDrug("肺炎","蛇胆川贝枇杷膏")

	#[(a,c,e),C,(001,005)] * 8
	for n in range(8):
		insertSympAndDisease("发烧","肺炎")
		insertSympAndDisease("咳嗽","肺炎")
		insertSympAndDisease("呼吸困难","肺炎")
		insertDiseaseAndDrug("肺炎","阿莫西林")
		insertDiseaseAndDrug("肺炎","蛇胆川贝枇杷膏")

	# search_drug("B")
	search_disease_and_drug(["发烧","流鼻涕"])

	print("insert done!")


