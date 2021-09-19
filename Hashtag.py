lib_has = {
'inspiration':"#Inspiration4",
'Inspiration':"#Inspiration4",
'Dragon':"#Dragon",
'dragon':"#Dragon",
'Resilience':"#Resilience",
"CesiumAstro":"#cesiumastro",
"Cesiumastro":"#cesiumastro",
"cesiumAstro":"#cesiumastro",
"Turksat":"#turksat",
"turksat":"#Turksat",
"spacex":"#SpaceX",
"SpaceX":"#SpaceX",
"falcon":"#Falcon",
"Falcon":"#Falcon",
"crew":"#Crew",
"Crew":"#Crew",
"space":"#Space",
"Space":"#Space"



}



def hashtag(text):
	splt_text = text.split(" ")
	htg_ed = []
	for i in splt_text:
		if i in lib_has:
			htg_ed.append(lib_has[i])
		else:
			htg_ed.append(i)
	regrouped = " ".join(htg_ed)
	return regrouped




