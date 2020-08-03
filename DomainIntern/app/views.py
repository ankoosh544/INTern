from django.shortcuts import render

from app.models import DomainsModel
from pywhoisxml.lookup import Lookup
import whois
from datetime import datetime
import pandas as pd

from django.shortcuts import render

from app.models import DomainsModel
from pywhoisxml.lookup import Lookup
import whois
from datetime import datetime


# def homePage(request):
#     return render(request,"hoempage.html")
#
#
def showIndex(request):
    dd = DomainsModel.objects.values()
    # user = request.POST.get("t1")
    # password = request.POST["t2"]
    # if user == "massimo" and password == "massimo":
    return render(request, "design.html", {"data": dd})
    # else:
    #     return homePage(request)


def displayIndex(request):
        dd = DomainsModel.objects.all()
        if request.method == "POST":
            ff = request.FILES["f"]
            # print(ff)
            text = ff.read()
            txt = text.split("\r\n".encode('utf-8'))
            # print(text)
            # print(txt)
            l = len(txt)

            b =[1,2,3]
            finalarray= [
                        {'name': "it", 'data': [],"dbdata":[]},
                        {'name': "com", 'data': [],"dbdata":[]},
                        {'name': "eu", 'data': [],"dbdata": []},
                        {'name': "net", 'data': [],"dbdata":[]},
                        {'name': "org", 'data': [],"dbdata":[]},
                        {'name': "info", 'data': [],"dbdata":[]},
                        {'name': "biz", 'data': [],"dbdata":[]}]

            resultArrary = []
            for x in range(l):

                res = txt[x].decode('utf-8')
                # print(res)
                # print(res)

                for domain in finalarray:
                    comstring = " "

                    comstring = res.replace("it", domain["name"])
                    # print(comstring)

                    try:
                        w = whois.whois(comstring)
                        # print(w)
                        # print(w.name_servers)
                        d= w.creation_date
                        if type(d) is type(b):
                            d = str(w.creation_date[0]).split(" ")[0]
                        elif w.creation_date == "null":
                            d = ""
                        else:
                            d = str(w.creation_date).split(" ")[0]

                        # res= res +" \n \n" + d
                        itserver = w.name_servers
                    except (whois.parser.PywhoisError):
                        # print(" no match found so free domain")
                        itserver = None

                    if itserver == None:
                        result ="free"
                    else:
                        result = "busy"
                        # print(itserver)

                    domain["data"].append(result)
                    DomainsModel(category=domain["name"],value=comstring,status=result,creation_date=d).save()
            # print(finalarray)

            return render(request,"design.html",{"data1":dd,"data":finalarray})


        else:
                return showIndex(request)



def deleteData(request):
    # print("delete")
    dd = DomainsModel.objects.all()
    dd.delete()
    displayIndex(request)
    return render(request, "design.html", {"data1": dd })


