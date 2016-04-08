import functools
import inspect
import itertools
import operator
import sys

from .compatibility import PY3

if PY3:  # pragma: py2 no cover
    import builtins
else:  # pragma: py3 no cover
    import __builtin__ as builtins

module_info = {}

module_info[builtins] = dict(
    abs=[
        lambda x: None],
    all=[
        lambda iterable: None],
    any=[
        lambda iterable: None],
    apply=[
        lambda object: None,
        lambda object, args: None,
        lambda object, args, kwargs: None],
    ascii=[
        lambda obj: None],
    bin=[
        lambda number: None],
    bool=[
        lambda x=False: None],
    buffer=[
        lambda object: None,
        lambda object, offset: None,
        lambda object, offset, size: None],
    bytearray=[
        lambda: None,
        lambda int: None,
        lambda string, encoding='utf8', errors='strict': None],
    callable=[
        lambda obj: None],
    chr=[
        lambda i: None],
    classmethod=[
        lambda function: None],
    cmp=[
        lambda x, y: None],
    coerce=[
        lambda x, y: None],
    complex=[
        lambda real=0, imag=0: None],
    delattr=[
        lambda obj, name: None],
    dict=[
        lambda **kwargs: None,
        lambda mapping, **kwargs: None],
    dir=[
        lambda: None,
        lambda object: None],
    divmod=[
        lambda x, y: None],
    enumerate=[
        (0, lambda iterable, start=0: None)],
    eval=[
        lambda source: None,
        lambda source, globals: None,
        lambda source, globals, locals: None],
    execfile=[
        lambda filename: None,
        lambda filename, globals: None,
        lambda filename, globals, locals: None],
    file=[
        (0, lambda name, mode='r', buffering=-1: None)],
    filter=[
        lambda function, iterable: None],
    float=[
        lambda x=0.0: None],
    format=[
        lambda value: None,
        lambda value, format_spec: None],
    frozenset=[
        lambda: None,
        lambda iterable: None],
    getattr=[
        lambda object, name: None,
        lambda object, name, default: None],
    globals=[
        lambda: None],
    hasattr=[
        lambda obj, name: None],
    hash=[
        lambda obj: None],
    hex=[
        lambda number: None],
    id=[
        lambda obj: None],
    input=[
        lambda: None,
        lambda prompt: None],
    int=[
        lambda x=0: None,
        (0, lambda x, base=10: None)],
    intern=[
        lambda string: None],
    isinstance=[
        lambda obj, class_or_tuple: None],
    issubclass=[
        lambda cls, class_or_tuple: None],
    iter=[
        lambda iterable: None,
        lambda callable, sentinel: None],
    len=[
        lambda obj: None],
    list=[
        lambda: None,
        lambda iterable: None],
    locals=[
        lambda: None],
    long=[
        lambda x=0: None,
        (0, lambda x, base=10: None)],
    map=[
        lambda func, sequence, *iterables: None],
    memoryview=[
        (0, lambda object: None)],
    next=[
        lambda iterator: None,
        lambda iterator, default: None],
    object=[
        lambda: None],
    oct=[
        lambda number: None],
    ord=[
        lambda c: None],
    pow=[
        lambda x, y: None,
        lambda x, y, z: None],
    property=[
        lambda fget=None, fset=None, fdel=None, doc=None: None],
    range=[
        lambda stop: None,
        lambda start, stop: None,
        lambda start, stop, step: None],
    raw_input=[
        lambda: None,
        lambda prompt: None],
    reduce=[
        lambda function, sequence: None,
        lambda function, sequence, initial: None],
    reload=[
        lambda module: None],
    repr=[
        lambda obj: None],
    reversed=[
        lambda sequence: None],
    round=[
        (0, lambda number, ndigits=0: None)],
    set=[
        lambda: None,
        lambda iterable: None],
    setattr=[
        lambda obj, name, value: None],
    slice=[
        lambda stop: None,
        lambda start, stop: None,
        lambda start, stop, step: None],
    staticmethod=[
        lambda function: None],
    sum=[
        lambda iterable: None,
        lambda iterable, start: None],
    super=[
        lambda type: None,
        lambda type, obj: None],
    tuple=[
        lambda: None,
        lambda iterable: None],
    type=[
        lambda object: None,
        lambda name, bases, dict: None],
    unichr=[
        lambda i: None],
    unicode=[
        lambda object: None,
        lambda string='', encoding='utf8', errors='strict': None],
    vars=[
        lambda: None,
        lambda object: None],
    xrange=[
        lambda stop: None,
        lambda start, stop: None,
        lambda start, stop, step: None],
    zip=[
        lambda *iterables: None],
)
module_info[builtins]['exec'] = [
    lambda source: None,
    lambda source, globals: None,
    lambda source, globals, locals: None]

if PY3:  # pragma: py2 no cover
    module_info[builtins].update(
        bytes=[
            lambda: None,
            lambda int: None,
            lambda string, encoding='utf8', errors='strict': None],
        compile=[
            (0, lambda source, filename, mode, flags=0,
                dont_inherit=False, optimize=-1: None)],
        max=[
            (1, lambda iterable: None, ('default', 'key',)),
            (1, lambda arg1, arg2, *args: None, ('key',))],
        min=[
            (1, lambda iterable: None, ('default', 'key',)),
            (1, lambda arg1, arg2, *args: None, ('key',))],
        open=[
            (0, lambda file, mode='r', buffering=-1, encoding=None,
                errors=None, newline=None, closefd=True, opener=None: None)],
        sorted=[
            lambda iterable, key=None, reverse=False: None],
        str=[
            lambda object='', encoding='utf', errors='strict': None],
    )
    module_info[builtins]['print'] = [
        (0, lambda *args: None, ('sep', 'end', 'file', 'flush',))]

else:  # pragma: py3 no cover
    module_info[builtins].update(
        bytes=[
            lambda object='': None],
        compile=[
            (0, lambda source, filename, mode, flags=0,
                dont_inherit=False: None)],
        max=[
            (1, lambda iterable, *args: None, ('key',))],
        min=[
            (1, lambda iterable, *args: None, ('key',))],
        open=[
            (0, lambda file, mode='r', buffering=-1: None)],
        sorted=[
            lambda iterable, cmp=None, key=None, reverse=False: None],
        str=[
            lambda object='': None],
    )
    module_info[builtins]['print'] = [
        (0, lambda *args: None, ('sep', 'end', 'file',))]

module_info[functools] = dict(
    cmp_to_key=[
        (0, lambda mycmp: None)],
    partial=[
        lambda func, *args, **kwargs: None],
    partialmethod=[
        lambda func, *args, **kwargs: None],
    reduce=[
        lambda function, sequence: None,
        lambda function, sequence, initial: None],
)

module_info[itertools] = dict(
    accumulate=[
        (0, lambda iterable, func=None: None)],
    chain=[
        lambda *iterables: None],
    combinations=[
        (0, lambda iterable, r: None)],
    combinations_with_replacement=[
        (0, lambda iterable, r: None)],
    compress=[
        (0, lambda data, selectors: None)],
    count=[
        lambda start=0, step=1: None],
    cycle=[
        lambda iterable: None],
    dropwhile=[
        lambda predicate, iterable: None],
    filterfalse=[
        lambda function, sequence: None],
    groupby=[
        (0, lambda iterable, key=None: None)],
    ifilter=[
        lambda function, sequence: None],
    ifilterfalse=[
        lambda function, sequence: None],
    imap=[
        lambda func, sequence, *iterables: None],
    islice=[
        lambda iterable, stop: None,
        lambda iterable, start, stop: None,
        lambda iterable, start, stop, step: None],
    izip=[
        lambda *iterables: None],
    izip_longest=[
        (0, lambda *iterables: None, ('fillvalue',))],
    permutations=[
        (0, lambda iterable, r=0: None)],
    repeat=[
        (0, lambda object, times=0: None)],
    starmap=[
        lambda function, sequence: None],
    takewhile=[
        lambda predicate, iterable: None],
    tee=[
        lambda iterable: None,
        lambda iterable, n: None],
    zip_longest=[
        (0, lambda *iterables: None, ('fillvalue',))],
)

if PY3:  # pragma: py2 no cover
    module_info[itertools].update(
        product=[
            (0, lambda *iterables: None, ('repeat',))],
    )
else:  # pragma: py3 no cover
    module_info[itertools].update(
        product=[
            lambda *iterables: None],
    )

module_info[operator] = dict(
    __abs__=[
        lambda a: None],
    __add__=[
        lambda a, b: None],
    __and__=[
        lambda a, b: None],
    __concat__=[
        lambda a, b: None],
    __contains__=[
        lambda a, b: None],
    __delitem__=[
        lambda a, b: None],
    __delslice__=[
        lambda a, b, c: None],
    __div__=[
        lambda a, b: None],
    __eq__=[
        lambda a, b: None],
    __floordiv__=[
        lambda a, b: None],
    __ge__=[
        lambda a, b: None],
    __getitem__=[
        lambda a, b: None],
    __getslice__=[
        lambda a, b, c: None],
    __gt__=[
        lambda a, b: None],
    __iadd__=[
        lambda a, b: None],
    __iand__=[
        lambda a, b: None],
    __iconcat__=[
        lambda a, b: None],
    __idiv__=[
        lambda a, b: None],
    __ifloordiv__=[
        lambda a, b: None],
    __ilshift__=[
        lambda a, b: None],
    __imatmul__=[
        lambda a, b: None],
    __imod__=[
        lambda a, b: None],
    __imul__=[
        lambda a, b: None],
    __index__=[
        lambda a: None],
    __inv__=[
        lambda a: None],
    __invert__=[
        lambda a: None],
    __ior__=[
        lambda a, b: None],
    __ipow__=[
        lambda a, b: None],
    __irepeat__=[
        lambda a, b: None],
    __irshift__=[
        lambda a, b: None],
    __isub__=[
        lambda a, b: None],
    __itruediv__=[
        lambda a, b: None],
    __ixor__=[
        lambda a, b: None],
    __le__=[
        lambda a, b: None],
    __lshift__=[
        lambda a, b: None],
    __lt__=[
        lambda a, b: None],
    __matmul__=[
        lambda a, b: None],
    __mod__=[
        lambda a, b: None],
    __mul__=[
        lambda a, b: None],
    __ne__=[
        lambda a, b: None],
    __neg__=[
        lambda a: None],
    __not__=[
        lambda a: None],
    __or__=[
        lambda a, b: None],
    __pos__=[
        lambda a: None],
    __pow__=[
        lambda a, b: None],
    __repeat__=[
        lambda a, b: None],
    __rshift__=[
        lambda a, b: None],
    __setitem__=[
        lambda a, b, c: None],
    __setslice__=[
        lambda a, b, c, d: None],
    __sub__=[
        lambda a, b: None],
    __truediv__=[
        lambda a, b: None],
    __xor__=[
        lambda a, b: None],
    _abs=[
        lambda x: None],
    _compare_digest=[
        lambda a, b: None],
    abs=[
        lambda a: None],
    add=[
        lambda a, b: None],
    and_=[
        lambda a, b: None],
    attrgetter=[
        lambda attr, *args: None],
    concat=[
        lambda a, b: None],
    contains=[
        lambda a, b: None],
    countOf=[
        lambda a, b: None],
    delitem=[
        lambda a, b: None],
    delslice=[
        lambda a, b, c: None],
    div=[
        lambda a, b: None],
    eq=[
        lambda a, b: None],
    floordiv=[
        lambda a, b: None],
    ge=[
        lambda a, b: None],
    getitem=[
        lambda a, b: None],
    getslice=[
        lambda a, b, c: None],
    gt=[
        lambda a, b: None],
    iadd=[
        lambda a, b: None],
    iand=[
        lambda a, b: None],
    iconcat=[
        lambda a, b: None],
    idiv=[
        lambda a, b: None],
    ifloordiv=[
        lambda a, b: None],
    ilshift=[
        lambda a, b: None],
    imatmul=[
        lambda a, b: None],
    imod=[
        lambda a, b: None],
    imul=[
        lambda a, b: None],
    index=[
        lambda a: None],
    indexOf=[
        lambda a, b: None],
    inv=[
        lambda a: None],
    invert=[
        lambda a: None],
    ior=[
        lambda a, b: None],
    ipow=[
        lambda a, b: None],
    irepeat=[
        lambda a, b: None],
    irshift=[
        lambda a, b: None],
    is_=[
        lambda a, b: None],
    is_not=[
        lambda a, b: None],
    isCallable=[
        lambda a: None],
    isMappingType=[
        lambda a: None],
    isNumberType=[
        lambda a: None],
    isSequenceType=[
        lambda a: None],
    isub=[
        lambda a, b: None],
    itemgetter=[
        lambda item, *args: None],
    itruediv=[
        lambda a, b: None],
    ixor=[
        lambda a, b: None],
    le=[
        lambda a, b: None],
    length_hint=[
        lambda obj: None,
        lambda obj, default: None],
    lshift=[
        lambda a, b: None],
    lt=[
        lambda a, b: None],
    matmul=[
        lambda a, b: None],
    methodcaller=[
        lambda name, *args, **kwargs: None],
    mod=[
        lambda a, b: None],
    mul=[
        lambda a, b: None],
    ne=[
        lambda a, b: None],
    neg=[
        lambda a: None],
    not_=[
        lambda a: None],
    or_=[
        lambda a, b: None],
    pos=[
        lambda a: None],
    pow=[
        lambda a, b: None],
    repeat=[
        lambda a, b: None],
    rshift=[
        lambda a, b: None],
    sequenceIncludes=[
        lambda a, b: None],
    setitem=[
        lambda a, b, c: None],
    setslice=[
        lambda a, b, c, d: None],
    sub=[
        lambda a, b: None],
    truediv=[
        lambda a, b: None],
    truth=[
        lambda a: None],
    xor=[
        lambda a, b: None],
)

if PY3:  # pragma: py2 no cover
    def num_pos_args(func):
        sig = inspect.signature(func)
        return sum(1 for x in sig.parameters.values()
                   if x.kind == x.POSITIONAL_OR_KEYWORD and
                   x.default is x.empty)

else:  # pragma: py3 no cover
    def num_pos_args(func):
        spec = inspect.getargspec(func)
        if spec.defaults:
            return len(spec.args) - len(spec.defaults)
        return len(spec.args)


def expand_sig(sig):
    if isinstance(sig, tuple):
        if len(sig) == 3:
            assert isinstance(sig[-1], tuple)
            return sig
        num_pos_only, func = sig
    else:
        func = sig
        num_pos_only = num_pos_args(func)
    return (num_pos_only, func, ())


signatures = {}
for module, info in module_info.items():
    for name, sigs in info.items():
        if hasattr(module, name):
            new_sigs = tuple(expand_sig(sig) for sig in sigs)
            signatures[getattr(module, name)] = new_sigs


def check_valid(sig, args, kwargs):
    num_pos_only, func, keyword_only = sig
    if len(args) < num_pos_only:
        return False
    if keyword_only:
        kwargs = dict(kwargs)
        for item in keyword_only:
            kwargs.pop(item, None)
    return is_valid_args(func, args, kwargs)


def check_partial(sig, args, kwargs):
    num_pos_only, func, keyword_only = sig
    if len(args) < num_pos_only:
        pad = (None,) * (num_pos_only - len(args))
        args = args + pad
    if keyword_only:
        kwargs = dict(kwargs)
        for item in keyword_only:
            kwargs.pop(item, None)
    return is_partial_args(func, args, kwargs)


def is_builtin_valid_args(func, args, kwargs):
    if func not in signatures:
        return None
    sigs = signatures[func]
    return any(check_valid(sig, args, kwargs) for sig in sigs)


def is_builtin_partial_args(func, args, kwargs):
    if func not in signatures:
        return None
    sigs = signatures[func]
    return any(check_partial(sig, args, kwargs) for sig in sigs)


if PY3:  # pragma: py2 no cover
    def has_unknown_args(func):
        if func in signatures:
            return False
        try:
            sig = inspect.signature(func)
        except ValueError:
            return True
        except TypeError:
            return False
        try:
            return any(x.kind == x.VAR_POSITIONAL
                       for x in sig.parameters.values())
        except AttributeError:  # pragma: no cover
            return False

else:  # pragma: py3 no cover
    def has_unknown_args(func):
        if func in signatures:
            return False
        try:
            spec = inspect.getargspec(func)
        except TypeError:
            return callable(func)
        return spec.varargs is not None


from .functoolz import is_valid_args, is_partial_args
