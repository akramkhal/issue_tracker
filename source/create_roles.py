from django.contrib.auth.models import Group, Permission, User
from webapp.models import Project

ROLES = {
    'Менеджер проекта': ['add_project', 'change_project', 'delete_project',
                         'add_task', 'change_task', 'delete_task', 'change_project_users'],
    'Капитан': ['add_task', 'change_task', 'delete_task', 'change_project_users'],
    'Разработчик': ['add_task', 'change_task'],
}

USERS = {
    'manager': 'Менеджер проекта',
    'lead': 'Капитан',
    'dev': 'Разработчик',
}

for group_name, codenames in ROLES.items():
    group, created = Group.objects.get_or_create(name=group_name)
    permissions = Permission.objects.filter(content_type__app_label='webapp', codename__in=codenames)
    group.permissions.set(permissions)
    print(group_name, '-', permissions.count(), 'разрешений')

first_project = Project.objects.order_by('pk').first()

for username, group_name in USERS.items():
    user, created = User.objects.get_or_create(username=username)
    user.set_password(username)
    user.save()
    user.groups.set([Group.objects.get(name=group_name)])
    first_project.users.add(user)
    print(username, '-', group_name)

print('Пользователи добавлены в проект:', first_project.name)