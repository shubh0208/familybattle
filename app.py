from bs4 import BeautifulSoup
import requests	
import pandas as pd
import numpy as np
from flask import Flask, render_template, url_for

#Family Game
app = Flask(__name__) 
  
@app.route('/') 
 
def hello_world():
	# FAMILY BATTLE
	team1_bat=["Rishabh Pant","Jasprit Bumrah","Suresh Raina","Andre Russell","Mohammad Shami",
			   "Ishan Kishan","Jos Buttler","Prithvi Shaw","T Natarajan","Mohammed Siraj",
			   "Kieron Pollard","Vijay Shankar","Pat Cummins"]
	team1_bowl=team1_bat

	team2_bat=["Rashid Khan","Rohit Sharma","Jofra Archer","Krunal Pandya","Chris Morris",
			   "Deepak Chahar","Rahul Chahar","Jonny Bairstow","Shardul Thakur","Navdeep Saini",
			   "Riley Meredith","Prasidh Krishna","Dinesh Karthik"]
	team2_bowl=team2_bat
	
	team3_bat=["Virat Kohli","KL Rahul","Suryakumar Yadav","Ben Stokes","Manish Pandey",
			   "Quinton de Kock","Varun Chakaravarthy","Trent Boult","Sanju Samson","Marcus Stoinis",
			   "Sandeep Sharma","Eoin Morgan","Ruturaj Gaikwad"]
	team3_bowl=team3_bat
	
	team4_bat=["David Warner","Shikhar Dhawan","Yuzvendra Chahal","Kagiso Rabada","Mayank Agarwal",
			   "Shubman Gill","Sam Curran","Nitish Rana","Shreyas Gopal","Axar Patel",
			   "Faf du Plessis","David Malan","Rahul Tewatia"]
	team4_bowl=team4_bat

	team5_bat=["Hardik Pandya", "Glenn Maxwell","Bhuvneshwar Kumar","AB de Villiers","Ravichandran Ashwin",
			   "Sunil Narine","Ravindra Jadeja","Devdutt Padikkal","Moeen Ali","Washington Sundar",
			   "Ambati Rayudu","Chris Gayle","MS Dhoni"]
	team5_bowl=team5_bat

	# KARAN KAVIN
	team6_bat=["Virat Kohli","Rohit Sharma","Jasprit Bumrah","Trent Boult","Shubman Gill",
			   "Rashid Khan","Jos Buttler","AB de Villiers","Chris Morris","Rishabh Pant",
			   "Mohammad Shami","Shikhar Dhawan","Suresh Raina","Glenn Maxwell","Yuzvendra Chahal",
			   "Hardik Pandya","Sanju Samson","Ravindra Jadeja","Nitish Rana","Ravichandran Ashwin",
			   "Eoin Morgan","Deepak Chahar","Prithvi Shaw","Shakib Al Hasan","Navdeep Saini",
			   "Jonny Bairstow","Dwayne Bravo","Steve Smith"]

	team6_bowl=team6_bat
	team6_bonus=["Virat Kohli","Jasprit Bumrah","Rohit Sharma","Rashid Khan"]
	Bonus_team6_dict={"Virat Kohli":0,"Rohit Sharma":0,"Jasprit Bumrah":0,"Rashid Khan":0}

	team7_bat=["Ben Stokes", "KL Rahul","David Warner","Kagiso Rabada","Suryakumar Yadav",
			   "Anrich Nortje","Mayank Agarwal","Faf du Plessis","Marcus Stoinis","Bhuvneshwar Kumar",
			   "Andre Russell","Sam Curran","Shardul Thakur","T Natarajan","Devdutt Padikkal",
			   "Quinton de Kock","Pat Cummins","Varun Chakaravarthy","Rahul Chahar","Manish Pandey",
			   "Dan Christian","Axar Patel","Rahul Tewatia","Mohammed Siraj","Ishan Kishan",
			   "Kane Williamson","Nicholas Pooran","Jhye Richardson"]
	team7_bowl=team7_bat
	team7_bonus=["David Warner","Ben Stokes","Kagiso Rabada","KL Rahul"]
	Bonus_team7_dict={"David Warner":0,"Ben Stokes":0,"Kagiso Rabada":0,"KL Rahul":0}

	# AMISH FRIENDS
	team8_bat=["KL Rahul", "Ishan Kishan","Devdutt Padikkal","Suresh Raina","Shubman Gill",
			   "Prithvi Shaw","Manish Pandey","Hardik Pandya","Ben Stokes","Kieron Pollard",
			   "Bhuvneshwar Kumar","Yuzvendra Chahal","Varun Chakaravarthy","Pat Cummins","Trent Boult"]
	team8_bowl=team8_bat

	team9_bat=["AB de Villiers","Jos Buttler","Rohit Sharma","Shikhar Dhawan","Ambati Rayudu",
			   "Ruturaj Gaikwad","Eoin Morgan","Chris Morris","Marcus Stoinis","Rahul Tewatia",
			   "Jasprit Bumrah","Mohammad Shami","Shardul Thakur","T Natarajan","Sunil Narine"]
	team9_bowl=team9_bat
	
	team10_bat=["Quinton de Kock", "MS Dhoni","Virat Kohli","Mayank Agarwal","Faf du Plessis",
			   "Rahul Tripathi","Priyam Garg","Andre Russell","Jason Holder","Ravindra Jadeja",
			   "Anrich Nortje","Mohammed Siraj","Sandeep Sharma","Ravi Bishnoi","Deepak Chahar"]
	team10_bowl=team10_bat

	team11_bat=["Rishabh Pant","Sanju Samson","David Warner","Suryakumar Yadav","David Malan",
			   "Nitish Rana","Riyan Parag","Glenn Maxwell","Sam Curran","Krunal Pandya",
			   "Rashid Khan","Kagiso Rabada","Navdeep Saini","Rahul Chahar","Harbhajan Singh"]
	team11_bowl=team11_bat

	#KARAN 2
	team12_bat=["Faf du Plessis","Suresh Raina","Dwayne Bravo","Anrich Nortje","Rishabh Pant",
			   "Ravichandran Ashwin","Shakib Al Hasan","Varun Chakaravarthy","Nitish Rana","Eoin Morgan",
			   "Trent Boult","Quinton de Kock","Rohit Sharma","Ishan Kishan","Hardik Pandya",
			   "KL Rahul","Nicholas Pooran","Ravi Bishnoi","AB de Villiers","Glenn Maxwell",
			   "Yuzvendra Chahal","Ben Stokes","Chris Morris","Jos Buttler","Rahul Tewatia",
			   "Rashid Khan","T Natarajan","Sandeep Sharma"]
	team12_bowl=team12_bat

	team13_bat =["Ravichandran Jadeja", "Shardul Thakur","Sam Curran","Kagiso Rabada","Marcus Stoinis",
			     "Shikhar Dhawan","Axar Patel","Prithvi Shaw","Shubman Gill","Pat Cummins",
			     "Prasidh Krishna","Andre Russell","Jasprit Bumrah","Suryakumar Yadav","Rahul Chahar",
			     "Mayank Agarwal","Mohammad Shami","Jhye Richardson","Virat Kohli","Mohammed Siraj",
			     "Devdutt Padikkal","Sanju Samson","Shreyas Gopal","David Warner","Bhuvneshwar Kumar",
			     "Manish Pandey","Kane Williamson"]
	team13_bowl=team13_bat

	# ["", "","","","",
	# 		   "","","","","",
	# 		   "","","","",""]


	source = requests.get("https://www.iplt20.com/stats/2021/most-runs").text
	soup=BeautifulSoup(source,'lxml')

	source2=requests.get("https://www.iplt20.com/stats/2021/most-wickets").text
	soup2=BeautifulSoup(source2,'lxml')

	

	PL=[]
	PR=[]
	batsman={}
	batsman_list=[]
	player_name_list=[]
	player_name1=""
	player_runs_list=[]
	player_runs1=""
	PL2=[]
	PW=[]
	bowler={}
	bowler_list=[]
	player_name_list2=[]
	player_name2=""
	player_wickets_list=[]
	player_wicket1=""
	bat_match1=""
	bat_match_list=[]
	bowl_match1=""
	bowl_match_list=[]

	runs_table=soup.find("table",class_="top-players")
	wicket_table=soup2.find("table",class_="top-players")

	for rt in runs_table.find_all("tr",class_="js-row"):
		player_name=rt.find("div",class_="top-players__player-name").a.text
		player_name_list=player_name.split('\n')
		player_name1=player_name_list[1].strip()+" "+player_name_list[2].strip()
		player_runs=rt.find("td",class_="top-players__r").text
		player_runs_list=player_runs.split("\n")
		player_runs1=int(player_runs_list[1].strip())
		bat_match=rt.find("td",class_="top-players__m").text
		bat_match_list=bat_match.split("\n")
		bat_match1=int(bat_match_list[1].strip())
		batsman={"Player":player_name1,"Matches":bat_match1,"Runs":player_runs1}
		batsman_list.append(batsman)
		PL.append(player_name1)
		PR.append(player_runs1)
		

	for rt in wicket_table.find_all("tr",class_="js-row"):
		player_name2=rt.find("div",class_="top-players__player-name").a.text
		player_name_list2=player_name2.split('\n')
		player_name2=player_name_list2[1].strip()+" "+player_name_list2[2].strip()
		player_wickets=rt.find("td",class_="top-players__w").text
		player_wickets_list=player_wickets.split("\n")
		player_wickets1=int(player_wickets_list[1].strip())
		bowl_match=rt.find("td",class_="top-players__m").text
		bowl_match_list=bowl_match.split("\n")
		bowl_match1=int(bowl_match_list[1].strip())
		bowler={"PLAYER":player_name2,"Matches":bowl_match1,"Wkts":player_wickets1}
		bowler_list.append(bowler)
		PL2.append(player_name2)
		PW.append(player_wickets1)

	data_bowl=pd.DataFrame(bowler_list)
	data_bowl=data_bowl[["PLAYER","Matches","Wkts"]]

	file=pd.DataFrame(batsman_list)
	file=file[["Player","Matches","Runs"]]

# FAMILY BATTLE
# Start Team1
	team1_bat_point=[]
	team1_bowl_point=[]
	team1_bat_data=file.loc[file["Player"].isin(team1_bat),["Player","Matches","Runs"]]
	team1_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team1_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team1_bowl_data:
	    team1_bowl_point.append(25*team1_bowl_data["Wkts"])
	    y.append(team1_bowl_data["Wkts"])
	team1_bowl_data.insert(2,"Points",team1_bowl_point[0],True)
	a=0
	for i in team1_bat_data:
	    team1_bat_point.append(team1_bat_data["Runs"])
	#for i in range(len(team1_bat_point)):
		 #a=a+int(team1_bat_point[i])
	team1_bat_data.insert(3, "Points", team1_bat_point[0], True)
	team1_bat_TRP=(sum(team1_bat_point[0]))
	team1_bowl_TWP=(sum(team1_bowl_point[0]))
	team1_total_points=team1_bat_TRP+team1_bowl_TWP
	team1_bat_point={"Player":"Total","Matches":"","Runs":team1_bat_TRP,"Points":team1_bat_TRP}
	team1_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team1_bowl_TWP}
	team1_bat_data=team1_bat_data.append(team1_bat_point,ignore_index=True,sort=False)	
	team1_bowl_data=team1_bowl_data.append(team1_bowl_point,ignore_index=True,sort=False)
	print(team1_bowl_data)
	print("\n")
	print(team1_bat_data)
	print("\n")
	print(team1_bat_TRP,team1_bowl_TWP,team1_total_points)
	team1_BatFinal={}
	team1_BowlFinal={}
	team1_BatFinal["Players"]=team1_bat_data["Player"]
	team1_BatFinal["Runs"]=team1_bat_data["Runs"]
	team1_BatFinal["Points"]=team1_bat_data["Points"]
	team1_BatFinal["Matches"]=team1_bat_data["Matches"]
	team1_BowlFinal["Players"]=team1_bowl_data["PLAYER"]
	team1_BowlFinal["Wickets"]=team1_bowl_data["Wkts"]
	team1_BowlFinal["Points"]=team1_bowl_data["Points"]
	team1_BowlFinal["Matches"]=team1_bowl_data["Matches"]
	#print(team1_BatFinal)
	#print("\n")
	#print(team1_BowlFinal)
	#End Team1


	# Start Team2
	team2_bat_point=[]
	team2_bowl_point=[]
	team2_bat_data=file.loc[file["Player"].isin(team2_bat),["Player","Matches","Runs"]]
	team2_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team2_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team2_bowl_data:
	    team2_bowl_point.append(25*team2_bowl_data["Wkts"])
	    y.append(team2_bowl_data["Wkts"])
	team2_bowl_data.insert(2,"Points",team2_bowl_point[0],True)
	a=0
	for i in team2_bat_data:
	    team2_bat_point.append(team2_bat_data["Runs"])
	for i in range(len(team2_bat_point)):
	    a=a+team2_bat_point[i]
	team2_bat_data.insert(2, "Points", team2_bat_point[0], True)
	team2_bat_TRP=(sum(team2_bat_point[0]))
	team2_bowl_TWP=(sum(team2_bowl_point[0]))
	team2_total_points=team2_bat_TRP+team2_bowl_TWP
	team2_bat_point={"Player":"Total","Matches":"","Runs":team2_bat_TRP,"Points":team2_bat_TRP}
	team2_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team2_bowl_TWP}
	team2_bat_data=team2_bat_data.append(team2_bat_point,ignore_index=True,sort=False)
	team2_bowl_data=team2_bowl_data.append(team2_bowl_point,ignore_index=True,sort=False)
	
	print(team2_bat_TRP,team2_bowl_TWP,team2_total_points)
	team2_BatFinal={}
	team2_BowlFinal={}
	team2_BatFinal["Players"]=team2_bat_data["Player"]
	team2_BatFinal["Runs"]=team2_bat_data["Runs"]
	team2_BatFinal["Points"]=team2_bat_data["Points"]
	team2_BatFinal["Matches"]=team2_bat_data["Matches"]
	team2_BowlFinal["Players"]=team2_bowl_data["PLAYER"]
	team2_BowlFinal["Wickets"]=team2_bowl_data["Wkts"]
	team2_BowlFinal["Points"]=team2_bowl_data["Points"]
	team2_BowlFinal["Matches"]=team2_bowl_data["Matches"]

	

	#End Team2



	# Start Team3
	team3_bat_point=[]
	team3_bowl_point=[]
	team3_bat_data=file.loc[file["Player"].isin(team3_bat),["Player","Matches","Runs"]]
	team3_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team3_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team3_bowl_data:
	    team3_bowl_point.append(25*team3_bowl_data["Wkts"])
	    y.append(team3_bowl_data["Wkts"])
	team3_bowl_data.insert(2,"Points",team3_bowl_point[0],True)
	a=0
	for i in team3_bat_data:
	    team3_bat_point.append(team3_bat_data["Runs"])
	for i in range(len(team3_bat_point)):
	    a=a+team3_bat_point[i]
	team3_bat_data.insert(2, "Points", team3_bat_point[0], True)
	team3_bat_TRP=(sum(team3_bat_point[0]))
	team3_bowl_TWP=(sum(team3_bowl_point[0]))
	team3_total_points=team3_bat_TRP+team3_bowl_TWP
	team3_bat_point={"Player":"Total","Matches":"","Runs":team3_bat_TRP,"Points":team3_bat_TRP}
	team3_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team3_bowl_TWP}
	team3_bat_data=team3_bat_data.append(team3_bat_point,ignore_index=True,sort=False)
	team3_bowl_data=team3_bowl_data.append(team3_bowl_point,ignore_index=True,sort=False)
	
	team3_BatFinal={}
	team3_BowlFinal={}
	team3_BatFinal["Players"]=team3_bat_data["Player"]
	team3_BatFinal["Runs"]=team3_bat_data["Runs"]
	team3_BatFinal["Points"]=team3_bat_data["Points"]
	team3_BatFinal["Matches"]=team3_bat_data["Matches"]
	team3_BowlFinal["Players"]=team3_bowl_data["PLAYER"]
	team3_BowlFinal["Wickets"]=team3_bowl_data["Wkts"]
	team3_BowlFinal["Points"]=team3_bowl_data["Points"]
	team3_BowlFinal["Matches"]=team3_bowl_data["Matches"]



	#End Team3


	# Start Team4
	team4_bat_point=[]
	team4_bowl_point=[]
	team4_bat_data=file.loc[file["Player"].isin(team4_bat),["Player","Matches","Runs"]]
	team4_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team4_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team4_bowl_data:
	    team4_bowl_point.append(25*team4_bowl_data["Wkts"])
	    y.append(team4_bowl_data["Wkts"])
	team4_bowl_data.insert(2,"Points",team4_bowl_point[0],True)
	a=0
	for i in team4_bat_data:
	    team4_bat_point.append(team4_bat_data["Runs"])
	for i in range(len(team4_bat_point)):
	    a=a+team4_bat_point[i]
	team4_bat_data.insert(2, "Points", team4_bat_point[0], True)
	team4_bat_TRP=(sum(team4_bat_point[0]))
	team4_bowl_TWP=(sum(team4_bowl_point[0]))
	team4_total_points=team4_bat_TRP+team4_bowl_TWP
	team4_bat_point={"Player":"Total","Matches":"","Runs":team4_bat_TRP,"Points":team4_bat_TRP}
	team4_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team4_bowl_TWP}
	team4_bat_data=team4_bat_data.append(team4_bat_point,ignore_index=True,sort=False)
	team4_bowl_data=team4_bowl_data.append(team4_bowl_point,ignore_index=True,sort=False)
	print(team4_bowl_data)
	print("\n")
	print(team4_bat_data)
	print("\n")
	print(team4_bat_TRP,team4_bowl_TWP,team4_total_points)
	team4_BatFinal={}
	team4_BowlFinal={}
	team4_BatFinal["Players"]=team4_bat_data["Player"]
	team4_BatFinal["Runs"]=team4_bat_data["Runs"]
	team4_BatFinal["Points"]=team4_bat_data["Points"]
	team4_BatFinal["Matches"]=team4_bat_data["Matches"]
	team4_BowlFinal["Players"]=team4_bowl_data["PLAYER"]
	team4_BowlFinal["Wickets"]=team4_bowl_data["Wkts"]
	team4_BowlFinal["Points"]=team4_bowl_data["Points"]
	team4_BowlFinal["Matches"]=team4_bowl_data["Matches"]

	print(team4_BatFinal)
	print("\n")
	print(team4_BowlFinal)
	#End Team4

	# Start Team5
	team5_bat_point=[]
	team5_bowl_point=[]
	team5_bat_data=file.loc[file["Player"].isin(team5_bat),["Player","Matches","Runs"]]
	team5_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team5_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team5_bowl_data:
	    team5_bowl_point.append(25*team5_bowl_data["Wkts"])
	    y.append(team5_bowl_data["Wkts"])
	team5_bowl_data.insert(2,"Points",team5_bowl_point[0],True)
	a=0
	for i in team5_bat_data:
	    team5_bat_point.append(team5_bat_data["Runs"])
	#for i in range(len(team1_bat_point)):
		 #a=a+int(team1_bat_point[i])
	team5_bat_data.insert(2, "Points", team5_bat_point[0], True)
	team5_bat_TRP=(sum(team5_bat_point[0]))
	team5_bowl_TWP=(sum(team5_bowl_point[0]))
	team5_total_points=team5_bat_TRP+team5_bowl_TWP
	team5_bat_point={"Player":"Total","Matches":"","Runs":team5_bat_TRP,"Points":team5_bat_TRP}
	team5_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team5_bowl_TWP}
	team5_bat_data=team5_bat_data.append(team5_bat_point,ignore_index=True,sort=False)	
	team5_bowl_data=team5_bowl_data.append(team5_bowl_point,ignore_index=True,sort=False)
	print(team5_bowl_data)
	print("\n")
	print(team5_bat_data)
	print("\n")
	print(team5_bat_TRP,team5_bowl_TWP,team5_total_points)
	team5_BatFinal={}
	team5_BowlFinal={}
	team5_BatFinal["Players"]=team5_bat_data["Player"]
	team5_BatFinal["Runs"]=team5_bat_data["Runs"]
	team5_BatFinal["Points"]=team5_bat_data["Points"]
	team5_BatFinal["Matches"]=team5_bat_data["Matches"]
	team5_BowlFinal["Players"]=team5_bowl_data["PLAYER"]
	team5_BowlFinal["Wickets"]=team5_bowl_data["Wkts"]
	team5_BowlFinal["Points"]=team5_bowl_data["Points"]
	team5_BowlFinal["Matches"]=team5_bowl_data["Matches"]

	print(team5_BatFinal)
	print("\n")
	print(team5_BowlFinal)
	#End Team5

# KARAN KAVIN
	# Start team6
	team6_bat_point=[]
	team6_bowl_point=[]
	Bonus_team6_data=[]
	team6_bat_data=file.loc[file["Player"].isin(team6_bat),["Player","Matches","Runs"]]
	Bonus_team6_DF1=pd.DataFrame(team6_bat_data)
	team6_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team6_bowl),["PLAYER","Matches","Wkts"]]
	Bonus_team6_DF2=pd.DataFrame(team6_bowl_data)
	for key in Bonus_team6_dict:
		for i in Bonus_team6_DF1.index:
			if (Bonus_team6_DF1["Player"][i]==key):
				Bonus_team6_dict[key]=Bonus_team6_dict[key]+int(Bonus_team6_DF1["Runs"][i])
		for j in Bonus_team6_DF2.index:
			if (Bonus_team6_DF2["PLAYER"][j]==key):
				Bonus_team6_dict[key]=Bonus_team6_dict[key]+int(Bonus_team6_DF2["Wkts"][j])*25
	
	Bonus_team6_tuples=[("Virat Kohli",Bonus_team6_dict["Virat Kohli"]),("Rohit Sharma",Bonus_team6_dict["Rohit Sharma"]),("Jasprit Bumrah",Bonus_team6_dict["Jasprit Bumrah"]),("Rashid Khan",Bonus_team6_dict["Rashid Khan"])]
	#for key in Bonus_team6_dict:
	#	Bonus_team6_tuples.append((key,Bonus_team6_dict[key]))
	Bonus_team6_tuples.sort(key = lambda x: x[1], reverse=True)	
			
	y=0
	for i in Bonus_team6_DF2.index:
		y=y+int(Bonus_team6_DF2["Wkts"][i])
		if (Bonus_team6_tuples[0][0]==Bonus_team6_DF2["PLAYER"][i]):
			team6_bowl_point.append(50*Bonus_team6_DF2["Wkts"][i])
		elif Bonus_team6_tuples[1][0]==Bonus_team6_DF2["PLAYER"][i]:
			team6_bowl_point.append(37.5*Bonus_team6_DF2["Wkts"][i])
		else:
			team6_bowl_point.append(25*Bonus_team6_DF2["Wkts"][i])	
	   # y=y+int(Bonus_team6_DF2["Wkts"][i])

	team6_bowl_data.insert(2,"Points",team6_bowl_point,True)
	a=0
	for i in Bonus_team6_DF1.index:
		if Bonus_team6_tuples[0][0]==Bonus_team6_DF1["Player"][i]:
			team6_bat_point.append(2*int(Bonus_team6_DF1["Runs"][i]))
		elif Bonus_team6_tuples[1][0]==Bonus_team6_DF1["Player"][i]:
			team6_bat_point.append(1.5*int(Bonus_team6_DF1["Runs"][i]))
		else:
			team6_bat_point.append(1*int(Bonus_team6_DF1["Runs"][i]))
		a=a+int(Bonus_team6_DF1["Runs"][i])



	   # team6_bat_point.append(team6_bat_data["Runs"])
	#for i in range(len(team6_bat_point)):
		 #a=a+int(team6_bat_point[i])
	team6_bat_data.insert(3, "Points", team6_bat_point, True)
	team6_bat_TRP=(sum(team6_bat_point))
	team6_bowl_TWP=(sum(team6_bowl_point))
	team6_total_points=team6_bat_TRP+team6_bowl_TWP
	team6_bat_point={"Player":"Total","Matches":"","Runs":a,"Points":team6_bat_TRP}
	team6_bowl_point={"PLAYER":"Total","Matches":"","Wkts":y,"Points":team6_bowl_TWP}
	team6_bat_data=team6_bat_data.append(team6_bat_point,ignore_index=True,sort=False)	
	team6_bowl_data=team6_bowl_data.append(team6_bowl_point,ignore_index=True,sort=False)
	print(team6_bowl_data)
	print("\n")
	print(team6_bat_data)
	print("\n")
	print(team6_bat_TRP,team6_bowl_TWP,team6_total_points)
	team6_BatFinal={}
	team6_BowlFinal={}
	team6_BatFinal["Players"]=team6_bat_data["Player"]
	team6_BatFinal["Runs"]=team6_bat_data["Runs"]
	team6_BatFinal["Points"]=team6_bat_data["Points"]
	team6_BatFinal["Matches"]=team6_bat_data["Matches"]
	team6_BowlFinal["Players"]=team6_bowl_data["PLAYER"]
	team6_BowlFinal["Wickets"]=team6_bowl_data["Wkts"]
	team6_BowlFinal["Points"]=team6_bowl_data["Points"]
	team6_BowlFinal["Matches"]=team6_bowl_data["Matches"]
	print(team6_BatFinal)
	print("\n")
	print(team6_BowlFinal)
	#End team6


	# Start team7
	team7_bat_point=[]
	team7_bowl_point=[]
	team7_bat_data=file.loc[file["Player"].isin(team7_bat),["Player","Matches","Runs"]]
	Bonus_team7_DF1=pd.DataFrame(team7_bat_data)
	team7_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team7_bowl),["PLAYER","Matches","Wkts"]]
	Bonus_team7_DF2=pd.DataFrame(team7_bowl_data)

	for key in Bonus_team7_dict:
			for i in Bonus_team7_DF1.index:
				if (Bonus_team7_DF1["Player"][i]==key):
					Bonus_team7_dict[key]=Bonus_team7_dict[key]+int(Bonus_team7_DF1["Runs"][i])
			for j in Bonus_team7_DF2.index:
				if (Bonus_team7_DF2["PLAYER"][j]==key):
					Bonus_team7_dict[key]=Bonus_team7_dict[key]+int(Bonus_team7_DF2["Wkts"][j])*25

	Bonus_team7_tuples=[("David Warner",Bonus_team7_dict["David Warner"]),("KL Rahul",Bonus_team7_dict["KL Rahul"]),("Kagiso Rabada",Bonus_team7_dict["Kagiso Rabada"]),("Ben Stokes",Bonus_team7_dict["Ben Stokes"])]
	#for key in Bonus_team6_dict:
	#	Bonus_team6_tuples.append((key,Bonus_team6_dict[key]))
	Bonus_team7_tuples.sort(key = lambda x: x[1], reverse=True)	

	y=0
	for i in Bonus_team7_DF2.index:
		y=y+int(Bonus_team7_DF2["Wkts"][i])
		if (Bonus_team7_tuples[0][0]==Bonus_team7_DF2["PLAYER"][i]):
			team7_bowl_point.append(50*Bonus_team7_DF2["Wkts"][i])
		elif Bonus_team7_tuples[1][0]==Bonus_team7_DF2["PLAYER"][i]:
			team7_bowl_point.append(37.5*Bonus_team7_DF2["Wkts"][i])
		else:
			team7_bowl_point.append(25*Bonus_team7_DF2["Wkts"][i])			
	    
	   # y.append(team6_bowl_data["Wkts"])
	team7_bowl_data.insert(2,"Points",team7_bowl_point,True)
	a=0
	for i in Bonus_team7_DF1.index:
		if Bonus_team7_tuples[0][0]==Bonus_team7_DF1["Player"][i]:
			 team7_bat_point.append(2*int(Bonus_team7_DF1["Runs"][i]))
		elif Bonus_team7_tuples[1][0]==Bonus_team7_DF1["Player"][i]:
			team7_bat_point.append(1.5*int(Bonus_team7_DF1["Runs"][i]))
		else:
			team7_bat_point.append(1*int(Bonus_team7_DF1["Runs"][i]))
		a=a+int(Bonus_team7_DF1["Runs"][i])



	  #  team7_bat_point.append(team7_bat_data["Runs"])
	#for i in range(len(team7_bat_point)):
	 #   a=a+team7_bat_point[i]

	team7_bat_data.insert(2, "Points", team7_bat_point, True)
	team7_bat_TRP=(sum(team7_bat_point))
	team7_bowl_TWP=(sum(team7_bowl_point))
	team7_total_points=team7_bat_TRP+team7_bowl_TWP
	team7_bat_point={"Player":"Total","Matches":"","Runs":a,"Points":team7_bat_TRP}
	team7_bowl_point={"PLAYER":"Total","Matches":"","Wkts":y,"Points":team7_bowl_TWP}
	team7_bat_data=team7_bat_data.append(team7_bat_point,ignore_index=True,sort=False)
	team7_bowl_data=team7_bowl_data.append(team7_bowl_point,ignore_index=True,sort=False)
	print(team7_bowl_data)
	print("\n")
	print(team7_bat_data)
	print("\n")
	print(team7_bat_TRP,team7_bowl_TWP,team7_total_points)
	team7_BatFinal={}
	team7_BowlFinal={}
	team7_BatFinal["Players"]=team7_bat_data["Player"]
	team7_BatFinal["Runs"]=team7_bat_data["Runs"]
	team7_BatFinal["Points"]=team7_bat_data["Points"]
	team7_BatFinal["Matches"]=team7_bat_data["Matches"]
	team7_BowlFinal["Players"]=team7_bowl_data["PLAYER"]
	team7_BowlFinal["Wickets"]=team7_bowl_data["Wkts"]
	team7_BowlFinal["Points"]=team7_bowl_data["Points"]
	team7_BowlFinal["Matches"]=team7_bowl_data["Matches"]

	print(team7_BatFinal)
	print("\n")
	print(team7_BowlFinal)

	#End team7

# AMISH FRIENDS
	# TEAM 8 - AMISH
	team8_bat_point=[]
	team8_bowl_point=[]
	team8_bat_data=file.loc[file["Player"].isin(team8_bat),["Player","Matches","Runs"]]
	team8_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team8_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team8_bowl_data:
	    team8_bowl_point.append(25*team8_bowl_data["Wkts"])
	    y.append(team8_bowl_data["Wkts"])
	team8_bowl_data.insert(2,"Points",team8_bowl_point[0],True)
	a=0
	for i in team8_bat_data:
	    team8_bat_point.append(team8_bat_data["Runs"])
	#for i in range(len(team1_bat_point)):
		 #a=a+int(team1_bat_point[i])
	team8_bat_data.insert(2, "Points", team8_bat_point[0], True)
	team8_bat_TRP=(sum(team8_bat_point[0]))
	team8_bowl_TWP=(sum(team8_bowl_point[0]))
	team8_total_points=team8_bat_TRP+team8_bowl_TWP
	team8_bat_point={"Player":"Total","Matches":"","Runs":team8_bat_TRP,"Points":team8_bat_TRP}
	team8_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team8_bowl_TWP}
	team8_bat_data=team8_bat_data.append(team8_bat_point,ignore_index=True,sort=False)	
	team8_bowl_data=team8_bowl_data.append(team8_bowl_point,ignore_index=True,sort=False)
	print(team8_bowl_data)
	print("\n")
	print(team8_bat_data)
	print("\n")
	print(team8_bat_TRP,team8_bowl_TWP,team8_total_points)
	team8_BatFinal={}
	team8_BowlFinal={}
	team8_BatFinal["Players"]=team8_bat_data["Player"]
	team8_BatFinal["Runs"]=team8_bat_data["Runs"]
	team8_BatFinal["Points"]=team8_bat_data["Points"]
	team8_BatFinal["Matches"]=team8_bat_data["Matches"]
	team8_BowlFinal["Players"]=team8_bowl_data["PLAYER"]
	team8_BowlFinal["Wickets"]=team8_bowl_data["Wkts"]
	team8_BowlFinal["Points"]=team8_bowl_data["Points"]
	team8_BowlFinal["Matches"]=team8_bowl_data["Matches"]

	print(team8_BatFinal)
	print("\n")
	print(team8_BowlFinal)

 	#TEAM 9 - KUSHAL

	team9_bat_point=[]
	team9_bowl_point=[]
	team9_bat_data=file.loc[file["Player"].isin(team9_bat),["Player","Matches","Runs"]]
	team9_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team9_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team9_bowl_data:
	    team9_bowl_point.append(25*team9_bowl_data["Wkts"])
	    y.append(team9_bowl_data["Wkts"])
	team9_bowl_data.insert(2,"Points",team9_bowl_point[0],True)
	a=0
	for i in team9_bat_data:
	    team9_bat_point.append(team9_bat_data["Runs"])
	#for i in range(len(team1_bat_point)):
		 #a=a+int(team1_bat_point[i])
	team9_bat_data.insert(2, "Points", team9_bat_point[0], True)
	team9_bat_TRP=(sum(team9_bat_point[0]))
	team9_bowl_TWP=(sum(team9_bowl_point[0]))
	team9_total_points=team9_bat_TRP+team9_bowl_TWP
	team9_bat_point={"Player":"Total","Matches":"","Runs":team9_bat_TRP,"Points":team9_bat_TRP}
	team9_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team9_bowl_TWP}
	team9_bat_data=team9_bat_data.append(team9_bat_point,ignore_index=True,sort=False)	
	team9_bowl_data=team9_bowl_data.append(team9_bowl_point,ignore_index=True,sort=False)
	print(team9_bowl_data)
	print("\n")
	print(team9_bat_data)
	print("\n")
	print(team9_bat_TRP,team9_bowl_TWP,team9_total_points)
	team9_BatFinal={}
	team9_BowlFinal={}
	team9_BatFinal["Players"]=team9_bat_data["Player"]
	team9_BatFinal["Runs"]=team9_bat_data["Runs"]
	team9_BatFinal["Points"]=team9_bat_data["Points"]
	team9_BatFinal["Matches"]=team9_bat_data["Matches"]
	team9_BowlFinal["Players"]=team9_bowl_data["PLAYER"]
	team9_BowlFinal["Wickets"]=team9_bowl_data["Wkts"]
	team9_BowlFinal["Points"]=team9_bowl_data["Points"]
	team9_BowlFinal["Matches"]=team9_bowl_data["Matches"]

	print(team9_BatFinal)
	print("\n")
	print(team9_BowlFinal)


 	#TEAM 10 - JINAY
	team10_bat_point=[]
	team10_bowl_point=[]
	team10_bat_data=file.loc[file["Player"].isin(team10_bat),["Player","Matches","Runs"]]
	team10_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team10_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team10_bowl_data:
	    team10_bowl_point.append(25*team10_bowl_data["Wkts"])
	    y.append(team10_bowl_data["Wkts"])
	team10_bowl_data.insert(2,"Points",team10_bowl_point[0],True)
	a=0
	for i in team10_bat_data:
	    team10_bat_point.append(team10_bat_data["Runs"])
	#for i in range(len(team1_bat_point)):
		 #a=a+int(team1_bat_point[i])
	team10_bat_data.insert(2, "Points", team10_bat_point[0], True)
	team10_bat_TRP=(sum(team10_bat_point[0]))
	team10_bowl_TWP=(sum(team10_bowl_point[0]))
	team10_total_points=team10_bat_TRP+team10_bowl_TWP
	team10_bat_point={"Player":"Total","Matches":"","Runs":team10_bat_TRP,"Points":team10_bat_TRP}
	team10_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team10_bowl_TWP}
	team10_bat_data=team10_bat_data.append(team10_bat_point,ignore_index=True,sort=False)	
	team10_bowl_data=team10_bowl_data.append(team10_bowl_point,ignore_index=True,sort=False)
	print(team10_bowl_data)
	print("\n")
	print(team10_bat_data)
	print("\n")
	print(team10_bat_TRP,team10_bowl_TWP,team10_total_points)
	team10_BatFinal={}
	team10_BowlFinal={}
	team10_BatFinal["Players"]=team10_bat_data["Player"]
	team10_BatFinal["Runs"]=team10_bat_data["Runs"]
	team10_BatFinal["Points"]=team10_bat_data["Points"]
	team10_BatFinal["Matches"]=team10_bat_data["Matches"]
	team10_BowlFinal["Players"]=team10_bowl_data["PLAYER"]
	team10_BowlFinal["Wickets"]=team10_bowl_data["Wkts"]
	team10_BowlFinal["Points"]=team10_bowl_data["Points"]
	team10_BowlFinal["Matches"]=team10_bowl_data["Matches"]

	print(team10_BatFinal)
	print("\n")
	print(team10_BowlFinal)
 	



 	#TEAM 11 - DEEP

	team11_bat_point=[]
	team11_bowl_point=[]
	team11_bat_data=file.loc[file["Player"].isin(team11_bat),["Player","Matches","Runs"]]
	team11_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team11_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team11_bowl_data:
	    team11_bowl_point.append(25*team11_bowl_data["Wkts"])
	    y.append(team11_bowl_data["Wkts"])
	team11_bowl_data.insert(2,"Points",team11_bowl_point[0],True)
	a=0
	for i in team11_bat_data:
	    team11_bat_point.append(team11_bat_data["Runs"])
	#for i in range(len(team1_bat_point)):
		 #a=a+int(team1_bat_point[i])
	team11_bat_data.insert(2, "Points", team11_bat_point[0], True)
	team11_bat_TRP=(sum(team11_bat_point[0]))
	team11_bowl_TWP=(sum(team11_bowl_point[0]))
	team11_total_points=team11_bat_TRP+team11_bowl_TWP
	team11_bat_point={"Player":"Total","Matches":"","Runs":team11_bat_TRP,"Points":team11_bat_TRP}
	team11_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team11_bowl_TWP}
	team11_bat_data=team11_bat_data.append(team11_bat_point,ignore_index=True,sort=False)	
	team11_bowl_data=team11_bowl_data.append(team11_bowl_point,ignore_index=True,sort=False)
	print(team11_bowl_data)
	print("\n")
	print(team11_bat_data)
	print("\n")
	print(team11_bat_TRP,team11_bowl_TWP,team11_total_points)
	team11_BatFinal={}
	team11_BowlFinal={}
	team11_BatFinal["Players"]=team11_bat_data["Player"]
	team11_BatFinal["Runs"]=team11_bat_data["Runs"]
	team11_BatFinal["Points"]=team11_bat_data["Points"]
	team11_BatFinal["Matches"]=team11_bat_data["Matches"]
	team11_BowlFinal["Players"]=team11_bowl_data["PLAYER"]
	team11_BowlFinal["Wickets"]=team11_bowl_data["Wkts"]
	team11_BowlFinal["Points"]=team11_bowl_data["Points"]
	team11_BowlFinal["Matches"]=team11_bowl_data["Matches"]

	print(team11_BatFinal)
	print("\n")
	print(team11_BowlFinal)

	# Kavin - karan - maulik

	# Start Team12
	team12_bat_point=[]
	team12_bowl_point=[]
	team12_bat_data=file.loc[file["Player"].isin(team12_bat),["Player","Matches","Runs"]]
	team12_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team12_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team12_bowl_data:
	    team12_bowl_point.append(25*team12_bowl_data["Wkts"])
	    y.append(team12_bowl_data["Wkts"])
	team12_bowl_data.insert(2,"Points",team12_bowl_point[0],True)
	a=0
	for i in team12_bat_data:
	    team12_bat_point.append(team12_bat_data["Runs"])
	#for i in range(len(team12_bat_point)):
		 #a=a+int(team12_bat_point[i])
	team12_bat_data.insert(3, "Points", team12_bat_point[0], True)
	team12_bat_TRP=(sum(team12_bat_point[0]))
	team12_bowl_TWP=(sum(team12_bowl_point[0]))
	team12_total_points=team12_bat_TRP+team12_bowl_TWP
	team12_bat_point={"Player":"Total","Matches":"","Runs":team12_bat_TRP,"Points":team12_bat_TRP}
	team12_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team12_bowl_TWP}
	team12_bat_data=team12_bat_data.append(team12_bat_point,ignore_index=True,sort=False)	
	team12_bowl_data=team12_bowl_data.append(team12_bowl_point,ignore_index=True,sort=False)
	print(team12_bowl_data)
	print("\n")
	print(team12_bat_data)
	print("\n")
	print(team12_bat_TRP,team12_bowl_TWP,team12_total_points)
	team12_BatFinal={}
	team12_BowlFinal={}
	team12_BatFinal["Players"]=team12_bat_data["Player"]
	team12_BatFinal["Runs"]=team12_bat_data["Runs"]
	team12_BatFinal["Points"]=team12_bat_data["Points"]
	team12_BatFinal["Matches"]=team12_bat_data["Matches"]
	team12_BowlFinal["Players"]=team12_bowl_data["PLAYER"]
	team12_BowlFinal["Wickets"]=team12_bowl_data["Wkts"]
	team12_BowlFinal["Points"]=team12_bowl_data["Points"]
	team12_BowlFinal["Matches"]=team12_bowl_data["Matches"]

		# Start Team13
	team13_bat_point=[]
	team13_bowl_point=[]
	team13_bat_data=file.loc[file["Player"].isin(team13_bat),["Player","Matches","Runs"]]
	team13_bowl_data=data_bowl.loc[data_bowl["PLAYER"].isin(team13_bowl),["PLAYER","Matches","Wkts"]]
	y=[]
	for i in team13_bowl_data:
	    team13_bowl_point.append(25*team13_bowl_data["Wkts"])
	    y.append(team13_bowl_data["Wkts"])
	team13_bowl_data.insert(2,"Points",team13_bowl_point[0],True)
	a=0
	for i in team13_bat_data:
	    team13_bat_point.append(team13_bat_data["Runs"])
	#for i in range(len(team13_bat_point)):
		 #a=a+int(team13_bat_point[i])
	team13_bat_data.insert(3, "Points", team13_bat_point[0], True)
	team13_bat_TRP=(sum(team13_bat_point[0]))
	team13_bowl_TWP=(sum(team13_bowl_point[0]))
	team13_total_points=team13_bat_TRP+team13_bowl_TWP
	team13_bat_point={"Player":"Total","Matches":"","Runs":team13_bat_TRP,"Points":team13_bat_TRP}
	team13_bowl_point={"PLAYER":"Total","Matches":"","Wkts":sum(y[0]),"Points":team13_bowl_TWP}
	team13_bat_data=team13_bat_data.append(team13_bat_point,ignore_index=True,sort=False)	
	team13_bowl_data=team13_bowl_data.append(team13_bowl_point,ignore_index=True,sort=False)
	print(team13_bowl_data)
	print("\n")
	print(team13_bat_data)
	print("\n")
	print(team13_bat_TRP,team13_bowl_TWP,team13_total_points)
	team13_BatFinal={}
	team13_BowlFinal={}
	team13_BatFinal["Players"]=team13_bat_data["Player"]
	team13_BatFinal["Runs"]=team13_bat_data["Runs"]
	team13_BatFinal["Points"]=team13_bat_data["Points"]
	team13_BatFinal["Matches"]=team13_bat_data["Matches"]
	team13_BowlFinal["Players"]=team13_bowl_data["PLAYER"]
	team13_BowlFinal["Wickets"]=team13_bowl_data["Wkts"]
	team13_BowlFinal["Points"]=team13_bowl_data["Points"]
	team13_BowlFinal["Matches"]=team13_bowl_data["Matches"]

	point_table4=[("Karan2",team12_bat_TRP,team12_bowl_TWP,team12_total_points),("Kavin2",team13_bat_TRP,team13_bowl_TWP,team13_total_points)]
	point_table4.sort(key = lambda x: x[3], reverse=True)
	print(point_table4)

	point_table3=[("Amish",team8_bat_TRP,team8_bowl_TWP,team8_total_points),("Khushal",team9_bat_TRP,team9_bowl_TWP,team9_total_points),("Jinay",team10_bat_TRP,team10_bowl_TWP,team10_total_points),("Deep",team11_bat_TRP,team11_bowl_TWP,team11_total_points)]
	point_table3.sort(key = lambda x: x[3], reverse=True)
	print(point_table3)

	point_table2=[("Karan",team6_bat_TRP,team6_bowl_TWP,team6_total_points),("Kavin",team7_bat_TRP,team7_bowl_TWP,team7_total_points)]
	point_table2.sort(key = lambda x: x[3], reverse=True)
	print(point_table2)

	point_table=[("Shubh",team1_bat_TRP,team1_bowl_TWP,team1_total_points),("Karan",team2_bat_TRP,team2_bowl_TWP,team2_total_points),("Harsh",team3_bat_TRP,team3_bowl_TWP,team3_total_points),("Amish",team4_bat_TRP,team4_bowl_TWP,team4_total_points),("Viraj",team5_bat_TRP,team5_bowl_TWP,team5_total_points)]
	point_table.sort(key = lambda x: x[3], reverse=True)
	print(point_table)

	return render_template("cricket.html", posts=team1_BatFinal, posts2=team2_BatFinal,Posts=team1_BowlFinal,Posts2=team2_BowlFinal,
										   posts3=team3_BatFinal,Posts3=team3_BowlFinal,posts4=team4_BatFinal,Posts4=team4_BowlFinal,
										   point_table=point_table,posts5=team5_BatFinal,Posts5=team5_BowlFinal,

										   posts6=team6_BatFinal,posts7=team7_BatFinal,Posts6=team6_BowlFinal,Posts7=team7_BowlFinal,
										   point_table2=point_table2,Bonus1=Bonus_team6_tuples,Bonus2=Bonus_team7_tuples,

										   posts8=team8_BatFinal, posts9=team9_BatFinal,Posts8=team8_BowlFinal,Posts9=team9_BowlFinal,
										   posts10=team10_BatFinal, posts11=team11_BatFinal,Posts10=team10_BowlFinal,Posts11=team11_BowlFinal,
										   point_table3 = point_table3,

										   posts12=team12_BatFinal, posts13=team13_BatFinal,Posts12=team12_BowlFinal,Posts13=team13_BowlFinal,
										   point_table4 = point_table4

										   )
	 # return (total_runs)

	csv_file.close()

if __name__ == '__main__': 
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)

