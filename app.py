from bs4 import BeautifulSoup
import pandas as pd
import requests	
import numpy as np
from flask import Flask, render_template, url_for

#Family Game
app = Flask(__name__) 
  
@app.route('/') 
 
def hello_world(): 
	team1_bat=["KL Rahul", "Hardik Pandya","David Warner","Suresh Raina","AB de Villiers","Shikhar Dhawan","Mohammad Shami","Mohammad Nabi","Jofra Archer","Kuldeep Yadav","Navdeep Saini"]
	team1_bowl=team1_bat

	team2_bat=["Virat Kohli","Jasprit Bumrah","Rashid Khan","Dwayne Bravo","Andre Russell","Ajinkya Rahane","Bhuvneshwar Kumar","MS Dhoni","Mayank Agarwal","Sandeep Lamichhane","Umesh Yadav"]
	team2_bowl=team2_bat
	
	team3_bat=["Rohit Sharma","Shreyas Iyer","Ishan Kishan","Glenn Maxwell","Eoin Morgan","Ben Stokes","Imran Tahir","Ravichandran Ashwin","Shardul Thakur","Rahul Chahar","Siddarth Kaul"]
	team3_bowl=team3_bat
	
	team4_bat=["Sunil Narine","Rishabh Pant","Shubman Gill","Steve Smith","Yuzvendra Chahal","Manish Pandey","Khaleel Ahmed","Suryakumar Yadav","Pat Cummins","Krunal Pandya","Deepak Chahar"]
	team4_bowl=team4_bat

	team5_bat=["Jos Buttler","Sanju Samson","Prithvi Shaw","Ravindra Jadeja","Aaron Finch","Washington Sundar","Kagiso Rabada","Nitish Rana","Ambati Rayudu","Mujeeb Ur Rahman","Prasidh Krishna"]
	team5_bowl=team5_bat

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

	point_table=[("Shubh",team1_bat_TRP,team1_bowl_TWP,team1_total_points),("Karan",team2_bat_TRP,team2_bowl_TWP,team2_total_points),("Harsh",team3_bat_TRP,team3_bowl_TWP,team3_total_points),("Amish",team4_bat_TRP,team4_bowl_TWP,team4_total_points),("Viraj",team5_bat_TRP,team5_bowl_TWP,team5_total_points)]
	point_table.sort(key = lambda x: x[3], reverse=True)
	print(point_table)

	return render_template("cricket.html", posts=team1_BatFinal, posts2=team2_BatFinal,Posts=team1_BowlFinal,Posts2=team2_BowlFinal,posts3=team3_BatFinal,Posts3=team3_BowlFinal,posts4=team4_BatFinal,Posts4=team4_BowlFinal,point_table=point_table,posts5=team5_BatFinal,Posts5=team5_BowlFinal)
	 # return (total_runs)

	csv_file.close()

if __name__ == '__main__': 
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)

