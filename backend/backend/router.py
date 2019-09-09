from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register('users', views.UserViewset, base_name='user')
router.register('roles', views.RoleViewset)
router.register('cities', views.CityViewset)
router.register('userroles', views.UserRoleViewset)