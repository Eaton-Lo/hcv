from django.http import JsonResponse
from hcv.svm import calculate1
from hcv.knn import calculate2


def ml_calculate(request):
    data = {'params':request.GET['key']}
    params1 = request.GET['params1']
    params2 = request.GET['params2']
    params3 = request.GET['params3']
    params4 = request.GET['params4']
    params5 = request.GET['params5']

    data['knn']=calculate1(float(params1),float(params2),float(params3))
    data['svm']=calculate2(float(params4),float(params5),float(params5))

    if request.method == 'GET':
        data['method'] = 'GET'

    elif request.method == 'POST':
        data['method'] = 'POST'

    return   JsonResponse(data)
