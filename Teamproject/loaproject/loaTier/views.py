import pandas as pd
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tier, Raid

# Create your views here.
    
def getToken():
    egv_init = {
                "01_bigi": 0,
                "02_kwangki": 0,
                "03_boonmang": 0,
                "04_zoongsu": 0,
                "05_gogi": 0,
                "06_zeontae": 0,
                "07_cheodan": 0,
                "08_posik": 0,
                "09_oeganhwa": 0,
                "10_chosim": 0,
                "11_zeolzung": 0,
                "12_zeolze": 0,
                "13_chesool": 0,
                "14_choongyuk": 0,
                "15_yukcheon": 0,
                "16_semaek": 0,
                "17_ilgyuk": 0,
                "18_nanmu": 0,
                "19_soora": 0,
                "20_kwaonwang": 0,
                "21_yoosan": 0,
                "22_kisool": 0,
                "23_pogyuk": 0,
                "24_hwaryuk": 0,
                "25_doodong": 0,
                "26_zuksoup": 0,
                "27_gangmu": 0,
                "28_hangun": 0,
                "29_pime": 0,
                "30_sasi": 0,
                "31_kyokam": 0,
                "32_sangso": 0,
                "33_hwangze": 0,
                "34_hwanghoo": 0,
                "35_zeomhwa": 0,
                "36_hwanryu": 0,
                "37_choongdong": 0,
                "38_ukze": 0,
                "39_burst": 0,
                "40_zanzae": 0,
                "41_dalso": 0,
                "42_galzung": 0,
                "43_manwol": 0,
                "44_gumum": 0,
                "45_zilpoong": 0,
                "46_islebi": 0,
                "47_chookoh": 0,
                "48_simpan": 0,
                "49_zeolgu": 0,
                "50_zinyong": 0,
                "51_mangae": 0,
                "52_heigwi": 0,
            }
    return egv_init
   
def index(request):
    context = {"engv": list(getToken().keys())}
    return render(request, "index/index1.html", context)

def index1(request):
    context = {"engv": list(getToken().keys())}
    return render(request, "index/index1.html", context)

def index2(request):
    context = {"engv": list(getToken().keys())}
    return render(request, "index/index2.html", context)

def index3(request):
    context = {"engv": list(getToken().keys())}
    return render(request, "index/index3.html", context)

def makeTier(request):
    try:
        if request.method == "POST":
            # Insert ORM
            tier = Tier(
                tier1=request.POST["1tia"],
                tier2=request.POST["2tia"],
                tier3=request.POST["3tia"],
                tier4=request.POST["4tia"],
                tier5=request.POST["5tia"],
                tierout=request.POST["tierout"],
            )

            # DB save
            tier.save()
            return HttpResponseRedirect("/res")

        # Select ORM (lastest DB row)
        tierRes = Tier.objects.order_by("-id")[:1]
        tier1 = tierRes[0].tier1.split(",")
        tier2 = tierRes[0].tier2.split(",")
        tier3 = tierRes[0].tier3.split(",")
        tier4 = tierRes[0].tier4.split(",")
        tier5 = tierRes[0].tier5.split(",")
        tierout = tierRes[0].tierout.split(",")
        
        # Returon Dictionary Object
        context = {
            "tier1": tier1,
            "tier2": tier2,
            "tier3": tier3,
            "tier4": tier4,
            "tier5": tier5,
            "tierout": tierout,
        }
        
        return render(request, "results/userResult.html", context)
    except Exception as e:
        return print(str(e))


def allResult(request):
    try:
        allDatas = pd.DataFrame(Tier.objects.all().values())
        df = pd.DataFrame(allDatas).loc[
            :, ["tier1", "tier2", "tier3", "tier4", "tier5", ]
        ]
        print(df)
        egv_init = {}

        return_obj = {"tier1": "", "tier2": "", "tier3": "", "tier4": "", "tier5": "", "tierout": ""}

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

        for i in range(len(df)):
            for j in return_obj.keys():
                for k in egv_init.keys():
                    if df[j].str.contains(k)[i]:
                        return_obj[j][k] += 1

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
        return render(request, "results/allResult.html", {"context": context})
    except Exception as e:
        return print(str(e))
