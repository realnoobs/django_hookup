import django_hookup


@django_hookup.register("register_foobar", order=1)
def say_foo(text):
    """Concat foo and given text"""
    return "foo:%s " % text


@django_hookup.register("register_foobar", order=0)
def say_bar(text):
    """Concat bar and given text"""
    return "bar:%s " % text
