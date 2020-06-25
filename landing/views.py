from django.shortcuts import render
from datetime import date


# Create your views here.
def index(request):
    today = date.today()
    born = date(1991, 9, 13)
    my_age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    cv_link = "https://www.dropbox.com/s/r21duymhq6pts0p/bk%C3%BCpfer_CV%20%5Bjun-2020%5D.pdf?dl=0"
    return render(request, "index.html", {"my_age": my_age, "cv_link": cv_link})
