"""An example of using wrappers and decorators"""

import functools

user = {'username': 'jose', 'access_level': 'user'}

def make_secure(access_level): #to jest factory
    def decorator(func): #to jest decorator
        @functools.wraps(func)
        def secure_func(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                print("Sorry no permission")
        return secure_func
    return decorator



@make_secure('admin')
def get_admin_password():
    return 'admin: 1234'

@make_secure('user')
def get_dashboard_password():
    return 'user: user_password'

print(get_admin_password())
print(get_dashboard_password())