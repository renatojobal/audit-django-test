from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
# router.register('users', views.UserViewset, base_name='user') # ! Se pernolizaron las views de Users

router.register('roles', views.RoleViewset)
router.register('cities', views.CityViewset)
router.register('userRoles', views.UserRoleViewset)
router.register('touristPoint', views.TouristPointViewset)
router.register('restaurant', views.RestaurantViewset)
router.register('route', views.RouteViewset)
router.register('prize', views.PrizeViewset)
router.register('touristPointRoute', views.TouristPointRouteViewset)
