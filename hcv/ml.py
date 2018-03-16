from django.http import JsonResponse
from hcv.svm import calculate1
from hcv.knn import calculate2


def ml_calculate(request):
    data = {'params':request.GET['key']}

    data['knn']=calculate1(1,1,1)
    data['svm']=calculate2(2,2,2)

    if request.method == 'GET':
        data['method'] = 'GET'

    elif request.method == 'POST':
        data['method'] = 'POST'

    return   JsonResponse(data)
