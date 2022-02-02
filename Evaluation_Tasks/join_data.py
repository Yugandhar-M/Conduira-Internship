import csv
import math
import ast

def return_activity_data(activity_data):
    activity_list = []
    for row in activity_data:
            temp_dict = {}
            temp_dict["media_type"]=ast.literal_eval(row["media_type"])['S']
            try:
                temp_dict["watched"]=ast.literal_eval(row["watched"])["M"]["value"]["S"]
            except:
                # temp_dict["watched"]=ast.literal_eval(row["watched"])["M"]["value"]["NULL"]
                temp_dict["watched"]=math.nan
            try:
                temp_dict["rating"]=ast.literal_eval(row["rating"])["M"]["value"]["S"]
            except:
                # temp_dict["rating"]=ast.literal_eval(row["rating"])["M"]["value"]["NULL"]
                temp_dict["rating"]=math.nan
            try:
                temp_dict["watchlist"]=ast.literal_eval(row["watchlist"])["M"]["value"]["S"]
            except:
                # temp_dict["watchlist"]=ast.literal_eval(row["watchlist"])["M"]["value"]["NULL"]
                temp_dict["watchlist"]=math.nan
            try:
                temp_dict["hide"]=ast.literal_eval(row["hide"])["M"]["value"]["S"]
            except:
                # temp_dict["hide"]=ast.literal_eval(row["hide"])["M"]["value"]["NULL"]
                temp_dict["hide"]=math.nan
            temp_dict["id"]=ast.literal_eval(row["id"])["S"].split('_')[0]
            activity_list.append(temp_dict)
    return activity_list

def check_id(row,activity_list):
    val = False
    for item in activity_list:
        if row["_id"]==item["id"] and row["_type"]==item["media_type"]:
            return item
            break
    else:
        return None

def main():
    with open("activity_data.csv","r") as f:
        activity_data = csv.DictReader(f)
        extracted_activity_data = return_activity_data(activity_data)
    f.close()
    
    out_data = []
    with open("data.csv","r") as ff:
        data = csv.DictReader(ff)
        default_dict = {"rating": math.nan, "hide": math.nan, "watchlist": math.nan, "watched": math.nan}
        for row in data:
            item = check_id(row,extracted_activity_data)
            if item:
                temp_dict = {}
                temp_dict = ast.literal_eval(row["_source"]) | item 
                out_data.append(str(temp_dict))
            else:
                temp_dict = {}
                temp_dict = {**ast.literal_eval(row["_source"]), **default_dict}
                out_data.append(str(temp_dict))
    ff.close()
    
    with open("Output_new.csv","w",newline="") as file:
        obj = csv.writer(file)
        obj.writerow(["_source"])
        for i in out_data:
            obj.writerow([i])
    file.close()

if __name__=="__main__":
    main()


    
