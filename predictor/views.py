from django.shortcuts import render
import pickle
import numpy as np
import os

# Load model safely
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model.pkl')
model = pickle.load(open(model_path, 'rb'))


def home(request):
    return render(request, "index.html")


def predict(request):
    if request.method == "POST":
        try:
            # ✅ Get all inputs
            holidayflag = float(request.POST.get('holidayflag'))
            forecastwind = float(request.POST.get('forecastwind'))
            systemloadea = float(request.POST.get('systemloadea'))
            smpea = float(request.POST.get('smpea'))
            temperature = float(request.POST.get('temperature'))
            windspeed = float(request.POST.get('windspeed'))
            co2 = float(request.POST.get('co2'))
            actualwind = float(request.POST.get('actualwind'))
            systemloadep2 = float(request.POST.get('systemloadep2'))
            hour = float(request.POST.get('hour'))
            day = float(request.POST.get('day'))
            month = float(request.POST.get('month'))

            # ✅ Arrange features (must match training)
            features = np.array([[holidayflag,
                                  forecastwind,
                                  systemloadea,
                                  smpea,
                                  temperature,
                                  windspeed,
                                  co2,
                                  actualwind,
                                  systemloadep2,
                                  hour,
                                  day,
                                  month]])

            prediction = model.predict(features)

            result = f"Predicted Electricity Price: {prediction[0]:.2f}"

        except Exception as e:
            result = f"Error: {str(e)}"

        return render(request, "index.html", {"result": result})

    return render(request, "index.html")