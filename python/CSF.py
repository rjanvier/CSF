# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _CSF
else:
    import _CSF

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _CSF.delete_SwigPyIterator

    def value(self):
        return _CSF.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _CSF.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _CSF.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _CSF.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _CSF.SwigPyIterator_equal(self, x)

    def copy(self):
        return _CSF.SwigPyIterator_copy(self)

    def next(self):
        return _CSF.SwigPyIterator_next(self)

    def __next__(self):
        return _CSF.SwigPyIterator___next__(self)

    def previous(self):
        return _CSF.SwigPyIterator_previous(self)

    def advance(self, n):
        return _CSF.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _CSF.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _CSF.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _CSF.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _CSF.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _CSF.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _CSF.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _CSF:
_CSF.SwigPyIterator_swigregister(SwigPyIterator)
class VecInt(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _CSF.VecInt_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _CSF.VecInt___nonzero__(self)

    def __bool__(self):
        return _CSF.VecInt___bool__(self)

    def __len__(self):
        return _CSF.VecInt___len__(self)

    def __getslice__(self, i, j):
        return _CSF.VecInt___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _CSF.VecInt___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _CSF.VecInt___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _CSF.VecInt___delitem__(self, *args)

    def __getitem__(self, *args):
        return _CSF.VecInt___getitem__(self, *args)

    def __setitem__(self, *args):
        return _CSF.VecInt___setitem__(self, *args)

    def pop(self):
        return _CSF.VecInt_pop(self)

    def append(self, x):
        return _CSF.VecInt_append(self, x)

    def empty(self):
        return _CSF.VecInt_empty(self)

    def size(self):
        return _CSF.VecInt_size(self)

    def swap(self, v):
        return _CSF.VecInt_swap(self, v)

    def begin(self):
        return _CSF.VecInt_begin(self)

    def end(self):
        return _CSF.VecInt_end(self)

    def rbegin(self):
        return _CSF.VecInt_rbegin(self)

    def rend(self):
        return _CSF.VecInt_rend(self)

    def clear(self):
        return _CSF.VecInt_clear(self)

    def get_allocator(self):
        return _CSF.VecInt_get_allocator(self)

    def pop_back(self):
        return _CSF.VecInt_pop_back(self)

    def erase(self, *args):
        return _CSF.VecInt_erase(self, *args)

    def __init__(self, *args):
        _CSF.VecInt_swiginit(self, _CSF.new_VecInt(*args))

    def push_back(self, x):
        return _CSF.VecInt_push_back(self, x)

    def front(self):
        return _CSF.VecInt_front(self)

    def back(self):
        return _CSF.VecInt_back(self)

    def assign(self, n, x):
        return _CSF.VecInt_assign(self, n, x)

    def resize(self, *args):
        return _CSF.VecInt_resize(self, *args)

    def insert(self, *args):
        return _CSF.VecInt_insert(self, *args)

    def reserve(self, n):
        return _CSF.VecInt_reserve(self, n)

    def capacity(self):
        return _CSF.VecInt_capacity(self)
    __swig_destroy__ = _CSF.delete_VecInt

# Register VecInt in _CSF:
_CSF.VecInt_swigregister(VecInt)
class VecFloat(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _CSF.VecFloat_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _CSF.VecFloat___nonzero__(self)

    def __bool__(self):
        return _CSF.VecFloat___bool__(self)

    def __len__(self):
        return _CSF.VecFloat___len__(self)

    def __getslice__(self, i, j):
        return _CSF.VecFloat___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _CSF.VecFloat___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _CSF.VecFloat___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _CSF.VecFloat___delitem__(self, *args)

    def __getitem__(self, *args):
        return _CSF.VecFloat___getitem__(self, *args)

    def __setitem__(self, *args):
        return _CSF.VecFloat___setitem__(self, *args)

    def pop(self):
        return _CSF.VecFloat_pop(self)

    def append(self, x):
        return _CSF.VecFloat_append(self, x)

    def empty(self):
        return _CSF.VecFloat_empty(self)

    def size(self):
        return _CSF.VecFloat_size(self)

    def swap(self, v):
        return _CSF.VecFloat_swap(self, v)

    def begin(self):
        return _CSF.VecFloat_begin(self)

    def end(self):
        return _CSF.VecFloat_end(self)

    def rbegin(self):
        return _CSF.VecFloat_rbegin(self)

    def rend(self):
        return _CSF.VecFloat_rend(self)

    def clear(self):
        return _CSF.VecFloat_clear(self)

    def get_allocator(self):
        return _CSF.VecFloat_get_allocator(self)

    def pop_back(self):
        return _CSF.VecFloat_pop_back(self)

    def erase(self, *args):
        return _CSF.VecFloat_erase(self, *args)

    def __init__(self, *args):
        _CSF.VecFloat_swiginit(self, _CSF.new_VecFloat(*args))

    def push_back(self, x):
        return _CSF.VecFloat_push_back(self, x)

    def front(self):
        return _CSF.VecFloat_front(self)

    def back(self):
        return _CSF.VecFloat_back(self)

    def assign(self, n, x):
        return _CSF.VecFloat_assign(self, n, x)

    def resize(self, *args):
        return _CSF.VecFloat_resize(self, *args)

    def insert(self, *args):
        return _CSF.VecFloat_insert(self, *args)

    def reserve(self, n):
        return _CSF.VecFloat_reserve(self, n)

    def capacity(self):
        return _CSF.VecFloat_capacity(self)
    __swig_destroy__ = _CSF.delete_VecFloat

# Register VecFloat in _CSF:
_CSF.VecFloat_swigregister(VecFloat)
class VecVecFloat(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _CSF.VecVecFloat_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _CSF.VecVecFloat___nonzero__(self)

    def __bool__(self):
        return _CSF.VecVecFloat___bool__(self)

    def __len__(self):
        return _CSF.VecVecFloat___len__(self)

    def __getslice__(self, i, j):
        return _CSF.VecVecFloat___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _CSF.VecVecFloat___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _CSF.VecVecFloat___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _CSF.VecVecFloat___delitem__(self, *args)

    def __getitem__(self, *args):
        return _CSF.VecVecFloat___getitem__(self, *args)

    def __setitem__(self, *args):
        return _CSF.VecVecFloat___setitem__(self, *args)

    def pop(self):
        return _CSF.VecVecFloat_pop(self)

    def append(self, x):
        return _CSF.VecVecFloat_append(self, x)

    def empty(self):
        return _CSF.VecVecFloat_empty(self)

    def size(self):
        return _CSF.VecVecFloat_size(self)

    def swap(self, v):
        return _CSF.VecVecFloat_swap(self, v)

    def begin(self):
        return _CSF.VecVecFloat_begin(self)

    def end(self):
        return _CSF.VecVecFloat_end(self)

    def rbegin(self):
        return _CSF.VecVecFloat_rbegin(self)

    def rend(self):
        return _CSF.VecVecFloat_rend(self)

    def clear(self):
        return _CSF.VecVecFloat_clear(self)

    def get_allocator(self):
        return _CSF.VecVecFloat_get_allocator(self)

    def pop_back(self):
        return _CSF.VecVecFloat_pop_back(self)

    def erase(self, *args):
        return _CSF.VecVecFloat_erase(self, *args)

    def __init__(self, *args):
        _CSF.VecVecFloat_swiginit(self, _CSF.new_VecVecFloat(*args))

    def push_back(self, x):
        return _CSF.VecVecFloat_push_back(self, x)

    def front(self):
        return _CSF.VecVecFloat_front(self)

    def back(self):
        return _CSF.VecVecFloat_back(self)

    def assign(self, n, x):
        return _CSF.VecVecFloat_assign(self, n, x)

    def resize(self, *args):
        return _CSF.VecVecFloat_resize(self, *args)

    def insert(self, *args):
        return _CSF.VecVecFloat_insert(self, *args)

    def reserve(self, n):
        return _CSF.VecVecFloat_reserve(self, n)

    def capacity(self):
        return _CSF.VecVecFloat_capacity(self)
    __swig_destroy__ = _CSF.delete_VecVecFloat

# Register VecVecFloat in _CSF:
_CSF.VecVecFloat_swigregister(VecVecFloat)
class VecDouble(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _CSF.VecDouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _CSF.VecDouble___nonzero__(self)

    def __bool__(self):
        return _CSF.VecDouble___bool__(self)

    def __len__(self):
        return _CSF.VecDouble___len__(self)

    def __getslice__(self, i, j):
        return _CSF.VecDouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _CSF.VecDouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _CSF.VecDouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _CSF.VecDouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _CSF.VecDouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _CSF.VecDouble___setitem__(self, *args)

    def pop(self):
        return _CSF.VecDouble_pop(self)

    def append(self, x):
        return _CSF.VecDouble_append(self, x)

    def empty(self):
        return _CSF.VecDouble_empty(self)

    def size(self):
        return _CSF.VecDouble_size(self)

    def swap(self, v):
        return _CSF.VecDouble_swap(self, v)

    def begin(self):
        return _CSF.VecDouble_begin(self)

    def end(self):
        return _CSF.VecDouble_end(self)

    def rbegin(self):
        return _CSF.VecDouble_rbegin(self)

    def rend(self):
        return _CSF.VecDouble_rend(self)

    def clear(self):
        return _CSF.VecDouble_clear(self)

    def get_allocator(self):
        return _CSF.VecDouble_get_allocator(self)

    def pop_back(self):
        return _CSF.VecDouble_pop_back(self)

    def erase(self, *args):
        return _CSF.VecDouble_erase(self, *args)

    def __init__(self, *args):
        _CSF.VecDouble_swiginit(self, _CSF.new_VecDouble(*args))

    def push_back(self, x):
        return _CSF.VecDouble_push_back(self, x)

    def front(self):
        return _CSF.VecDouble_front(self)

    def back(self):
        return _CSF.VecDouble_back(self)

    def assign(self, n, x):
        return _CSF.VecDouble_assign(self, n, x)

    def resize(self, *args):
        return _CSF.VecDouble_resize(self, *args)

    def insert(self, *args):
        return _CSF.VecDouble_insert(self, *args)

    def reserve(self, n):
        return _CSF.VecDouble_reserve(self, n)

    def capacity(self):
        return _CSF.VecDouble_capacity(self)
    __swig_destroy__ = _CSF.delete_VecDouble

# Register VecDouble in _CSF:
_CSF.VecDouble_swigregister(VecDouble)
class Params(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    bSloopSmooth = property(_CSF.Params_bSloopSmooth_get, _CSF.Params_bSloopSmooth_set)
    time_step = property(_CSF.Params_time_step_get, _CSF.Params_time_step_set)
    class_threshold = property(_CSF.Params_class_threshold_get, _CSF.Params_class_threshold_set)
    cloth_resolution = property(_CSF.Params_cloth_resolution_get, _CSF.Params_cloth_resolution_set)
    rigidness = property(_CSF.Params_rigidness_get, _CSF.Params_rigidness_set)
    interations = property(_CSF.Params_interations_get, _CSF.Params_interations_set)

    def __init__(self):
        _CSF.Params_swiginit(self, _CSF.new_Params())
    __swig_destroy__ = _CSF.delete_Params

# Register Params in _CSF:
_CSF.Params_swigregister(Params)
class CSF(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _CSF.CSF_swiginit(self, _CSF.new_CSF(*args))
    __swig_destroy__ = _CSF.delete_CSF

    def readPointsFromFile(self, filename):
        return _CSF.CSF_readPointsFromFile(self, filename)

    def getPointCloud(self, *args):
        return _CSF.CSF_getPointCloud(self, *args)

    def savePoints(self, grp, path):
        return _CSF.CSF_savePoints(self, grp, path)

    def size(self):
        return _CSF.CSF_size(self)

    def setPointCloud(self, *args):
        return _CSF.CSF_setPointCloud(self, *args)

    def do_filtering(self, *args):
        return _CSF.CSF_do_filtering(self, *args)
    params = property(_CSF.CSF_params_get, _CSF.CSF_params_set)
    index = property(_CSF.CSF_index_get, _CSF.CSF_index_set)

# Register CSF in _CSF:
_CSF.CSF_swigregister(CSF)

