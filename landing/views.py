from django.shortcuts import render
from datetime import date


# Create your views here.
def index(request):
    today = date.today()
    born = date(1991, 9, 13)
    my_age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    cv_link = [
        "https://www.dropbox.com/s/r21duymhq6pts0p/bk%C3%BCpfer_CV%20%5Bjun-2020%5D.pdf?dl=0",  # 06.2020
        "https://www.dropbox.com/s/8bofssviydqb1vk/%5B20.07%5D%20bkuepfer_CV.pdf?dl=0",         # 07.2020
    ]
    return render(request, "index.html", {"my_age": my_age, "cv_link": cv_link[1]})
