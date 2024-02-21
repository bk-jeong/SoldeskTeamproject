import pandas as pd
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Tier

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
    engv = list(getToken().keys())
    context = {"engv": engv}
    return render(request, "index.html", context)

def makeTier(request):
    try:
        if request.method == "POST":
            # Insert ORM
            tier = Tier(
                # raid=request.POST.get("raid"),
                tier1=request.POST.get("1tia"),
                tier2=request.POST.get("2tia"),
                tier3=request.POST.get("3tia"),
                # tier4=request.POST.get("1tia"),
                # tier5=request.POST.get("1tia"),
                # tierout=request.POST.get("1tia"),
            )
            # DB save
            tier.save()
            return HttpResponseRedirect("/res")

        # Select ORM (lastest DB row)
        tierRes = Tier.objects.order_by("-id")[:1]
        # raid = tierRes[0].raid.values()
        tier1 = tierRes[0].tier1.split(",")
        tier2 = tierRes[0].tier2.split(",")
        tier3 = tierRes[0].tier3.split(",")
        # tier4 = tierRes[0].tier4.split(",")
        # tier5 = tierRes[0].tier5.split(",")
        # tierout = tierRes[0].tierout.split(",")

        # Returon Dictionary Object
        context = {
            # "raid":raid,
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
        # Tier 테이블에 있는 데이터 가져오기
        data = Tier.objects.all().values()

        alldf = pd.DataFrame(data).loc[
            :, ["tier1", "tier2", "tier3", "tier4", "tier5"]
        ]
        # 각인이 몇번 해당 티어에 있는지 count하기 위한 변수(dictionary)
        egv_init = getToken()
        # egv_init이라는 변수를 넣을 상위 dictionary
        return_obj = {"tier1": "", "tier2": "", "tier3": "", "tier4": "", "tier5": ""}
        # return_obj의 key(각 티어)에 egv_init(value) 설정
        for i in return_obj.keys():
            # egv_init = 각인명 - 각 티어에 매겨진 횟수
            return_obj[i] = getToken()

        # 각인 count
        for i in range(len(alldf)):     # DB row 수 만큼 반복
            for j in return_obj.keys(): # 각 티어만큼 반복
                for k in egv_init.keys():   # 각인 개수만큼 반복
                    if alldf[j].str.contains(k)[i]:
                        return_obj[j][k] += 1   # 특정 티어의 특정 각인의 value 1씩 더한다

        # print(return_obj)
        # 평균 티어표를 만들기 위한 각 각인의 점수를 넣을 score(dictionary)
        score = getToken()
        
        for j in return_obj.keys():
            for k in egv_init.keys():
                if j == "tier1":
                    score[k] += return_obj[j][k] * 5 / len(alldf)
                elif j == "tier2":
                    score[k] += return_obj[j][k] * 4 / len(alldf)
                elif j == "tier3":
                    score[k] += return_obj[j][k] * 3 / len(alldf)
                elif j == "tier4":
                    score[k] += return_obj[j][k] * 2 / len(alldf)
                elif j == "tier5":
                    score[k] += return_obj[j][k] / len(alldf)
        # 점수를 큰 순서대로 정렬
        sorted_score = sorted(score.items(), key=lambda item: item[1], reverse=True)
        #print(sorted_score)

        # html에서 보여줄 티어표
        context = {
            "tier1": [],
            "tier2": [],
            "tier3": [],
            "tier4": [],
            "tier5": [],
            "NonSel": [],
        }
        # 점수를 기반으로 context에 각인명 넣어주기
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

        # print(context)
        return render(request, "allResult.html", context)
    except Exception as e:
        return print(str(e))
