import pykokkos as pk


@pk.workunit
def reciprocal_impl_1d_double(tid: int, view: pk.View1D[pk.double]):
    view[tid] = 1 / view[tid] # type: ignore


@pk.workunit
def reciprocal_impl_1d_float(tid: int, view: pk.View1D[pk.float]):
    view[tid] = 1 / view[tid] # type: ignore


@pk.workunit
def reciprocal_impl_2d_double(tid: int, view: pk.View2D[pk.double]):
    for i in range(view.extent(1)): # type: ignore
        view[tid][i] = 1 / view[tid][i] # type: ignore


@pk.workunit
def reciprocal_impl_2d_float(tid: int, view: pk.View2D[pk.float]):
    for i in range(view.extent(1)): # type: ignore
        view[tid][i] = 1 / view[tid][i] # type: ignore


def reciprocal(view):
    """
    Return the reciprocal of the argument, element-wise.

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    y : pykokkos view
        Output view.

    Notes
    -----
    .. note::
        This function is not designed to work with integers.

    """
    # see gh-29 for some discussion of the dispatching
    # awkwardness used here
    if str(view.dtype) == "DataType.double" and len(view.shape) == 1:
        pk.parallel_for(view.shape[0], reciprocal_impl_1d_double, view=view)
    elif str(view.dtype) == "DataType.float" and len(view.shape) == 1:
        pk.parallel_for(view.shape[0], reciprocal_impl_1d_float, view=view)
    elif str(view.dtype) == "DataType.float" and len(view.shape) == 2:
        pk.parallel_for(view.shape[0], reciprocal_impl_2d_float, view=view)
    elif str(view.dtype) == "DataType.double" and len(view.shape) == 2:
        pk.parallel_for(view.shape[0], reciprocal_impl_2d_double, view=view)
    # NOTE: pretty awkward to both return the view
    # and operate on it in place; the former is closer
    # to NumPy semantics
    return view


@pk.workunit
def log_impl_1d_double(tid: int, view: pk.View1D[pk.double]):
    view[tid] = log(view[tid]) # type: ignore


@pk.workunit
def log_impl_1d_float(tid: int, view: pk.View1D[pk.float]):
    view[tid] = log(view[tid]) # type: ignore


def log(view):
    """
    Natural logarithm, element-wise.

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    y : pykokkos view
        Output view.

    """
    if str(view.dtype) == "DataType.double":
        pk.parallel_for(view.shape[0], log_impl_1d_double, view=view)
    elif str(view.dtype) == "DataType.float":
        pk.parallel_for(view.shape[0], log_impl_1d_float, view=view)
    return view


@pk.workunit
def sqrt_impl_1d_double(tid: int, view: pk.View1D[pk.double]):
    view[tid] = sqrt(view[tid]) # type: ignore


@pk.workunit
def sqrt_impl_1d_float(tid: int, view: pk.View1D[pk.float]):
    view[tid] = sqrt(view[tid]) # type: ignore


def sqrt(view):
    """
    Return the non-negative square root of the argument, element-wise.

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    y : pykokkos view
        Output view.

    Notes
    -----
    .. note::
        This function should exhibit the same branch cut behavior
        as the equivalent NumPy ufunc.
    """
    # TODO: support complex types when they
    # are available in pykokkos?
    if str(view.dtype) == "DataType.double":
        pk.parallel_for(view.shape[0], sqrt_impl_1d_double, view=view)
    elif str(view.dtype) == "DataType.float":
        pk.parallel_for(view.shape[0], sqrt_impl_1d_float, view=view)
    return view


@pk.workunit
def log2_impl_1d_double(tid: int, view: pk.View1D[pk.double]):
    view[tid] = log2(view[tid]) # type: ignore


@pk.workunit
def log2_impl_1d_float(tid: int, view: pk.View1D[pk.float]):
    view[tid] = log2(view[tid]) # type: ignore


def log2(view):
    """
    Base-2 logarithm, element-wise.

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    y : pykokkos view
        Output view.

    """
    if str(view.dtype) == "DataType.double":
        pk.parallel_for(view.shape[0], log2_impl_1d_double, view=view)
    elif str(view.dtype) == "DataType.float":
        pk.parallel_for(view.shape[0], log2_impl_1d_float, view=view)
    return view


@pk.workunit
def log10_impl_1d_double(tid: int, view: pk.View1D[pk.double]):
    view[tid] = log10(view[tid]) # type: ignore


@pk.workunit
def log10_impl_1d_float(tid: int, view: pk.View1D[pk.float]):
    view[tid] = log10(view[tid]) # type: ignore


def log10(view):
    """
    Base-10 logarithm, element-wise.

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    y : pykokkos view
        Output view.

    """
    if str(view.dtype) == "DataType.double":
        pk.parallel_for(view.shape[0], log10_impl_1d_double, view=view)
    elif str(view.dtype) == "DataType.float":
        pk.parallel_for(view.shape[0], log10_impl_1d_float, view=view)
    return view


@pk.workunit
def log1p_impl_1d_double(tid: int, view: pk.View1D[pk.double]):
    view[tid] = log1p(view[tid]) # type: ignore


@pk.workunit
def log1p_impl_1d_float(tid: int, view: pk.View1D[pk.float]):
    view[tid] = log1p(view[tid]) # type: ignore


def log1p(view):
    """
    Return the natural logarithm of one plus the input array, element-wise.

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    y : pykokkos view
        Output view.

    """
    if str(view.dtype) == "DataType.double":
        pk.parallel_for(view.shape[0], log1p_impl_1d_double, view=view)
    elif str(view.dtype) == "DataType.float":
        pk.parallel_for(view.shape[0], log1p_impl_1d_float, view=view)
    return view


@pk.workunit
def sign_impl_1d_double(tid: int, view: pk.View1D[pk.double]):
    if view[tid] > 0:
        view[tid] = 1
    elif view[tid] == 0:
        view[tid] = 0
    elif view[tid] < 0:
        view[tid] = -1
    else:
        view[tid] = nan("")


@pk.workunit
def sign_impl_1d_float(tid: int, view: pk.View1D[pk.float]):
    if view[tid] > 0:
        view[tid] = 1
    elif view[tid] == 0:
        view[tid] = 0
    elif view[tid] < 0:
        view[tid] = -1
    else:
        view[tid] = nan("")


def sign(view):
    if str(view.dtype) == "DataType.double":
        pk.parallel_for(view.shape[0], sign_impl_1d_double, view=view)
    elif str(view.dtype) == "DataType.float":
        pk.parallel_for(view.shape[0], sign_impl_1d_float, view=view)
    return view


@pk.workunit
def add_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.double], ):
    out[tid] = viewA[tid] + viewB[tid]


@pk.workunit
def add_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = viewA[tid] + viewB[tid]


def add(viewA, viewB):
    """
    Sums positionally corresponding elements
    of viewA with elements of viewB

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """

    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        out = pk.View([viewA.shape[0]], pk.double)
        pk.parallel_for(
            viewA.shape[0],
            add_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        out = pk.View([viewA.shape[0]], pk.float)
        pk.parallel_for(
            viewA.shape[0],
            add_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def multiply_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = viewA[tid] * viewB[tid]


@pk.workunit
def multiply_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = viewA[tid] * viewB[tid]


def multiply(viewA, viewB):
    """
    Multiplies positionally corresponding elements
    of viewA with elements of viewB

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """

    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        out = pk.View([viewA.shape[0]], pk.double)
        pk.parallel_for(
            viewA.shape[0],
            multiply_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        out = pk.View([viewA.shape[0]], pk.float)
        pk.parallel_for(
            viewA.shape[0],
            multiply_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def subtract_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = viewA[tid] - viewB[tid]


@pk.workunit
def subtract_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = viewA[tid] - viewB[tid]


def subtract(viewA, viewB):
    """
    Subtracts positionally corresponding elements
    of viewA with elements of viewB

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        out = pk.View([viewA.shape[0]], pk.double)
        pk.parallel_for(
            viewA.shape[0],
            subtract_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        out = pk.View([viewA.shape[0]], pk.float)
        pk.parallel_for(
            viewA.shape[0],
            subtract_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def matmul_impl_1d_double(tid: int, acc: pk.Acc[pk.double], viewA: pk.View1D[pk.double], viewB: pk.View2D[pk.double]):
    acc += viewA[tid] * viewB[0][tid]


@pk.workunit
def matmul_impl_1d_float(tid: int, acc: pk.Acc[pk.float], viewA: pk.View1D[pk.float], viewB: pk.View2D[pk.float]):
    acc += viewA[tid] * viewB[0][tid]

def matmul(viewA, viewB):
    """
    1D Matrix Multiplication of compatible views

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    Float/Double
        1D Matmul result

    """
    if len(viewA.shape) != 1 or viewA.shape[0] != viewB.shape[0]:
        raise RuntimeError(
            "Input operand 1 has a mismatch in its core dimension (Size {} is different from {})".format(viewA.shape[0], viewB.shape[0]))

    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        return pk.parallel_reduce(
            viewA.shape[0],
            matmul_impl_1d_double,
            viewA=viewA,
            viewB=viewB)
    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        return pk.parallel_reduce(
            viewA.shape[0],
            matmul_impl_1d_float,
            viewA=viewA,
            viewB=viewB)
    else:
        raise RuntimeError("Incompatible Types")


@pk.workunit
def divide_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = viewA[tid] / viewB[tid]


@pk.workunit
def divide_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = viewA[tid] / viewB[tid]


def divide(viewA, viewB):
    """
    Divides positionally corresponding elements
    of viewA with elements of viewB

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        out = pk.View([viewA.shape[0]], pk.double)
        pk.parallel_for(
            viewA.shape[0],
            divide_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        out = pk.View([viewA.shape[0]], pk.float)
        pk.parallel_for(
            viewA.shape[0],
            divide_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def negative_impl_1d_double(tid: int, view: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = view[tid] * -1


@pk.workunit
def negative_impl_1d_float(tid: int, view: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = view[tid] * -1

def negative(view):
    """
    Element-wise negative of the view

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(view.dtype) == "DataType.double":
        out = pk.View([view.shape[0]], pk.double)
        pk.parallel_for(view.shape[0], negative_impl_1d_double, view=view, out=out)
    elif str(view.dtype) == "DataType.float":
        out = pk.View([view.shape[0]], pk.float)
        pk.parallel_for(view.shape[0], negative_impl_1d_float, view=view, out=out)
    return out


@pk.workunit
def positive_impl_1d_double(tid: int, view: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = view[tid]


@pk.workunit
def positive_impl_1d_float(tid: int, view: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = view[tid]

def positive(view):
    """
    Element-wise positive of the view;
    Essentially returns a copy of the view

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(view.dtype) == "DataType.double":
        out = pk.View([view.shape[0]], pk.double)
        pk.parallel_for(view.shape[0], positive_impl_1d_double, view=view, out=out)
    elif str(view.dtype) == "DataType.float":
        out = pk.View([view.shape[0]], pk.float)
        pk.parallel_for(view.shape[0], positive_impl_1d_float, view=view, out=out)
    return out


@pk.workunit
def power_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = pow(viewA[tid], viewB[tid])


@pk.workunit
def power_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = pow(viewA[tid], viewB[tid])


def power(viewA, viewB):
    """
    Returns a view with each val in viewA raised
    to the positionally corresponding power in viewB

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        out = pk.View([viewA.shape[0]], pk.double)
        pk.parallel_for(
            viewA.shape[0],
            power_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        out = pk.View([viewA.shape[0]], pk.float)
        pk.parallel_for(
            viewA.shape[0],
            power_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def fmod_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = fmod(viewA[tid], viewB[tid])


@pk.workunit
def fmod_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = fmod(viewA[tid], viewB[tid])


def fmod(viewA, viewB):
    """
    Element-wise remainder of division when element of viewA is
    divided by positionally corresponding element of viewB

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """

    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        out = pk.View([viewA.shape[0]], pk.double)
        pk.parallel_for(
            viewA.shape[0],
            fmod_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        out = pk.View([viewA.shape[0]], pk.float)
        pk.parallel_for(
            viewA.shape[0],
            fmod_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def square_impl_1d_double(tid: int, view: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = view[tid] * view[tid]


@pk.workunit
def square_impl_1d_float(tid: int, view: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = view[tid] * view[tid]

def square(view):
    """
    Squares argument element-wise

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(view.dtype) == "DataType.double":
        out = pk.View([view.shape[0]], pk.double)
        pk.parallel_for(
            view.shape[0],
            square_impl_1d_double,
            view=view,
            out=out)

    elif str(view.dtype) == "DataType.float":
        out = pk.View([view.shape[0]], pk.float)
        pk.parallel_for(
            view.shape[0],
            square_impl_1d_float,
            view=view,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def greater_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.uint16]):
    out[tid] = viewA[tid] > viewB[tid]


@pk.workunit
def greater_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.uint16]):
    out[tid] = viewA[tid] > viewB[tid]


def greater(viewA, viewB):
    """
    Return the truth value of viewA > viewB element-wise.

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view (uint16)
           Output view.

    """
    out = pk.View([viewA.shape[0]], pk.uint16)
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        pk.parallel_for(
            viewA.shape[0],
            greater_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        pk.parallel_for(
            viewA.shape[0],
            greater_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def logaddexp_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.double],):
    out[tid] = log(exp(viewA[tid]) + exp(viewB[tid]))


@pk.workunit
def logaddexp_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.float],):
    out[tid] = log(exp(viewA[tid]) + exp(viewB[tid]))


def logaddexp(viewA, viewB):
    """
    Return a view with log(exp(a) + exp(b)) calculate for
    positionally corresponding elements in viewA and viewB

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        out = pk.View([viewA.shape[0]], pk.double)
        pk.parallel_for(
            viewA.shape[0],
            logaddexp_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        out = pk.View([viewA.shape[0]], pk.float)
        pk.parallel_for(
            viewA.shape[0],
            logaddexp_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out

def true_divide(viewA, viewB):
    """
    true_divide is an alias of divide

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """

    return divide(viewA, viewB)


@pk.workunit
def logaddexp2_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.double],):
    out[tid] = log2(pow(2, viewA[tid]) + pow(2, viewB[tid]))


@pk.workunit
def logaddexp2_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.float],):
    out[tid] = log2(pow(2, viewA[tid]) + pow(2, viewB[tid]))


def logaddexp2(viewA, viewB):
    """
    Return a view with log(pow(2, a) + pow(2, b)) calculated for
    positionally corresponding elements in viewA and viewB

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        out = pk.View([viewA.shape[0]], pk.double)
        pk.parallel_for(
            viewA.shape[0],
            logaddexp2_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        out = pk.View([viewA.shape[0]], pk.float)
        pk.parallel_for(
            viewA.shape[0],
            logaddexp2_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def floor_divide_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = viewA[tid] // viewB[tid]


@pk.workunit
def floor_divide_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = viewA[tid] // viewB[tid]


def floor_divide(viewA, viewB):
    """
    Divides positionally corresponding elements
    of viewA with elements of viewB and floors the result

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        out = pk.View([viewA.shape[0]], pk.double)
        pk.parallel_for(
            viewA.shape[0],
            floor_divide_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        out = pk.View([viewA.shape[0]], pk.float)
        pk.parallel_for(
            viewA.shape[0],
            floor_divide_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def sin_impl_1d_double(tid: int, view: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = sin(view[tid])


@pk.workunit
def sin_impl_1d_float(tid: int, view: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = sin(view[tid])


def sin(view):
    """
    Element-wise trignometric sine of the view

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(view.dtype) == "DataType.double":
        out = pk.View([view.shape[0]], pk.double)
        pk.parallel_for(view.shape[0], sin_impl_1d_double, view=view, out=out)
    elif str(view.dtype) == "DataType.float":
        out = pk.View([view.shape[0]], pk.float)
        pk.parallel_for(view.shape[0], sin_impl_1d_float, view=view, out=out)
    return out


@pk.workunit
def cos_impl_1d_double(tid: int, view: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = cos(view[tid])


@pk.workunit
def cos_impl_1d_float(tid: int, view: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = cos(view[tid])


def cos(view):
    """
    Element-wise trignometric cosine of the view

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(view.dtype) == "DataType.double":
        out = pk.View([view.shape[0]], pk.double)
        pk.parallel_for(view.shape[0], cos_impl_1d_double, view=view, out=out)
    elif str(view.dtype) == "DataType.float":
        out = pk.View([view.shape[0]], pk.float)
        pk.parallel_for(view.shape[0], cos_impl_1d_float, view=view, out=out)
    return out


@pk.workunit
def tan_impl_1d_double(tid: int, view: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = tan(view[tid])


@pk.workunit
def tan_impl_1d_float(tid: int, view: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = tan(view[tid])


def tan(view):
    """
    Element-wise tangent of the view

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(view.dtype) == "DataType.double":
        out = pk.View([view.shape[0]], pk.double)
        pk.parallel_for(view.shape[0], tan_impl_1d_double, view=view, out=out)
    elif str(view.dtype) == "DataType.float":
        out = pk.View([view.shape[0]], pk.float)
        pk.parallel_for(view.shape[0], tan_impl_1d_float, view=view, out=out)
    return out


@pk.workunit
def logical_and_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.uint16]):
    out[tid] = viewA[tid] and viewB[tid]


@pk.workunit
def logical_and_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.uint16]):
    out[tid] = viewA[tid] and viewB[tid]


def logical_and(viewA, viewB):
    """
    Return the element-wise truth value of viewA AND viewB.

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view (uint16)
           Output view.

    """
    out = pk.View([viewA.shape[0]], pk.uint16)
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        pk.parallel_for(
            viewA.shape[0],
            logical_and_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        pk.parallel_for(
            viewA.shape[0],
            logical_and_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def logical_or_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.uint16]):
    out[tid] = viewA[tid] or viewB[tid]


@pk.workunit
def logical_or_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.uint16]):
    out[tid] = viewA[tid] or viewB[tid]


def logical_or(viewA, viewB):
    """
    Return the element-wise truth value of viewA OR viewB.

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view (uint16)
           Output view.

    """
    out = pk.View([viewA.shape[0]], pk.uint16)
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        pk.parallel_for(
            viewA.shape[0],
            logical_or_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        pk.parallel_for(
            viewA.shape[0],
            logical_or_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def logical_xor_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.uint16]):
    out[tid] = bool(viewA[tid]) ^ bool(viewB[tid])


@pk.workunit
def logical_xor_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.uint16]):
    out[tid] = bool(viewA[tid]) ^ bool(viewB[tid])


def logical_xor(viewA, viewB):
    """
    Return the element-wise truth value of viewA XOR viewB.

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view (uint16)
           Output view.

    """
    out = pk.View([viewA.shape[0]], pk.uint16)
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        pk.parallel_for(
            viewA.shape[0],
            logical_xor_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        pk.parallel_for(
            viewA.shape[0],
            logical_xor_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def logical_not_impl_1d_double(tid: int, view: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = not view[tid]


@pk.workunit
def logical_not_impl_1d_float(tid: int, view: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = not view[tid]


def logical_not(view):
    """
    Element-wise logical_not of the view.

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(view.dtype) == "DataType.double":
        out = pk.View([view.shape[0]], pk.double)
        pk.parallel_for(view.shape[0], logical_not_impl_1d_double, view=view, out=out)
    elif str(view.dtype) == "DataType.float":
        out = pk.View([view.shape[0]], pk.float)
        pk.parallel_for(view.shape[0], logical_not_impl_1d_float, view=view, out=out)
    return out


@pk.workunit
def fmax_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.uint16]):
    out[tid] = fmax(viewA[tid], viewB[tid])


@pk.workunit
def fmax_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.uint16]):
    out[tid] = fmax(viewA[tid], viewB[tid])


def fmax(viewA, viewB):
    """
    Return the element-wise fmax.

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view (uint16)
           Output view.

    """
    out = pk.View([viewA.shape[0]], pk.uint16)
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        pk.parallel_for(
            viewA.shape[0],
            fmax_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        pk.parallel_for(
            viewA.shape[0],
            fmax_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def fmin_impl_1d_double(tid: int, viewA: pk.View1D[pk.double], viewB: pk.View1D[pk.double], out: pk.View1D[pk.uint16]):
    out[tid] = fmin(viewA[tid], viewB[tid])


@pk.workunit
def fmin_impl_1d_float(tid: int, viewA: pk.View1D[pk.float], viewB: pk.View1D[pk.float], out: pk.View1D[pk.uint16]):
    out[tid] = fmin(viewA[tid], viewB[tid])


def fmin(viewA, viewB):
    """
    Return the element-wise fmin.

    Parameters
    ----------
    viewA : pykokkos view
            Input view.
    viewB : pykokkos view
            Input view.

    Returns
    -------
    out : pykokkos view (uint16)
           Output view.

    """
    out = pk.View([viewA.shape[0]], pk.uint16)
    if str(viewA.dtype) == "DataType.double" and str(viewB.dtype) == "DataType.double":
        pk.parallel_for(
            viewA.shape[0],
            fmin_impl_1d_double,
            viewA=viewA,
            viewB=viewB,
            out=out)

    elif str(viewA.dtype) == "DataType.float" and str(viewB.dtype) == "DataType.float":
        pk.parallel_for(
            viewA.shape[0],
            fmin_impl_1d_float,
            viewA=viewA,
            viewB=viewB,
            out=out)
    else:
        raise RuntimeError("Incompatible Types")
    return out


@pk.workunit
def exp_impl_1d_double(tid: int, view: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = exp(view[tid])


@pk.workunit
def exp_impl_1d_float(tid: int, view: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = exp(view[tid])


def exp(view):
    """
    Element-wise exp of the view.

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(view.dtype) == "DataType.double":
        out = pk.View([view.shape[0]], pk.double)
        pk.parallel_for(view.shape[0], exp_impl_1d_double, view=view, out=out)
    elif str(view.dtype) == "DataType.float":
        out = pk.View([view.shape[0]], pk.float)
        pk.parallel_for(view.shape[0], exp_impl_1d_float, view=view, out=out)
    return out


@pk.workunit
def exp2_impl_1d_double(tid: int, view: pk.View1D[pk.double], out: pk.View1D[pk.double]):
    out[tid] = pow(2, view[tid])


@pk.workunit
def exp2_impl_1d_float(tid: int, view: pk.View1D[pk.float], out: pk.View1D[pk.float]):
    out[tid] = pow(2, view[tid])


def exp2(view):
    """
    Element-wise 2**x of the view.

    Parameters
    ----------
    view : pykokkos view
           Input view.

    Returns
    -------
    out : pykokkos view
           Output view.

    """
    if str(view.dtype) == "DataType.double":
        out = pk.View([view.shape[0]], pk.double)
        pk.parallel_for(view.shape[0], exp2_impl_1d_double, view=view, out=out)
    elif str(view.dtype) == "DataType.float":
        out = pk.View([view.shape[0]], pk.float)
        pk.parallel_for(view.shape[0], exp2_impl_1d_float, view=view, out=out)
    return out
