from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from django.http import JsonResponse
from .serializer import DepositProductsListSerializer, DepositOptionsListSerializer
from .models import DepositProducts, DespositOptions

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

def api(request):
    url = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(url, params=params).json()
    return JsonResponse(response)

@api_view(['GET',])
def save_deposit_products(request):
    url = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(url, params=params).json()

    for li in response["result"].get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')  # 금융 상품 코드
        kor_co_nm = li.get('kor_co_nm') # 금융 회사명
        fin_prdt_nm = li.get('fin_prdt_nm') # 금융 상품명
        etc_note = li.get('etc_note') # 금융 상품 설명
        join_deny = li.get('join_deny') # 가입제한
        join_member = li.get('join_member') # 가입 대상
        join_way = li.get('join_way') # 가입 방법
        spcl_cnd = li.get('spcl_cnd') # 우대조건

        if DepositProducts.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            kor_co_nm=kor_co_nm, 
            fin_prdt_nm=fin_prdt_nm,
            etc_note=etc_note, 
            join_deny=join_deny, 
            join_member=join_member, 
            join_way=join_way,
            spcl_cnd=spcl_cnd
            ):
            continue

        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm' : kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'etc_note' : etc_note,
            'join_deny' : join_deny,
            'join_member' : join_member,
            'join_way' : join_way,
            'spcl_cnd' : spcl_cnd
        }
        serializer = DepositProductsListSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
    for li in response["result"].get('optionList'):
       fin_prdt_cd = li.get('fin_prdt_cd')  # 금융 상품 코드
       intr_rate_type_nm = li.get('intr_rate_type_nm') # 저축금리 유형명
       intr_rate = li.get('intr_rate') # 저축 금리
       intr_rate2 = li.get('intr_rate2') # 최고우대금리
       save_trm = li.get('save_trm') # 저축 기간

       if DespositOptions.objects.filter(
           fin_prdt_cd=fin_prdt_cd,
           intr_rate_type_nm=intr_rate_type_nm, 
           intr_rate=intr_rate,
           intr_rate2=intr_rate2, 
           save_trm=save_trm, 
           ):
           continue
       
       save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'intr_rate_type_nm' : intr_rate_type_nm,
            'intr_rate' : intr_rate,
            'intr_rate2' : intr_rate2,
            'save_trm' : save_trm,
        }
       serializer = DepositOptionsListSerializer(data=save_data)
       if serializer.is_valid(raise_exception=True):
           serializer.save()
    return JsonResponse({"message" : "okay"})