# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import connection
from datetime import datetime
from django.http import JsonResponse
import json
import datetime 
# Create your views here.

def statistics(response):
    q1 = "SELECT MAX(RK) AS L_RK FROM B_DATA;"
    q2 = "WITH temp_table AS ( "
    q2 += "SELECT Count(C_DATA.ime) AS c_count "
    q2 += "FROM C_DATA "
    q2 += "GROUP BY C_DATA.ime) "
    q2 += "SELECT MAX(c_count) AS max_count "
    q2 += "FROM temp_table;"
    
    with connection.cursor() as cursor:
        cursor.execute(q1)
        L_RK = cursor.fetchall()
        cursor.execute(q2)
        M_C = cursor.fetchall()
    return render(response, "statistics.html", {'q1': L_RK, 'q2': M_C})

def card(request):
    cur_rk = 0
    q1 = "SELECT MIN(RK) AS L_RK FROM B_DATA;"
    with connection.cursor() as cursor:
        cursor.execute(q1)
        val = cursor.fetchall()
        cur_rk = val[0][0]
    
    if request.method == 'POST':
        RK = request.POST['RK']
        RN = request.POST['RN']
        Marka = request.POST['Marka']
        Model = request.POST['Model']
        G_PR = request.POST['G_PR']
        KM = request.POST['KM']
        Kupe = request.POST['Kupe']
        Rama = request.POST['Rama']
        Dvigatel = request.POST['Dvigatel']
        Descr = request.POST['Descr']
        Problem = request.POST['Problem']
        R_DATA = request.POST['R_DATA']
        
        new_b_data = b_data(
            RK=RK,
            RN=RN,
            Marka=Marka,
            Model=Model,
            G_PR=G_PR,
            KM=KM,
            Kupe=Kupe,
            Rama=Rama,
            Dvigatel=Dvigatel,
            Descr=Descr,
            Problem=Problem,
            R_DATA=R_DATA,
        )
        
        ime = request.POST['ime']
        telefon = request.POST['telefon']
        
        new_c_data = c_data(
            RK=RK,
            ime=ime,
            telefon=telefon,
        )
        
        new_b_data.save()
        new_c_data.save()
        
    def get_db_data(rk):
        q1 = "SELECT * FROM B_DATA WHERE RK = "
        q2 = "SELECT * FROM C_DATA WHERE RK = "
        q1 += str(rk)
        q2 += str(rk)
        with connection.cursor() as cursor:
            cursor.execute(q1)
            bdata = cursor.fetchall()
            #print(bdata)
            cursor.execute(q2)
            cdata = cursor.fetchall()
            #print(cdata)
            
        default_box_values = {
            'RK': bdata[0][1],
            'RN': bdata[0][2],
            'Marka': bdata[0][3],
            'Model': bdata[0][4],
            'G_PR': bdata[0][5],
            'KM': bdata[0][6],
            'Kupe': bdata[0][7],
            'Rama': bdata[0][8],
            'Dvigatel': bdata[0][9],
            'Descr': bdata[0][10],
            'Problem': bdata[0][11],
            'R_DATA': bdata[0][12],
            'ime': cdata[0][2],
            'telefon': cdata[0][3],
        }
        return default_box_values
    
    if request.method == 'GET':
        if request.GET.get('C', '') == '1':
            q1 = "SELECT MAX(RK) AS L_RK FROM B_DATA;"
            with connection.cursor() as cursor:
                cursor.execute(q1)
                val = cursor.fetchall()
                cur_rk = val[0][0]
        
        elif request.GET.get('C', '') == '0':
            q1 = "SELECT MIN(RK) AS L_RK FROM B_DATA;"
            with connection.cursor() as cursor:
                cursor.execute(q1)
                val = cursor.fetchall()
                cur_rk = val[0][0]
            
    context = get_db_data(cur_rk)
    print(cur_rk, context)
    return render(request, "card.html", context)


def search(response):
	return render(response, "search.html", {})