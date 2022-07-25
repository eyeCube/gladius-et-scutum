import pandas as pd

ability_sheets=["Abilities-Fire","Abilities-Earth","Abilities-Air","Abilities-Water"]
                #"Abilities-Combo"]

abilities={}
    
for sheet in ability_sheets:

    df = pd.read_excel('rpg.xlsx', sheet_name=sheet)

    col_ability = df['Ability'].tolist()
    col_element = df['Element'].tolist()
    col_mode = df['Mode'].tolist()
    col_prereqs = df['Pre-reqs'].tolist()
    col_reqskill = df['ReqSkill'].tolist()
    col_level = df['Level'].tolist()
    col_weapon = df['Weapon'].tolist()
    col_sp = df['SP cost'].tolist()
    col_nrg = df['NRG cost'].tolist()
    col_hit = df['Hit%'].tolist()
    col_priority = df['Priority'].tolist()
    col_damage = df['Damage'].tolist()
    col_defense = df['Defense'].tolist()
    col_evade = df['Evade+%'].tolist()
    col_short = df['Short%'].tolist()
    col_wide = df['Wide%'].tolist()
    col_status = df['Status%'].tolist()
    col_statusDur = df['StatusDur'].tolist()
    col_special = df['Special'].tolist()
    col_notes = df['Notes'].tolist()

    zipped=zip(
        col_ability, col_element, col_mode, col_prereqs,col_reqskill, col_level,
        col_weapon, col_sp, col_nrg, col_hit, col_priority, col_damage, col_defense,
        col_evade, col_short, col_wide, col_status, col_statusDur, col_special,
        col_notes
        )

    for ability in zipped:
        if (not pd.isna(ability[0])):
##            print(ability)
            data={}
            data.update({"name":ability[0]})
            data.update({"element":ability[1] if (not pd.isna(ability[1])) else ""})
            data.update({"mode":ability[2] if (not pd.isna(ability[2])) else ""})
            data.update({"pre-reqs":ability[3] if (not pd.isna(ability[3])) else ""})
            data.update({"req-skill":round(ability[4]) if (not pd.isna(ability[4])) else 0})
            data.update({"level":round(ability[5]) if (not pd.isna(ability[5])) else 0})
            data.update({"weapon":ability[6] if (not pd.isna(ability[6])) else "Any"})
            data.update({"sp":round(ability[7]) if (not pd.isna(ability[7])) else 0})
            data.update({"nrg":round(ability[8]) if (not pd.isna(ability[8])) else 0})
            data.update({"hit":round(100*ability[9]) if (not pd.isna(ability[9])) else 0})
            data.update({"priority":round(ability[10]) if (not pd.isna(ability[10])) else 0})
            data.update({"damage":round(ability[11]) if (not pd.isna(ability[11])) else 0})
            data.update({"defense":round(ability[12]) if (not pd.isna(ability[12])) else 0})
            data.update({"evasion":round(100*ability[13]) if (not pd.isna(ability[13])) else 0})
            data.update({"short":round(100*ability[14]) if (not pd.isna(ability[14])) else 0})
            data.update({"wide":round(100*ability[15]) if (not pd.isna(ability[15])) else 0})
            data.update({"status":round(100*ability[16]) if (not pd.isna(ability[16])) else 0})
            data.update({"status-dur":round(ability[17]) if (not pd.isna(ability[17])) else 0})
            data.update({"special":ability[18] if (not pd.isna(ability[18])) else ""})
            data.update({"notes":ability[19] if (not pd.isna(ability[19])) else ""})
            abilities.update({ability[0]: data})


# generic attack tech
data={}
data.update({"name":"Attack"})
data.update({"element":""})
data.update({"mode":"both"})
data.update({"pre-reqs":""})
data.update({"req-skill":0})
data.update({"level":0})
data.update({"weapon":"Any"})
data.update({"sp":0})
data.update({"nrg":1})
data.update({"hit":50})
data.update({"priority":0})
data.update({"damage":1})
data.update({"defense":0})
data.update({"evasion":0})
data.update({"short":0})
data.update({"wide":0})
data.update({"status":0})
data.update({"status-dur":0})
data.update({"special":""})
data.update({"notes":"The most basic of combat techniques."})
abilities.update({"Attack":data})

# output

print('{')
for k,v in abilities.items():
    print("\"{}\": {},".format(k,v))
print('}')












