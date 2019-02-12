from django.shortcuts import redirect

def authenticated_as_player(function):
    def wrap(request, *args, **kwargs):

        if request.user.is_authenticated:
            try:
                request.user.player
            except AttributeError:
                return redirect('/login')
        else:
            return redirect('/login')

        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def authenticated_as_admin(function):
    def wrap(request, *args, **kwargs):

        if request.user.is_staff:
            pass
        else:
            return redirect('/login')

        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
