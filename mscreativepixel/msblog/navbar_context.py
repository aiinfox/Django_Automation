from .models import HeaderNavs

def loadNavItems(context):
    navitems = HeaderNavs.objects.all()[:10]  #Limit to 10 for now
    return {'navitems': navitems}