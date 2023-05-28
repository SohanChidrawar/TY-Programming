from random import choice
from experta import *

class Disease(Fact):
	"""
	Allergies - sneezing, blocked nose, watery eyes, red eyes, coughing, red rash
	Asthma - wheezing, shortness of breath, a tight chest
	Head Tumor - severe headaches, seizures, mental changes, vision problem
	Chronic pain - diabetes, arthritis, back pain
	Dehydration - feeling thirsty, a dry mouth, tiredness, strong smelling urine
	Food Poisoning - nausea, vomiting, weakness, loss of appetite, aching muscles, chills
	"""
	pass
	
	
class Patient(KnowledgeEngine):
	
	Allergies = ['sneezing', 'blocked nose', 'watery eyes', 'red eyes', 'coughing', 'red rash']
	Asthma = ['wheezing', 'shortness of breath', 'tight chest']
	Head_Tumor = ['severe headaches', 'seizures', 'mental changes', 'vision problem']
	Chronic_Pain = ['diabetes', 'arthritis', 'back pain']
	Dehydration = ['feeling thirsty', 'dry mouth', 'tiredness', 'strong smelling urine']
	Food_Poisoning = ['nausea', 'vomiting', 'weakness', 'loss of appetite', 'aching muscles', 'chills']	
	
	@Rule(Disease(symptoms=Allergies))
	def allrg(self):
		print("You have Allergies")
	
	@Rule(Disease(symptoms=Asthma))
	def asma(self):
		print("You have Asthma")
		
	@Rule(Disease(symptoms=Head_Tumor))
	def heat_t(self):
		print("You have Head Tumor")
		
	@Rule(Disease(symptoms=Chronic_Pain))
	def chr_pain(self):
		print("You have Chronic Pain")
		
	@Rule(Disease(symptoms=Dehydration))
	def dehydra(self):
		print("You have Dehydration")
		
	@Rule(Disease(symptoms=Food_Poisoning))
	def fod_poi(self):
		print("You have Food Poisoning")



Allergies = ['sneezing', 'blocked nose', 'watery eyes', 'red eyes', 'coughing', 'red rash']
Asthma = ['wheezing', 'shortness of breath', 'tight chest']
Head_Tumor = ['severe headaches', 'seizures', 'mental changes', 'vision problem']
Chronic_Pain = ['diabetes', 'arthritis', 'back pain']
Dehydration = ['feeling thirsty', 'dry mouth', 'tiredness', 'strong smelling urine']
Food_Poisoning = ['nausea', 'vomiting', 'weakness', 'loss of appetite', 'aching muscles', 'chills']	


engine = Patient()
engine.reset()
#random_choice = choice([Allergies, Asthma, Head_Tumor, Chronic_Pain, Dehydration, Food_Poisoning])
symps = []
count_symps = int(input("How many symptoms you have: "))

for i in range(count_symps):
	get_symps = input("Enter symptom: ")
	symps.append(get_symps.lower())

#print("\nSelected Symptoms are is {}\n".format(random_choice))
print("According to your symptoms you have: ")
engine.declare(Disease(symptoms=symps))
engine.run()
