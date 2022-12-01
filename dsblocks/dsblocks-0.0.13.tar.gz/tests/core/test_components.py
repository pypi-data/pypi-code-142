# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../nbs/00_tests/core/tst.components.ipynb.

# %% auto 0
__all__ = ['Transform1', 'TransformWithFitApply', 'TransformWithoutFitApply', 'MyDataConverter', 'TransformWithFitApplyDC',
           'TransformWithoutFitApply2', 'TransformWithFitApply2', 'component_save_data', 'TransformWithoutFit',
           'TransformWithFitApplyOnly', 'get_data_for_one_class', 'f', 'g', 'add_one', 'test_component_config',
           'test_component_store_attrs', 'test_component_aliases', 'test_component_multiple_inputs',
           'test_component_fit_apply', 'test_component_validation_test', 'test_component_save_load',
           'test_component_run_depend_on_existence', 'test_component_logger', 'test_component_data_converter',
           'test_component_data_io', 'test_component_equal', 'test_set_paths', 'test_determine_fit_function',
           'test_direct_methods', 'test_pass_apply', 'test_wrapping_estimator',
           'test_get_specific_data_io_parameters_for_component', 'test_get_specific_data_io_parameters',
           'test_set_suffix', 'test_compare_kwargs', 'test_build_partial', 'test_sampling_component',
           'test_sklearn_component', 'test_no_saver_component', 'test_one_class_sklearn_component',
           'test_pandas_component', 'test_io', 'test_pandas_io', 'test_component_decorator']

# %% ../../../nbs/00_tests/core/tst.components.ipynb 2
from dsblocks.core.components import *

# %% ../../../nbs/00_tests/core/tst.components.ipynb 3
import pytest
import numpy as np
import os
import joblib
from sklearn.utils import Bunch
from pathlib import Path
import time
from IPython.display import display
import pandas as pd

from dsblocks.core.data_conversion import DataConverter, NoConverter, PandasConverter, data_converter_factory
from dsblocks.core.utils import DataIO, SklearnIO, PandasIO, NoSaverIO
from dsblocks.utils.utils import remove_previous_results, check_last_part
from dsblocks.utils.utils import set_logger
import dsblocks.config.bt_defaults as dflt
from dsblocks.core.data_conversion import DataConverter
from dsblocks.utils.dummies import SumXY
from dsblocks.utils.dummies import DummyEstimator
from dsblocks.utils.dummies import Multiply10direct, Max10direct
from dsblocks.utils.dummies import DummyEstimatorWithLabels
from hpsearch.utils.experiment_utils import read_df
from sklearn.preprocessing import MinMaxScaler

# %% ../../../nbs/00_tests/core/tst.components.ipynb 4
# example with _fit_apply implemented
class TransformWithFitApply (Component):
    def __init__ (self, **kwargs):
        super().__init__ (**kwargs)
    def _fit (self, X, y=None):
        self.sum = X.sum(axis=0)
    def _apply (self, X):
        return X + self.sum
    def _fit_apply (self, X, y=None):
        self.sum = X.sum(axis=0)*10
        return X + self.sum

# example without _fit_apply implemented
class TransformWithoutFitApply (Component):
    def __init__ (self, **kwargs):
        super().__init__ (**kwargs)
    def _fit (self, X, y=None):
        self.sum = X.sum(axis=0)
    def _apply (self, X):
        return X + self.sum

# %% ../../../nbs/00_tests/core/tst.components.ipynb 5
# example with _fit_apply implemented
class MyDataConverter (DataConverter):
    def __init__ (self, **kwargs):
        super ().__init__ (**kwargs)
    def convert_before_fitting (self, *X):
        X, y = X if len(X)==2 else (X[0], None)
        self.orig = X[0]
        X[0] = 0
        return X, y
    def convert_after_fitting (self, *X):
        X, y = X if len(X)==2 else (X, None)
        if type(X) is tuple and len(X)==1: X = X[0]
        X[0] = self.orig
        return X
    def convert_before_applying (self, X, **kwargs):
        self.orig2 = X[1]
        X[1] = 0
        return X
    def convert_after_applying (self, X, **kwargs):
        X[1] = self.orig2
        return X
    def convert_before_fit_apply (self, *X, **kwargs):
        _ = self.convert_before_fitting (*X)
        if self.inplace:
            X2, y = X if len(X)==2 else (X[0], None)
            self.X = X2 if type(X2) is tuple else (X2,)
        return self.convert_before_applying (*X)
        
class TransformWithFitApplyDC (Component):
    def __init__ (self, **kwargs):
        super().__init__ (data_converter=MyDataConverter,**kwargs)
    def _fit (self, X, y=None):
        self.sum = X.sum(axis=0)
    def _apply (self, X):
        return X + self.sum
    def _fit_apply (self, X, y=None):
        self.sum = X.sum(axis=0)
        return X + self.sum

# %% ../../../nbs/00_tests/core/tst.components.ipynb 6
# example with _fit_apply implemented
class TransformWithoutFitApply2 (Component):
    def __init__ (self, error_if_fit_func=False, error_if_apply_func=False,  **kwargs):
        super().__init__ (data_io='SklearnIO', **kwargs)
        self.estimator = Bunch(sum=None)
    def _fit (self, X, y=None):
        if self.error_if_fit_func: raise RuntimeError ('fit should not run')
        print ('running _fit')
        self.estimator.sum = X.sum(axis=0)
    def _apply (self, X):
        if self.error_if_apply_func: raise RuntimeError ('apply should not run')
        if self.estimator.sum is None: raise RuntimeError ('fit should be called before apply')
        print ('running _apply')
        return X + self.estimator.sum

Transform1 = TransformWithoutFitApply2

class TransformWithFitApply2 (Component):
    def __init__ (self, error_if_fit_func=False, error_if_apply_func=False, error_if_fit_apply_func=False, 
                  **kwargs):
        super().__init__ (data_io='SklearnIO', **kwargs)
        self.estimator = Bunch(sum=None)
    def _fit (self, X, y=None):
        if self.error_if_fit_func: raise RuntimeError ('fit should not run')
        print ('running _fit')
        self.estimator.sum = X.sum(axis=0)
    def _apply (self, X):
        if self.error_if_apply_func: raise RuntimeError ('apply should not run')
        if self.estimator.sum is None: raise RuntimeError ('fit should be called before apply')
        print ('running _apply')
        return X + self.estimator.sum
    def _fit_apply (self, X, y=None):
        if self.error_if_fit_apply_func: raise RuntimeError ('fit_apply should not run')
        print ('running _fit_apply')
        self.estimator.sum = X.sum(axis=0)
        return X + self.estimator.sum

def component_save_data ():
    X = np.array ([100, 90, 10])
    return X

# %% ../../../nbs/00_tests/core/tst.components.ipynb 7
class TransformWithoutFit (Component):
    def __init__ (self, factor=2, **kwargs):
        super().__init__ (**kwargs)
    def _apply (self, X):
        return X * self.factor
    
class TransformWithFitApplyOnly (Component):
    def __init__ (self, **kwargs):
        super().__init__ (**kwargs)
    def _apply (self, X):
        return X + self.sum
    def _fit_apply (self, X, y=None):
        self.sum = X.sum(axis=0)*10
        return X + self.sum

# %% ../../../nbs/00_tests/core/tst.components.ipynb 8
def get_data_for_one_class ():
    data = np.r_[np.ones ((5,2)), 2*np.ones((5,2))]
    y = np.r_[np.ones ((5,)), np.zeros((5,))]
    return data, y

# %% ../../../nbs/00_tests/core/tst.components.ipynb 9
@io
def f (x, **kwargs):
    time.sleep (0.5)
    return x+1

# %% ../../../nbs/00_tests/core/tst.components.ipynb 10
@pandas_io
def g (X, **kwargs):
    time.sleep (1)
    return X+1

# %% ../../../nbs/00_tests/core/tst.components.ipynb 11
@component
def add_one (x, **kwargs):
    return x+1

# %% ../../../nbs/00_tests/core/tst.components.ipynb 12
def test_component_config ():
    # **********************************************************************
    # test obtain_config_params method
    # **********************************************************************
    tr = Component(name='sky')
    config = dict(first=1,
                  second=2,
                  third=3,
                  sky=dict (second=4)
                 )
    config_r = tr.obtain_config_params (**config)
    logger = set_logger (dflt.name_logger, verbose=dflt.verbose)
    assert config_r=={'first': 1, 'second': 4, 'third': 3, 'sky': {'second': 4}, 'verbose': dflt.verbose, 'logger': logger}
    assert config == {'first': 1, 'second': 2, 'third': 3, 'sky': {'second': 4}}
    
    # **********************************************************************
    # test that component saves results when using global 
    # parameter save=True
    # **********************************************************************
    class MyTransform (Component):
        def __init__ (self,**kwargs):
            super().__init__ (**kwargs)
            self.create_estimator ()
    
        def _fit (self, X, y=None):
            self.estimator.mu = X.mean()
        def _transform (self, X):
            return X-self.estimator.mu
    
    path_results = 'testing_configuration'
    tr = MyTransform (path_results=path_results,
                      save = True)
    
    X = np.array([[1,2,3],[4,5,6]])
    tr.fit_transform(X)
    
    
    l = sorted(os.listdir(path_results))
    assert l==['models', 'whole'], f'found: {l}'
    
    # **********************************************************************
    # test that component does not save results when we 
    # use component-specific parameter MyTransform = dict(save=False)
    # **********************************************************************
    
    remove_previous_results (path_results)
    
    tr = MyTransform (data_io = SklearnIO(
                                  path_results='testing_configuration',
                                  save = True,
                                  MyTransform = dict(save=False)
                                )
                     )
    tr.fit_transform(X)
    with pytest.raises(FileNotFoundError):
        os.listdir(path_results)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 13
def test_component_store_attrs ():
    # recursively storing __init__ attrs across hiearchy of classes
    class Intermediate (Component):
        def __init__ (self, x=3, y=4, **kwargs):
            super().__init__ (**kwargs)
    
    class Final (Intermediate):
        def __init__ (self, z=6, h=[2,3,5], **kwargs):
            super().__init__ (**kwargs)
    
    o = Final (x=9, h=[1,2,4])
    assert o.x==9 and o.y==4 and o.z==6 and o.h==[1,2,4]
    
    o = Final (y=7, z=10, h=[1,2,4], Final={'h': [9,11,10]})
    assert o.x==3 and o.y==7 and o.z==10 and o.h==[9,11,10]
    
    # only attributes specific of Final are replaced.
    # trying to replace attributes specific of Intermediate 
    # does not work
    o = Final (y=7, z=10, h=[1,2,4], Intermediate={'y': 12})
    assert o.x==3 and o.y==7 and o.z==10 and o.h==[1,2,4]
    
    class Intermediate (Component):
        def __init__ (self, x=3, y=4, **kwargs):
            super().__init__ (**kwargs)
    
    class Final (Intermediate):
        def __init__ (self, z=6, h=[2,3,5], **kwargs):
            super().__init__ (**kwargs)
    
    o = Final (x=9, h=[1,2,4], group='group_1', group_1={'y': 10, 'z':60})
    assert o.x==9 and o.y==10 and o.z==60 and o.h==[1,2,4]
    
    
     # *******************
    # test using same field in B4 and in A3, but
    # B4 passes that value to A3 in super(),
    # after modifying it
    # *****************
    class A (Component):
        def __init__ (self, x=3, path_results='test_recursive', **kwargs):
            path_results = f'{path_results}/another'
            super ().__init__ (path_results=path_results, error_if_present=True, 
                               **kwargs)
    
    class B (A):
        def __init__ (self, x=30, y=10, **kwargs):
            x = x*2
            super().__init__ (x=x, **kwargs)
            self.ab = A (**kwargs)
    
    b = B ()
    assert b.x==60 and b.ab.x==3 and b.y==10 and b.path_results==Path('test_recursive/another').resolve()
    
    b = B (x=6, path_results='new_path')
    assert b.x==12 and b.ab.x==3 and b.y==10 and b.path_results==Path('new_path/another').resolve()
    
    # *******************
    # test using same field in C and in A, but
    # the field is modified in a parent B
    # *****************
    class C(B):
        def __init__ (self, x=40, z=100, **kwargs):
            super().__init__ (x=x, **kwargs)
            self.b = B(**kwargs)
    
    with pytest.raises (RuntimeError):
        c = C()
    
    c = C(ignore={'x'})
    assert c.x==80 and c.y==10 and c.z==100 and c.b.x==60 and c.b.y==10
    
    c = C (x=9, ignore={'x'})
    assert c.x==18 and c.y==10 and c.z==100 and c.b.x==60 and c.b.y==10
    
    assert not hasattr(c, 'ignore')


# %% ../../../nbs/00_tests/core/tst.components.ipynb 14
def test_component_aliases ():
    # test that we can implement _transform and use all the aliases 
    # (transform, predict, apply,  __call__)
    class MyTransform (Component):
        def _transform (self, x):
            return x*2
    
    my_transform = MyTransform()
    assert my_transform.transform (3) == 6
    assert my_transform.predict (3) == 6
    assert my_transform.apply (3) == 6
    assert my_transform (3) == 6
    
    # test that we can implement _apply and use all the aliases 
    # (transform, predict, apply and __call__)
    class MyTransform2 (Component):
        def _apply (self, x):
            return x*2
    
    my_transform2 = MyTransform2()
    assert my_transform2.transform (3) == 6
    assert my_transform2.predict (3) == 6
    assert my_transform2.apply (3) == 6
    assert my_transform2 (3) == 6
    
    # test that we can implement _predict and use all the aliases 
    # (transform, predict, apply and __call__)
    class MyTransform3 (Component):
        def _predict (self, x):
            return x*2
    
    my_transform3 = MyTransform3()
    assert my_transform3.transform (3) == 6
    assert my_transform3.predict (3) == 6
    assert my_transform3.apply (3) == 6
    assert my_transform3 (3) == 6
    
    # test that an exception is raised if neither _tranform nor _apply are defined
    class MyTransform4 (Component):
        def _wrong_method (self, x):
            return x*2
    
    my_transform4 = MyTransform4 ()
    
    with pytest.raises (AssertionError):
        my_transform4.transform(3)
    
    
    # test that an exception is raised if more than one alias is implemented
    class MyTransform5 (Component):
        def _predict (self, x):
            return x*2
        def _apply (self, x):
            return x*2
    
    with pytest.raises(AttributeError):
        my_transform5 = MyTransform5 ()


# %% ../../../nbs/00_tests/core/tst.components.ipynb 15
def test_component_multiple_inputs ():
    # test that we can apply tranform to multiple data items
    my_transform = SumXY ()
    result = my_transform.transform (3, 4)
    print (result)
    assert result==7
    
    # test that we can apply tranform to single data items
    class MyTransform2 (Component):
        def _apply (self, x):
            return x*2
    
    my_transform2 = MyTransform2 ()
    result = my_transform2.transform (3)
    print (result)
    assert result==6


# %% ../../../nbs/00_tests/core/tst.components.ipynb 16
def test_component_fit_apply ():
    tr1 = TransformWithFitApply ()
    X = np.array ([100, 90, 10])
    result = tr1.fit_apply (X)
    assert (result==(X+2000)).all()
    
    # same result obtained by aliases
    result = tr1.fit_transform (X)
    assert (result==(X+2000)).all()
    
    # different result if we apply fit and apply separately
    result = tr1.fit (X).transform (X)
    assert (result==(X+200)).all()
    
    # transform without fit_apply
    tr2 = TransformWithoutFitApply ()
    result = tr2.fit_apply (X)
    assert (result==(X+200)).all()
    
    # same result obtained by aliases
    result = tr2.fit_transform (X)
    assert (result==(X+200)).all()


# %% ../../../nbs/00_tests/core/tst.components.ipynb 17
def test_component_validation_test ():
    class Transform1 (Component):
        def __init__ (self, **kwargs):
            super().__init__ (**kwargs)
        def _fit (self, X, y=None, validation_data=None, test_data=None):
            self.sum = X.sum(axis=0)
    
            print (f'validation_data: {validation_data}')
            print (f'test_data: {test_data}')
    
            self.validation_data = validation_data
            self.test_data = test_data
    
        def _apply (self, X):
            return X + self.sum
    
    tr1 = Transform1 ()
    X = np.array ([100, 90, 10])
    
    # case 1: validation_data and test_data are not tuples
    validation_data = np.array ([100, 90, 10])*10
    test_data = np.array ([100, 90, 10])*100
    result = tr1.fit_apply (X, validation_data=validation_data, test_data=test_data)
    assert (tr1.validation_data==validation_data).all()
    assert (tr1.test_data==test_data).all()
    
    # case 2: validation_data is a tuple, and test_data is not given
    result = tr1.fit_apply (X, validation_data=(validation_data,1))
    assert (tr1.validation_data[0]==validation_data).all()
    assert tr1.validation_data[1]==1
    assert tr1.test_data is None
    
    # case 3: validation_data is a tuple with more than 2 elements, exception is raised
    with pytest.raises(ValueError):
        result = tr1.fit_apply (X, validation_data=(validation_data,1,2))


# %% ../../../nbs/00_tests/core/tst.components.ipynb 18
def test_component_save_load ():
    X = component_save_data ()
    
    path_results = 'component_loading_saving'
    remove_previous_results (path_results=path_results)
    
    tr1 = Transform1 (path_results=path_results)
    tr1.fit (X)
    result = tr1.apply (X)
    
    tr2 = Transform1 (path_results=path_results)
    tr2.load_estimator()
    assert tr2.estimator.sum == tr1.estimator.sum
    
    result2 = tr2.data_io.load_result ()
    assert (result2 == sum(X)+X).all()
    
    assert os.listdir (f'{path_results}/whole')==['transform_without_fit_apply2_result.pk']
    assert os.listdir (f'{path_results}/models')==['transform_without_fit_apply2_estimator.pk']
    
    result_b = tr1.apply (X*2, split='test')
    result2b = tr2.data_io.load_result (split='test')
    assert (result_b==result2b).all()
    assert os.listdir (f'{path_results}/test')==['transform_without_fit_apply2_result.pk']
    
    result2b = tr2.data_io.load_result ()
    assert (result_b!=result2b).all()
    
    remove_previous_results (path_results=path_results)
    
    
    # Test that no saving is done if save=False
    tr1 = Transform1 (path_results=path_results, save=False)
    tr1.fit (X)
    result = tr1.apply (X)
    assert not os.path.exists(path_results)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 19
def test_component_run_depend_on_existence ():
    path_results = 'component_run_existence'
    remove_previous_results (path_results=path_results)
    
    tr1 = TransformWithFitApply2 (path_results=path_results, error_if_fit_func=True, error_if_apply_func=True)
    X = np.array ([100, 90, 10])
    result = tr1.fit_apply (X)
    assert (result==(X+200)).all()
    
    assert os.listdir(f'{path_results}/models')==['transform_with_fit_apply2_estimator.pk']
    
    assert os.listdir(f'{path_results}/whole')==['transform_with_fit_apply2_result.pk']
    
    tr1 = TransformWithFitApply2 (path_results=path_results, error_if_fit_func=True, error_if_apply_func=True,
                                  error_if_fit_func_apply=True)
    result2 = tr1.fit_apply (X)
    assert (result2==(X+200)).all()
    
    assert tr1.estimator=={'sum': 200}
    
    tr2 = TransformWithFitApply2 (path_results=path_results, error_if_fit_func=True, error_if_apply_func=True,
                                  error_if_fit_apply_func=True)
    result3 = tr2.apply (X)
    
    assert (result3==(X+200)).all()
    assert tr2.estimator=={'sum': None}
    
    os.remove (f'{path_results}/models/transform_with_fit_apply2_estimator.pk')
    
    with pytest.raises (RuntimeError):
        result3 = tr2.fit_apply (X)
    
    tr2.error_if_fit_apply_func = False
    result4 = tr2.fit_apply (X)
    assert tr2.estimator=={'sum': 200}
    assert (result4==(X+200)).all()
    
    os.remove (f'{path_results}/whole/transform_with_fit_apply2_result.pk')
    
    tr3 = TransformWithFitApply2 (path_results=path_results, error_if_fit_func=True, error_if_apply_func=True,
                                  error_if_fit_apply_func=True)
    with pytest.raises (RuntimeError):
        _ = tr3.apply (X)
    with pytest.raises (RuntimeError):
        _ = tr3.fit_apply (X)
    tr3.error_if_fit_apply_func = False
    result5 = tr3.fit_apply (X)
    assert tr3.estimator=={'sum': 200}
    assert (result5==(X+200)).all()
    
    assert os.listdir (f'{path_results}/whole')==['transform_with_fit_apply2_result.pk']
    assert os.listdir (f'{path_results}/models')==['transform_with_fit_apply2_estimator.pk']
    
    remove_previous_results (path_results)
    
    tr4 = TransformWithFitApply2 (path_results=path_results, error_if_fit_func=False, error_if_apply_func=False,
                                  error_if_fit_apply_func=True)
    result6 = tr4.fit(X).apply (X)
    assert tr4.estimator=={'sum': 200}
    assert (result6==(X+200)).all()
    assert os.listdir (f'{path_results}/whole')==['transform_with_fit_apply2_result.pk']
    assert os.listdir (f'{path_results}/models')==['transform_with_fit_apply2_estimator.pk']
    
    remove_previous_results (path_results)
    
    tr5 = TransformWithoutFitApply2 (path_results=path_results, error_if_fit_func=False, error_if_apply_func=False)
    result7 = tr5.fit(X).apply (X)
    assert tr5.estimator=={'sum': 200}
    assert (result7==(X+200)).all()
    assert os.listdir (f'{path_results}/whole')==['transform_without_fit_apply2_result.pk']
    assert os.listdir (f'{path_results}/models')==['transform_without_fit_apply2_estimator.pk']
    
    remove_previous_results (path_results)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 20
def test_component_logger ():
    X = component_save_data ()
    
    tr1 = Transform1 (verbose=0)
    tr1.fit (X)
    result = tr1.apply (X)
    
    tr1 = Transform1 (verbose=1)
    tr1.fit (X)
    result = tr1.apply (X)
    
    tr1 = Transform1 (verbose=2)
    tr1.fit (X)
    result = tr1.apply (X)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 21
def test_component_data_converter ():
    class MyTransform (Component):
        def __init__ (self, **kwargs):
            super().__init__ (data_converter='PandasConverter',
                              **kwargs)
        def _apply (self, x):
            return x*2
    
    my_transform = MyTransform (separate_labels=False)
    assert my_transform.data_converter.separate_labels is False
    assert type(my_transform.data_converter) is PandasConverter
    
    # example where data-converter uses class-specific parameters
    config = dict(separate_labels=False, MyTransform=dict(separate_labels=True))
    my_transform = MyTransform (**config)
    assert my_transform.data_converter.separate_labels is True
    assert config['separate_labels'] is False


# %% ../../../nbs/00_tests/core/tst.components.ipynb 22
def test_component_data_io ():
    # example using data_io
    
    path_results = 'test_data_io'
    remove_previous_results (path_results=path_results)
    
    class MyTransform (Component):
        def __init__ (self, **kwargs):
            super().__init__ (result_io='pandas',
                              **kwargs)
        def _fit (self, X, y=None):
            self.estimator = Bunch(sum=100)
    
        def _apply (self, x):
            return pd.DataFrame ([[1,2],[3,4]], columns=['a','b'])
    
    my_transform = MyTransform (path_results='do_not_use', MyTransform=dict(path_results=path_results))
    my_transform.fit (1)
    assert os.listdir (f'{path_results}/models')==['my_transform_estimator.pk']
    
    df1 = my_transform.apply (1)
    assert os.listdir (f'{path_results}/whole')==['my_transform_result.parquet']
    
    assert not os.path.exists ('do_not_use')
    
    del my_transform
    my_transform = MyTransform (path_results='do_not_use', MyTransform=dict(path_results=path_results))
    #assert my_transform.estimator is None
    my_transform.load_estimator()
    assert my_transform.estimator == Bunch(sum=100)
    
    df2 = my_transform.load_result ()
    pd.testing.assert_frame_equal (df1, df2)
    
    remove_previous_results (path_results=path_results)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 23
def test_component_equal ():
    path_results = 'assert_equal'
    remove_previous_results (path_results=path_results)
    
    class MyTransform (Component):
        def __init__ (self, noise=1e-10, different = False, **kwargs):
            super().__init__ (result_io='pandas',
                              **kwargs)
        def _fit (self, X, y=None):
            self.estimator = Bunch(sum=100)
    
        def _generate_noise (self):
            while True:
                noise = np.random.rand() * self.noise
                if noise > self.noise/10:
                    break
            return noise
    
        def _apply (self, x):
            df = pd.DataFrame ([[1.0,2.0],[3.0,4.0]], columns=['a','b']) + self._generate_noise ()
            if self.different:
                df = df+10
            x = np.array([[10.0,20.0],[30.0,40.0]]) + self._generate_noise ()
            result = dict(sequence=[[1.0,2.0], x+1, dict(vector=x, data=df)],
                          array=x+10)
            return result
    
    tr = MyTransform ()
    tr2= MyTransform ()
    tr.assert_equal (tr(1), tr2(1), significant_digits=7)
    
    with pytest.raises (AssertionError):
        tr = MyTransform (noise=1e-3, verbose=1)
        tr2= MyTransform (noise=1e-3, verbose=1)
        tr.assert_equal (tr(1), tr2(1), significant_digits=7)
    
    with pytest.raises (AssertionError):
        tr = MyTransform (verbose=1, different=True)
        tr2= MyTransform (verbose=1)
        tr.assert_equal (tr(1), tr2(1))
    
    result = tr.assert_equal (tr(1), tr2(1), raise_error=False)
    assert result is False
    remove_previous_results (path_results=path_results)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 24
def test_set_paths ():
    def assert_paths (x, path_results, path_models):
        base = os.path.abspath('.')
        assert x.path_results==Path(f'{base}/{path_results}')
        assert x.data_io.path_results==Path(f'{base}/{path_results}')
        assert x.path_models==Path(f'{base}/{path_models}')
        assert x.data_io.path_models==Path(f'{base}/{path_models}')
    
    path_results = 'test_set_paths_1'
    path_models = 'test_set_paths_1'
    tr = Component (path_results=path_results)
    assert_paths (tr, path_results, path_models)
    path_results = 'test_set_paths_2'
    tr.data_io.set_path_results (path_results)
    assert_paths (tr, path_results, path_models)
    path_models='test_set_paths_models_1'
    tr.data_io.set_path_models (path_models)
    assert_paths (tr, path_results, path_models)
    
    path_results = 'test_set_paths_a'
    path_models = 'test_set_paths_models_a'
    tr = Component (path_results=path_results, path_models=path_models)
    assert_paths (tr, path_results, path_models)
    
    path_results = 'test_set_paths_b'
    tr.data_io.set_path_results (path_results)
    assert_paths (tr, path_results, path_models)
    
    path_models = 'test_set_paths_models_b'
    tr.data_io.set_path_models (path_models)
    assert_paths (tr, path_results, path_models)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 25
def test_determine_fit_function ():
    # example when there is _fit implemented
    component = TransformWithoutFitApply ()
    X = np.array ([1,2,3])
    component.fit (X)
    X2 = np.array ([10,20,30])
    r = component (X2)
    assert (r == (X.sum() + X2)).all()
    assert component.is_model
    
    # example when there is estimator
    component = Component (DummyEstimator (2))
    X = np.array ([1,2,3])
    component.fit (X)
    assert component.estimator.sum == 6
    X2 = np.array ([10,20,30])
    r = component (X2)
    assert (r == (X.sum() + X2*2)).all()
    assert component.is_model
    
    # example when there is no _fit implemented, and there is no estimator
    component = TransformWithoutFit ()
    X = np.array ([1,2,3])
    component.fit (X)
    X2 = np.array ([10,20,30])
    r = component (X2)
    assert (r == (X2*2)).all()
    assert not component.is_model
    assert component._fit == component._fit_
    
    # example when there is only fit_apply implemented
    component = TransformWithFitApplyOnly ()
    X2 = np.array ([10,20,30])
    r = component.fit_apply (X2)
    assert (r == (X2 + X2.sum(axis=0)*10)).all()
    assert component.is_model
    assert component._fit == component._fit_
    
    #| test use_fit_from_loaded_estimator 
    path_models = 'test_use_fit_from_loaded_estimator'
    component = Component (DummyEstimator (2), path_models=path_models)
    X = np.array ([1,2,3])
    component.fit (X)
    assert (Path (path_models) / 'models').exists()
    del component
    
    estimator1 = DummyEstimator (2)
    print (estimator1)
    component = Component (estimator1, path_models=path_models)
    print ('before loading')
    print (component.estimator)
    print (component._fit)
    print (component.result_func)
    
    component.load_estimator ()
    print ('after loading')
    print (component.estimator)
    print (component._fit)
    print (component.result_func)
    
    assert component.estimator.sum == 6
    assert component.is_model
    
    X2 = np.array ([10,20,30])
    r = component (X2)
    assert (r == (X.sum() + X2*2)).all()
    
    remove_previous_results (path_models)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 26
def test_direct_methods ():
    # input
    X = np.array ([1,2,3])
    
    # example where we do not use direct methods
    component = Max10direct (verbose=2)
    component.fit (X)
    r = component (X)
    assert (r==X*10+X.max()).all()
    
    component = Max10direct (verbose=2, error_if_apply=True)
    component.fit (X)
    with pytest.raises (RuntimeError):
        r = component (X)
    #assert component.fitted
    #assert component.applied
    
    # example where we use direct methods
    component = Max10direct (direct_apply=True, verbose=2, error_if_apply=True)
    component.logger.info (f'{"-"*100}')
    component.logger.info (f'direct_apply={component.direct_apply}, direct_fit={component.direct_fit}, direct_fit_apply={component.direct_fit_apply}\n')
    component.fit (X)
    r = component (X)
    assert (r==X*10+X.max()).all()
    #assert component.fitted
    #assert not component.applied
    
    component = Max10direct (direct_fit=True, verbose=2, error_if_fit=True)
    component.logger.info (f'{"-"*100}')
    component.logger.info (f'direct_apply={component.direct_apply}, direct_fit={component.direct_fit}, direct_fit_apply={component.direct_fit_apply}\n')
    component.fit (X)
    r = component.apply (X)
    assert (r==X*10+X.max()).all()
    #assert not component.fitted
    #assert component.applied
    
    component = Max10direct (direct_apply=True, direct_fit=True, verbose=2, error_if_apply=True, 
                             error_if_fit=True)
    component.logger.info (f'{"-"*100}')
    component.logger.info (f'direct_apply={component.direct_apply}, direct_fit={component.direct_fit}, direct_fit_apply={component.direct_fit_apply}\n')
    component.fit (X)
    r = component.transform (X)
    assert (r==X*10+X.max()).all()
    #assert not component.fitted
    #assert not component.applied
    
    # example when there is no _fit implemented and we call fit_apply
    component = Multiply10direct (verbose=2, error_if_fit=True)
    component.logger.info (f'{"-"*100}')
    component.logger.info (f'direct_apply={component.direct_apply}, direct_fit={component.direct_fit}, direct_fit_apply={component.direct_fit_apply}\n')
    r = component.fit_apply (X)
    assert (r==X*10).all()
    #assert not component.is_model
    assert component.fit == component._fit_
    #assert component.fit_apply == component.apply
    r2 = component.fit (X).apply (X)
    assert (r==X*10).all()
    
    # example when there is no _fit implemented and we want a direct apply call
    component = Multiply10direct (verbose=2, direct_apply=True, error_if_apply=True, error_if_fit=True)
    component.logger.info (f'{"-"*100}')
    component.logger.info (f'direct_apply={component.direct_apply}, direct_fit={component.direct_fit}, direct_fit_apply={component.direct_fit_apply}\n')
    r = component.fit_apply (X)
    assert (r==X*10).all()
    assert not component.is_model
    assert component.fit == component._fit_
    #assert component.fit_apply == component._apply
    #assert component.fit_transform == component._apply
    #assert not component.applied
    r2 = component.fit (X).apply (X)
    assert (r==X*10).all()
    #assert not component.applied


# %% ../../../nbs/00_tests/core/tst.components.ipynb 27
def test_pass_apply ():
    component = Component (apply=lambda x: x*10, verbose=2, direct_apply=True, error_if_apply=True)
    X = np.array ([1,2,3])
    r = component (X)
    assert (r==X*10).all()


# %% ../../../nbs/00_tests/core/tst.components.ipynb 28
def test_wrapping_estimator ():
    estimator = DummyEstimatorWithLabels ()
    c = Component (estimator)
    X = np.array ([100, 90, 10])
    y = np.array ([1, 2, 3])
    c.fit (X, y)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 29
def test_get_specific_data_io_parameters_for_component ():
    component = Component (tag='data', x=3, par=[1,2], path_results='hello', path_results_data='world', 
                           other='yes', load_result_data = False, save_model_data=True)
    check_last_part(component.path_results, 'world')
    assert component.data_io.load_result_flag == False
    assert component.data_io.save_model_flag == True


# %% ../../../nbs/00_tests/core/tst.components.ipynb 30
def test_get_specific_data_io_parameters ():
    component = Component ()
    config = component.get_specific_data_io_parameters (
        'data', **dict(x=3, par=[1,2], path_results='hello', path_results_data='world', other='yes', 
                       load_result_data = True))
    assert config == dict (path_results='world', load_result=True)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 31
def test_set_suffix ():
    component = Component (name='my_component')
    assert component.name == 'my_component'
    component.set_suffix ('first')
    assert component.name == 'my_component_first'
    component.set_suffix ('second')
    assert component.name == 'my_component_second'
    component.set_suffix ('third')
    assert component.name == 'my_component_third'
    
    component.set_name ('another')
    assert component.name == 'another'
    
    component.set_suffix ('first')
    assert component.name == 'another_first'
    component.set_suffix ('second')
    assert component.name == 'another_second'
    
    component.set_name ('last')
    assert component.name == 'last'
    component.set_suffix ('first')
    assert component.name == 'last_first'
    component.set_suffix ('second')
    assert component.name == 'last_second'


# %% ../../../nbs/00_tests/core/tst.components.ipynb 32
def test_compare_kwargs ():
    class A (Component):
        def __init__ (self, x, y=1, z=2, **kwargs):
            super ().__init__ (**kwargs)
    
    a = A(3, verbose=2, error_if_kwargs_mismatch=True)
    with pytest.raises (ValueError):
        a = A(3, verbos=2, error_if_kwargs_mismatch=True)
    a = A(3, verbos=2)
    a = A(3, verbos=2, compare_kwargs=True)
    a = A(3, z=3, verbose=2, error_if_kwargs_mismatch=True)
    with pytest.raises (ValueError):
        a = A(3, zs=3, verbose=2, error_if_kwargs_mismatch=True)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 33
def test_build_partial ():
    def my_f (x, p=3):
      return x+p
    
    c = Component(my_f, build_partial=False, p=30)
    assert c (4)==7
    
    c = Component(my_f, build_partial=True, p=30)
    assert c (4)==34
    
    c = Component(my_f, p=30)
    assert c (4)==34


# %% ../../../nbs/00_tests/core/tst.components.ipynb 34
def test_sampling_component ():
    c = SamplingComponent (data_converter='DataConverter')
    assert c.apply_uses_labels
    assert not hasattr(c.data_converter,'apply_uses_labels')
    c = SamplingComponent (data_converter='PandasConverter')
    assert c.data_converter.apply_uses_labels


# %% ../../../nbs/00_tests/core/tst.components.ipynb 35
def test_sklearn_component ():
    c = SklearnComponent ()
    assert c.data_io.fitting_load_func==joblib.load
    assert c.data_io.result_save_func==joblib.dump


# %% ../../../nbs/00_tests/core/tst.components.ipynb 36
def test_no_saver_component ():
    c = NoSaverComponent ()
    assert c.data_io.__class__.__name__ == 'NoSaverIO'


# %% ../../../nbs/00_tests/core/tst.components.ipynb 37
def test_one_class_sklearn_component ():
    path_results = 'one_class_sklearn_component'
    remove_previous_results (path_results=path_results)
    
    data, y = get_data_for_one_class ()
    
    result1 = OneClassSklearnComponent (MinMaxScaler()).fit(data,y).transform (data)
    result2 = MinMaxScaler().fit(data[y==0]).transform (data)
    assert (result1==result2).all().all()
    
    remove_previous_results (path_results=path_results)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 38
def test_pandas_component ():
    c = PandasComponent ()
    assert c.data_converter.__class__.__name__ == 'PandasConverter'
    assert c.data_io.__class__.__name__ == 'PandasIO'


# %% ../../../nbs/00_tests/core/tst.components.ipynb 39
def test_io ():
    # If no arguments are given, no results are saved or loaded. The average execution 
    # time is 0.5 seconds.
    #%timeit f(3)
    
    # If given `path_results`, the result is stored:
    path_results = 'test_io'
    name = 'my_decorator'
    assert f (3, path_results=path_results, name=name)==4
    assert os.path.exists (f'{path_results}/whole/{name}_result.pk')
    
    # Subsequent calls to this function will load the pre-computed results, so that the 
    # execution time is much lower.
    #%timeit f (3, path_results='test_decorator', name='my_result')
    assert f (3, path_results=path_results, name=name)==4
    
    # if no name is given, the name from the function is used
    f (3, path_results=path_results)
    assert os.path.exists (f'{path_results}/whole/f_result.pk')
    
    remove_previous_results (path_results)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 40
def test_pandas_io ():
    # If no arguments are given, no results are saved or loaded. The average execution time is 1 second.
    #%timeit g(3)
    
    # If given `path_results`, the result is stored:
    path_results = 'test_pandas_io'
    name='my_pandas'
    df = pd.DataFrame ({'a':[1,2,3], 'b': [4,5,6]})
    result = g (df, path_results=path_results, name=name)
    assert (result==pd.DataFrame ({'a':[2,3,4], 'b': [5,6,7]})).all().all()
    assert os.path.exists (f'{path_results}/whole/{name}_result.parquet')
    
    # Subsequent calls to this function will load the pre-computed results, so that the execution time is much lower.
    #%timeit g (df, path_results=path_results, name=name)
    result = g (df, path_results=path_results, name=name)
    assert (result==pd.DataFrame ({'a':[2,3,4], 'b': [5,6,7]})).all().all()
    
    remove_previous_results (path_results)


# %% ../../../nbs/00_tests/core/tst.components.ipynb 41
def test_component_decorator ():
    assert add_one().class_name == 'AddOne'
    assert add_one()(1)==2

