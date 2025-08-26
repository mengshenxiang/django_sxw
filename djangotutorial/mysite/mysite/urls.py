# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from django.conf import settings  # 新增
from django.conf.urls import include  # 新增

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]

# 仅在 DEBUG 模式下添加 debug-toolbar 路由（关键）
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]