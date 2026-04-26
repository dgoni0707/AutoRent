from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
import os
import django

# СНАЧАЛА настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# ПОТОМ импортируем Django модели

User = get_user_model()

# Admin
admin, created = User.objects.get_or_create(username='admin')
admin.set_password('admin123')
admin.is_superuser = True
admin.is_staff = True
admin.save()
print("Admin: login='admin', password='admin123'")

# Manager
manager_group, _ = Group.objects.get_or_create(name='Manager')
manager, created = User.objects.get_or_create(username='manager')
manager.set_password('manager123')
manager.is_superuser = False
manager.is_staff = False
manager.save()
manager.groups.add(manager_group)

# Assign Permissions
apps_to_allow = ['customers', 'documents', 'payments']

for app in apps_to_allow:
    content_types = ContentType.objects.filter(app_label=app)
    for ct in content_types:
        perms = Permission.objects.filter(content_type=ct)
        for perm in perms:
            if app == 'documents' and ('change' in perm.codename or 'delete' in perm.codename):
                continue
            manager_group.permissions.add(perm)

print("Manager created successfully")
