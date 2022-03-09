import django_hookup


@django_hookup.register("register_foo", order=1)
def say_foo(text):
    """Concat foo and given text"""
    return "foo:%s " % text


@django_hookup.register("register_bar", order=0)
def say_bar(text):
    """Concat bar and given text"""
    return "bar:%s " % text


@django_hookup.register(["register_foo", "register_bar"], order=0)
def say_foobar(text):
    """Concat bar and given text"""
    return "foobar:%s " % text
