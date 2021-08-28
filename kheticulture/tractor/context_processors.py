from .models import Tractor


def tractor(request):
    return {'tractor': Tractor(request)}
