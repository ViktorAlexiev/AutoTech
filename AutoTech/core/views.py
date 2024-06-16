# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import connection
from datetime import datetime
from django.http import JsonResponse
import json
import datetime 
from .forms import *
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
    return render(response, "statistics.html", {'q1': L_RK[0][0], 'q2': M_C[0][0]})

def card(request):
    context = {}
    #del request.session['cur_rk']
    cur_rk = request.session.get('cur_rk', 1)
    
    
    def get_min_rk():
        q = "SELECT MIN(RK) AS L_RK FROM B_DATA;"
        with connection.cursor() as cursor:
            cursor.execute(q)
            val = cursor.fetchall()
        return val[0][0]
    
    def get_max_rk():
        q = "SELECT MAX(RK) AS L_RK FROM B_DATA;"
        with connection.cursor() as cursor:
            cursor.execute(q)
            val = cursor.fetchall()
        return val[0][0]
    
    
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
        try:
            default_b_values = {
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
            }
            default_c_values = {
                'ime': cdata[0][2],
                'telefon': cdata[0][3],
            }
            
        except:
            default_b_values = {
                'RK': rk,
                'RN': None,
                'Marka': None,
                'Model': None,
                'G_PR': None,
                'KM': None,
                'Kupe': None,
                'Rama': None,
                'Dvigatel': None,
                'Descr': None,
                'Problem': None,
                'R_DATA': None,             
            }
            default_c_values = {
                'ime': None,
                'telefon': None,
            }
        return default_b_values, default_c_values
    
    
    
    if request.method == 'POST':
        '''RK = request.POST['RK']
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
        ime = request.POST['ime']
        telefon = request.POST['telefon']'''
        
        b_form = b_dataForm(request.POST)
        c_form = c_dataForm(request.POST)
        if b_form.is_valid() and c_form.is_valid():
            RK = b_form.cleaned_data['RK']
            RN = b_form.cleaned_data['RN']
            Marka = b_form.cleaned_data['Marka']
            Model = b_form.cleaned_data['Model']
            G_PR = b_form.cleaned_data['G_PR']
            KM = b_form.cleaned_data['KM']
            Kupe = b_form.cleaned_data['Kupe']
            Rama = b_form.cleaned_data['Rama']
            Dvigatel = b_form.cleaned_data['Dvigatel']
            Descr = b_form.cleaned_data['Descr']
            Problem = b_form.cleaned_data['Problem']
            R_DATA = b_form.cleaned_data['R_DATA']
            
            ime = c_form.cleaned_data['ime']
            telefon = c_form.cleaned_data['telefon']
        
        
        if cur_rk > get_max_rk():
            try:
                print("createEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
            
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
                new_c_data = c_data(
                    RK=RK,
                    ime=ime,
                    telefon=telefon,
                )
                
                new_b_data.save()
                new_c_data.save()
            except:
                pass
        else:
            print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSEEE")
            b = b_data.objects.filter(RK=cur_rk).first()
            c = c_data.objects.filter(RK=cur_rk).first()
            
    
    if request.method == 'GET':
        if request.GET.get('C', '') == '-1':
            cur_rk = get_min_rk()
                
        elif request.GET.get('C', '') == '-2':
            if cur_rk > get_min_rk():
                cur_rk -= 1
            
        elif request.GET.get('C', '') == '-3':
            if cur_rk < get_max_rk():
                cur_rk += 1
                
        elif request.GET.get('C', '') == '-4':
            cur_rk = get_max_rk()
        
        elif request.GET.get('C', '') == '0':
            newest_rk = get_max_rk()+1
            cur_rk =  newest_rk
            
        
    
    request.session['cur_rk'] = cur_rk
    initial_b, initial_c = get_db_data(cur_rk)
    b_form = b_dataForm(request.POST or None, initial = initial_b) 
    c_form = c_dataForm(request.POST or None, initial = initial_c) 
    search_form = searchForm(None) 
    context['b_form'] = b_form
    context['c_form'] = c_form
    context['search_form'] = search_form
    return render(request, "card.html", context)


def search(request):
    
    def create_full_table():
        q = "CREATE TABLE fulltable AS SELECT B_DATA.RK, B_DATA.RN, B_DATA.Marka, B_DATA.Model, B_DATA.G_PR, B_DATA.KM, B_DATA.Kupe, B_DATA.Rama, B_DATA.Dvigatel, B_DATA.R_DATA, B_DATA.Descr, B_DATA.Problem,"
        q += " C_DATA.ime, C_DATA.telefon"
        q += " FROM B_DATA INNER JOIN C_DATA ON B_DATA.RK = C_DATA.RK"
        q += " ORDER BY B_DATA.RK;"
        with connection.cursor() as cursor:
            cursor.execute(q)
            #full_table = cursor.fetchall()
            
    def drop_table(table):
        q = "DROP TABLE "
        q += table
        with connection.cursor() as cursor:
            cursor.execute(q)
            #res = cursor.fetchall()
            
            
    if request.method == 'GET':
        get_RN = request.GET.get('RN', '')
        get_ime = request.GET.get('ime', '')
        get_date1 = request.GET.get('date1', '')
        get_date2 = request.GET.get('date2', '')
        json_data = []
        where_clause = ""
        flag = 0
        try:
            drop_table('fulltable')
        except:
            pass
        if get_RN != '' or get_ime != '' or get_date1 != '' or get_date2 != '':
            where_clause+=" WHERE"
            if get_RN != '':
                flag+=1
            if get_ime != '':
                flag+=1
            if get_date1 != '':
                flag+=1
            if get_date2 != '':
                flag+=1
                
            if flag>0:
                
                if get_RN != '' and flag>=2:
                    where_clause+=" RN="
                    where_clause+=' "'
                    where_clause+=get_RN
                    where_clause+='"'
                    where_clause+=" AND "
                    flag-=1
                    
                elif get_RN != '':
                    where_clause+=" RN="
                    where_clause+=' "'
                    where_clause+=get_RN
                    where_clause+='"'
                    print("=====================================================")
                    print(where_clause)
                
                if get_ime != '' and flag>=2:
                    where_clause+=" ime="
                    where_clause+=' "'
                    where_clause+=get_ime
                    where_clause+='"'
                    where_clause+=" AND "
                    flag-=1
                elif get_ime != '':
                    where_clause+=" ime="
                    where_clause+=' "'
                    where_clause+=get_ime
                    where_clause+='"'
                    flag-=1
                    print("=====================================================")
                    print(where_clause)
                    
                if get_date1 != '' and flag>=2:
                    where_clause+=" R_DATA="
                    where_clause+=' "'
                    where_clause+=get_date1
                    where_clause+='"'
                    where_clause+=" AND "
                    flag-=1
                elif get_date1 != '':
                    where_clause+=" R_DATA="
                    where_clause+=' "'
                    where_clause+=get_date1
                    where_clause+='"'
                    flag-=1
                    print("=====================================================")
                    print(where_clause)
                    
                """"if get_date2 != '' and flag>=2:
                    where_clause+=" date2="
                    where_clause+=' "'
                    where_clause+=get_date2
                    where_clause+='"'
                    where_clause+=" AND "
                    flag-=1
                else:
                    where_clause+=get_date2"""

                    
            q = "CREATE TABLE fulltable AS SELECT B_DATA.RK, B_DATA.RN, B_DATA.Marka, B_DATA.Model, B_DATA.G_PR, B_DATA.KM, B_DATA.Kupe, B_DATA.Rama, B_DATA.Dvigatel, B_DATA.R_DATA, B_DATA.Descr, B_DATA.Problem,"
            q += " C_DATA.ime, C_DATA.telefon"
            q += " FROM B_DATA" 
            q += " INNER JOIN C_DATA ON B_DATA.RK = C_DATA.RK"
            q += where_clause
            q += " ORDER BY B_DATA.RK;"
            with connection.cursor() as cursor:
                cursor.execute(q)
        else:
            create_full_table()
            
            
            
        q = "SELECT * FROM fulltable"
        with connection.cursor() as cursor:
            cursor.execute(q)
            table = cursor.fetchall()
            print(table)
                
        
    return render(request, "search.html", {})