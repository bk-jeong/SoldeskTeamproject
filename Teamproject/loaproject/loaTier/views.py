import pandas as pd
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from .models import Tier, Raid

# Create your views here.


def index(request):
    return render(request, "index.html")



def makeTier(request):
    try:
        # Insert ORM
        tier = Tier(
            tier1=request.POST["1tia"],
            tier2=request.POST["2tia"],
            tier3=request.POST["3tia"],
            # tier4=request.POST[""],
            # tier5=request.POST[""],
            # tierout=request.POST[""],
            # r_id=request.POST[""]
        )

        # DB save
        tier.save()

        # Select ORM (lastest DB row)
        tierRes = Tier.objects.order_by("-id")[:1]
        tier1 = tierRes[0].tier1.split(",")
        tier2 = tierRes[0].tier2.split(",")
        tier3 = tierRes[0].tier3.split(",")
        # tier4 = tierRes[0].tier4.split(",")
        # tier5 = tierRes[0].tier5.split(",")
        # tierout = tierRes[0].tierout.split(",")

        # Returon Dictionary Object
        context = {
            "tier1": tier1,
            "tier2": tier2,
            "tier3": tier3,
            # "tier4": tier4,
            # "tier5": tier5,
            # "tierout": tierout,
        }
        return render(request, "userResult.html", context)
    except Exception as e:
        return print(str(e))

def allResult(request):
    try:
        allDatas = pd.DataFrame(Tier.objects.all().values())
        df = pd.DataFrame(allDatas).loc[
            :, ["tier1", "tier2", "tier3", "tier4", "tier5"]
        ]
        print(df)
        egv_init = {}

        return_obj = {"tier1": "", "tier2": "", "tier3": "", "tier4": "", "tier5": ""}

        for i in return_obj.keys():
            egv_init = {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "07": 0,
                "08": 0,
                "09": 0,
                "10": 0,
                "11": 0,
                "12": 0,
                "13": 0,
                "14": 0,
                "15": 0,
                "16": 0,
                "17": 0,
                "18": 0,
                "19": 0,
                "20": 0,
                "21": 0,
                "22": 0,
                "23": 0,
                "24": 0,
                "25": 0,
                "26": 0,
                "27": 0,
                "28": 0,
                "29": 0,
                "30": 0,
                "31": 0,
                "32": 0,
                "33": 0,
                "34": 0,
                "35": 0,
                "36": 0,
                "37": 0,
                "38": 0,
                "39": 0,
                "40": 0,
                "41": 0,
                "42": 0,
                "43": 0,
                "44": 0,
                "45": 0,
                "46": 0,
                "47": 0,
                "48": 0,
                "49": 0,
                "50": 0,
                "51": 0,
                "52": 0,
            }
            return_obj[i] = egv_init
        #testlist=list(0 for i in range(0,52))
        #print(testlist)
        for i in range(len(df)):
            for j in return_obj.keys():
                for k in egv_init.keys():
                    if df[j].str.contains(k)[i]:
                        return_obj[j][k] += 1
                        #testlist[k]+=1
        #print(testlist)
        
        # print(return_obj)
        score = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "07": 0,
            "08": 0,
            "09": 0,
            "10": 0,
            "11": 0,
            "12": 0,
            "13": 0,
            "14": 0,
            "15": 0,
            "16": 0,
            "17": 0,
            "18": 0,
            "19": 0,
            "20": 0,
            "21": 0,
            "22": 0,
            "23": 0,
            "24": 0,
            "25": 0,
            "26": 0,
            "27": 0,
            "28": 0,
            "29": 0,
            "30": 0,
            "31": 0,
            "32": 0,
            "33": 0,
            "34": 0,
            "35": 0,
            "36": 0,
            "37": 0,
            "38": 0,
            "39": 0,
            "40": 0,
            "41": 0,
            "42": 0,
            "43": 0,
            "44": 0,
            "45": 0,
            "46": 0,
            "47": 0,
            "48": 0,
            "49": 0,
            "50": 0,
            "51": 0,
            "52": 0,
        }
        for j in return_obj.keys():
            for k in egv_init.keys():
                if j == "tier1":
                    score[k] += return_obj[j][k] * 5 / len(df)
                elif j == "tier2":
                    score[k] += return_obj[j][k] * 4 / len(df)
                elif j == "tier3":
                    score[k] += return_obj[j][k] * 3 / len(df)
                elif j == "tier4":
                    score[k] += return_obj[j][k] * 2 / len(df)
                elif j == "tier5":
                    score[k] += return_obj[j][k] / len(df)

        sorted_score = sorted(score.items(), key=lambda item: item[1], reverse=True)
        print(sorted_score)
        context = {
            "tier1": [],
            "tier2": [],
            "tier3": [],
            "tier4": [],
            "tier5": [],
            "NonSel": [],
        }

        for x, y in sorted_score:
            if y >= 4.0:
                context["tier1"] += [x]
            elif y >= 3.0:
                context["tier2"] += [x]
            elif y >= 2.0:
                context["tier3"] += [x]
            elif y >= 1.0:
                context["tier4"] += [x]
            elif y > 0:
                context["tier5"] += [x]
            else:
                context["NonSel"] += [x]

        print(context)
        return render(request, "allResult.html",  context)
    except Exception as e:
        return print(str(e))
