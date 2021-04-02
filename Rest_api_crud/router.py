from employeeapi import viewsets
from rest_framework import routers
router =routers.DefaultRouter()
router.register("employee",viewsets.EmployeeViewSets)

#get post update Delete
#list retrive