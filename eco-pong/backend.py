id_list=[1,2,6,19,29,32,37]

score_list=[0,0,0,0,0,0,0]
def back_end(current_date):
    import requests
    import json
    import datetime
    import os
    def increment_by_week(in_date,days):
        out_date=[0,0,0,0,0,0]
        for i in range(len(in_date)):
            if i==2:
                out_date[i]=in_date[i]+days%month_list[in_date[1]-1]

                if in_date[i]+days!=out_date[i]:
                    if in_date[i]+list_[0]%month_list[in_date[1]-1]==0:
                        out_date[i]=month_list[in_date[1]-1]

                    else:
                        out_date[1]+=in_date[1]
            else:
                out_date[i]=in_date[i]
        return(out_date)



    def decrement_by_week(in_date,days):
        out_date=[0,0,0,0,0,0]
        for i in range(len(in_date)):
            if i==2:
                out_date[i]=in_date[i]-days%month_list[in_date[1]-1]

                if in_date[i]-days!=out_date[i]:
                    out_date[1]=in_date[1]-1
                if out_date[i]==0:
                        out_date[i]=month_list[in_date[1]-1]
                        out_date[1]=in_date[1]-1
            else:
                out_date[i]=in_date[i]
        return(out_date)



    def dic_zip(keys, values):
        dic = {}
        for i in range(len(keys)):
            dic[keys[i]] = values[i]
        return dic

    def what_start_date(list_):
        out_list=[0,0,0,0,0,0]
        day=datetime.date(list_[0],list_[1],list_[2]).weekday()
        out_list=decrement_by_week(list_,day)
        out_list[3:6]=[00,30,00]
        return out_list






    id_list=[1,2,6,19,29,32,37]
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    school_list=[None,None,None,None,None,None,None]

    school_total_beg=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    school_total_end=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    school_reduction=[]
    start_date_back=[0,0,0,0,0,0]
    week_back_date=[0,0,0,0,0,0]
    start_date=what_start_date(current_date)
    week_end_date=[0,0,0,0,0,0]
    school_dic={}


    start_date_back=decrement_by_week(start_date,7)

    week_end_date=increment_by_week(start_date,7)

    week_back_date=decrement_by_week(current_date,7)
    date_string=str(current_date).replace(" ","").replace(",","").replace("[","").replace("]","")
    if not os.path.isfile(date_string+".txt"):
        test_mesg=str(week_back_date[0])+"-"+str(week_back_date[1]).zfill(2)+"-"+str(week_back_date[2]).zfill(2)+"T"+str(week_back_date[3]).zfill(2)+":"+str(week_back_date[4]).zfill(2)+":"+str(week_back_date[5]).zfill(2)
        for i in range(7):
            request_message="http://data.energysmartbirmingham.com/api/Utility/GetElectric?startDate="+str(start_date_back[2])+"-"+str(start_date_back[1])+"-"+str(start_date_back[0])+"&endDate="+str(start_date[2])+"-"+str(start_date[1])+"-"+str(start_date[0])+"&siteId="+str(id_list[i])
            response=requests.get(request_message)
            data_json = response.json()
            #data=response.content
            #data_json=json.loads(data)
            #school_list[i]=data_json[1]["SiteName"]
            for item in data_json:
                school_total_beg[i]=school_total_beg[i]+item["Value"]
                school_total_beg[i]=round(school_total_beg[i],2)
                if str(item["TimeStamp"])==str(test_mesg):
                    break
        test_mesg=str(current_date[0])+"-"+str(current_date[1]).zfill(2)+"-"+str(current_date[2]).zfill(2)+"T"+str(current_date[3]).zfill(2)+":"+str(current_date[4]).zfill(2)+":"+str(current_date[5]).zfill(2)
        for i in range(7):
            request_message="http://data.energysmartbirmingham.com/api/Utility/GetElectric?startDate="+str(start_date[2])+"-"+str(start_date[1])+"-"+str(start_date[0])+"&endDate="+str(week_end_date[2])+"-"+str(week_end_date[1])+"-"+str(week_end_date[0])+"&siteId="+str(id_list[i])
            response=requests.get(request_message)
            #data=response.content
            #data_json=json.loads(data)
            data_json = response.json()
            for item in data_json:
                school_total_end[i]=school_total_end[i]+item["Value"]
                school_total_end[i]=round(school_total_end[i],2)
                if str(item["TimeStamp"])==str(test_mesg):
                    break
        for i in range(7):
            school_reduction.append((school_total_end[i]/school_total_beg[i])*100-100)
            school_reduction[i]=round(school_reduction[i],2)
        school_dic=dic_zip(school_list,school_reduction)

        file=open(date_string+".txt","w")
        for item in school_reduction:
            file.write(str(item))
            file.write("\n")
        file.close()
        return(school_reduction)
    else:
        file=open(date_string+".txt","r")
        for i in range(7):
            item=file.readline()
            item=item.replace("\n","")
            school_reduction.append(float(item))
        file.close()
        return(school_reduction)
def score_track(idd,wl):
    global score_list
    if wl==2:
        return score_list
    elif wl==3:
      score_list=[0,0,0,0,0,0,0]
    else:
        for i in range(len(id_list)):
            if idd==id_list[i]:
                no=i
                break
        if wl==0:
            score_list[no]=score_list[no]+1
        else:
            score_list[no]=score_list[no]+3
        return score_list

'''
print(back_end([2015,1,16,15,00,00]))
score_track(6,3)
print(score_track(6,1))
'''
