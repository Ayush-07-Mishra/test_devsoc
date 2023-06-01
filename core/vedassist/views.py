from django.shortcuts import render , redirect
from .models import*
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib



@login_required(login_url='/login/')
def home(request):
    return render(request , 'home.html')
    



def test(request):
    return render(request, 'test.html')



def result(request):
    return render(request, 'result.html')



def predict(request):
    if request.method == 'POST':
        # Retrieve user input from the form
        user_input = [
            request.POST.get('cold').lower(),
            request.POST.get('eyepain').lower(),
            request.POST.get('fever').lower(),
            request.POST.get('headache').lower(),
            request.POST.get('stomachache').lower(),
            request.POST.get('dizziness').lower(),
            request.POST.get('vomiting').lower(),
            request.POST.get('chestpain').lower(),
            request.POST.get('jointpain').lower(),
            request.POST.get('loosemotion').lower(),
            request.POST.get('throatinfection').lower(),
            int(request.POST.get('age')),
            int(request.POST.get('gender')),
            int(request.POST.get('weight'))
        ]


        # Load the trained model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        data=pd.DataFrame([
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','no','no','no','no','yes','no','yes','yes','yes',30,'Female',150,'Chandanasava','Khadirarishta','Mustakarishta'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','yes','yes','yes','no','yes','no','no','yes','no','no',60,'Male',136,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatryasava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjunarishta'],
['no','yes','no','yes','no','yes','no','no','no','no','yes',47,'Female',77,'Dhatrysava','Pippalyasavam','Jeerakarishtam'],
['yes','no','yes','no','yes','no','no','no','no','no','no',25,'Male',65,'Ayaskriti','Palashpushpasava','Pippalyasavam'],
['no','yes','no','yes','no','no','no','no','yes','no','yes',32,'Female',58,'Chandanasava','Kutajarishta','Arjunarishta'],
['no','no','yes','no','no','yes','no','no','no','no','yes',45,'Male',72,'Kalmeghasava','Angoorasava','Drakshasava'],
['yes','yes','yes','no','no','no','no','yes','no','no','no',38,'Female',61,'Saraswatarishta','Mrigamadasava','Raktshodhakarishta'],
['yes','no','yes','yes','no','yes','yes','no','yes','yes','no',42,'Male',77,'Dhatryasava','Dasamoolarishtam','Punarnavasavam'],
['no','no','yes','no','yes','no','yes','no','no','no','no',34,'Female',63,'Babularishta','Takrarishta','Balamritam'],
['yes','no','no','yes','no','no','no','no','no','no','yes',37,'Male',72,'Ashwagandha','Lohasava','Vasarishta & Vasasava'],
['no','yes','yes','yes','yes','no','no','yes','no','yes','yes',40,'Female',69,'Neem','Arvindasava','Punarnavarishta'],
['yes','no','no','yes','no','yes','no','no','no','no','no',48,'Male',73,'Ayaskriti','Dashamoola Jeerakam','Karpoorasava'],
['no','no','yes','no','no','no','yes','no','yes','no','no',33,'Female',63,'Chandanasava','Khadirarishta','Mustakarishta'],
['yes','yes','yes','no','yes','no','no','yes','no','no','yes',31,'Male',68,'Raktshodhakarishta','Vidangarishta','Arjun']
],columns=['Cold','Eyepain','Fever','Headache','Stomachache','Dizziness','Vomiting','Chestpain','Jointpain','Loosemotion','Throatinfection','Age','Gender','Weight','Ayurvedic Medicine','Ayurvedic Medicine1','Ayurvedic Medicine2'])


        data.replace({'yes': 0, 'no': 1}, inplace=True)
        data.replace({'Male': 3, 'Female': 4}, inplace=True)
        features = data.drop(columns=['Ayurvedic Medicine', 'Ayurvedic Medicine1', 'Ayurvedic Medicine2'])
        targets = data[['Ayurvedic Medicine', 'Ayurvedic Medicine1', 'Ayurvedic Medicine2']]
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2, random_state=42)

        # Fit the model to the training data
        model.fit(X_train, y_train)

        # Make predictions on the user input
        user_output = model.predict([user_input])

        # Decode the predictions
        user_output_decoded = pd.DataFrame(user_output, columns=['Ayurvedic Medicine', 'Ayurvedic Medicine1', 'Ayurvedic Medicine2'])
        user_output_decoded.replace({0: 'yes', 1: 'no'}, inplace=True)
        user_output_decoded.replace({3: 'Male', 4: 'Female'}, inplace=True)

        # Extract the predicted values
        medicine1 = user_output_decoded['Ayurvedic Medicine'][0]
        medicine2 = user_output_decoded['Ayurvedic Medicine1'][0]
        medicine3 = user_output_decoded['Ayurvedic Medicine2'][0]

        # Save the user input and predicted medicines to the database
        prediction = AyurvedicPrediction(
            cold=user_input[0],
            eyepain=user_input[1],
            fever=user_input[2],
            headache=user_input[3],
            stomachache=user_input[4],
            dizziness=user_input[5],
            vomiting=user_input[6],
            chestpain=user_input[7],
            jointpain=user_input[8],
            loosemotion=user_input[9],
            throatinfection=user_input[10],
            age=user_input[11],
            gender=user_input[12],
            weight=user_input[13],
            medicine1=medicine1,
            medicine2=medicine2,
            medicine3=medicine3
        )
        prediction.save()

        context = {
            'medicine1': medicine1,
            'medicine2': medicine2,
            'medicine3': medicine3
        }

        return render(request, 'result.html', context)

    else:
        return render(request , 'test.html')



def login_page(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Inavlid Username")
            return redirect('/login/')
        
        user =authenticate(username = username, password = password)

        if user is None:    
            messages.info(request, "Inavlid Password")
            return redirect('/login/')
        
        else:
            login(request,user)       # iska name(lgoin()) aur function ka name (login_page) diffrent hona chaiye 
                        # varna infiniite loop chlenga 
            return redirect('/home/')


    return render(request, 'login.html')



def logout_page(request):
    logout(request)
    return redirect('/login')


def register(request):



    if request.method != "POST":
        return render(request, 'register.html')
    


    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')




    user = User.objects.filter(username=username)


    if user.exists():
        messages.info(request, "Username Already Exists")
        return redirect('/register/')


    user = User.objects.create(
        first_name= first_name, 
        last_name= last_name,
        username=username,
        # password=password  we cant directly add password so we have encrypt it
        )

    user.set_password(password)    # this method is already thier in django
    user.save()
    messages.info(request, "Account created successfully")

    return redirect('/login/')






























