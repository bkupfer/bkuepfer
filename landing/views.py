from django.shortcuts import render
from dog_classifier.dog_classifier import DogClassifier
from base64 import b64encode
import datetime


def index(request):
    birth_date = datetime.date(1991, 9, 13)
    current_year = datetime.date.today().year
    current_age = round((datetime.date.today() - birth_date).days / 365, 1)
    cv_link = ""
    return render(request, "index.html", {
        "my_age": current_age,
        "copyright_year": current_year,
        "cv_link": cv_link,
    })


def dog_classifier(request):
    prediction = input_image = ''
    if request.FILES:
        image_file = request.FILES['dog_image'].read()

        encoded = b64encode(image_file).decode('ascii')
        mime = "image/jpg"
        mime = mime + ";" if mime else ";"
        input_image = "data:%sbase64,%s" % (mime, encoded)

        classifier = DogClassifier()
        prediction = classifier.Xception_predict_breed(image_file)

    return render(request, "dog_classifier.html", {
        "prediction": prediction,
        "img_uri": input_image
    })


