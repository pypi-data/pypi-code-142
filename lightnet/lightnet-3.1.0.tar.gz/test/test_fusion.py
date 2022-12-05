#
#   Test fusion module
#   Copyright EAVISE
#

import pytest
import torch
import lightnet as ln


@pytest.fixture(scope='module')
def input_tensor():
    def _input_tensor(dimension, channels=3, batch=1):
        return torch.rand(batch, channels, dimension, dimension)
    return _input_tensor


# Base classification networks
@pytest.mark.parametrize('network', ['Alexnet', 'Darknet19', 'Resnet50', 'VGG19'])
def test_fusion_classification_cpu(network, input_tensor):
    uut = getattr(ln.models, network)(10).eval()
    fusion = ln.network.module.Fusion(uut, (3, 1))
    it = input_tensor(uut.inner_stride, channels=4)

    output_tensor = fusion(it)
    assert output_tensor.dim() == 2
    assert output_tensor.shape[0] == it.shape[0]
    assert output_tensor.shape[1] == uut.num_classes


@pytest.mark.parametrize('network', ['Alexnet', 'Darknet19', 'Resnet50', 'VGG19'])
@pytest.mark.cuda
@pytest.mark.skipif(not torch.cuda.is_available(), reason='CUDA not available')
def test_fusion_classification_cuda(network, input_tensor):
    uut = getattr(ln.models, network)(10)
    fusion = ln.network.module.Fusion(uut, (3, 1)).to('cuda')
    it = input_tensor(uut.inner_stride, channels=4, batch=2).to('cuda')

    output_tensor = fusion(it)
    assert output_tensor.dim() == 2
    assert output_tensor.shape[0] == it.shape[0]
    assert output_tensor.shape[1] == uut.num_classes


# Anchor detection networks
@pytest.mark.parametrize('network', ['YoloV2', 'Yolt', 'YoloV3', 'ResnetYolo'])
def test_fusion_anchor_detection_cpu(network, input_tensor):
    uut = getattr(ln.models, network)(20).eval()
    fusion = ln.network.module.Fusion(uut, (3, 1))
    it = input_tensor(uut.inner_stride, channels=4)

    output_tensor = fusion(it)
    if isinstance(output_tensor, torch.Tensor):
        assert output_tensor.dim() == 4
        assert output_tensor.shape[0] == it.shape[0]
        assert output_tensor.shape[1] == uut.anchors.num_anchors * (5 + uut.num_classes)
        assert output_tensor.shape[2] == it.shape[2] // uut.stride
        assert output_tensor.shape[3] == it.shape[3] // uut.stride
    else:
        for i, tensor in enumerate(output_tensor):
            assert tensor.dim() == 4
            assert tensor.shape[0] == it.shape[0]
            assert tensor.shape[1] == uut.anchors.get_scale(i).num_anchors * (5 + uut.num_classes)
            assert tensor.shape[2] == it.shape[2] // uut.stride[i]
            assert tensor.shape[3] == it.shape[3] // uut.stride[i]


@pytest.mark.parametrize('network', ['YoloV2', 'Yolt', 'YoloV3', 'ResnetYolo'])
@pytest.mark.cuda
@pytest.mark.skipif(not torch.cuda.is_available(), reason='CUDA not available')
def test_fusion_anchor_detection_cuda(network, input_tensor):
    uut = getattr(ln.models, network)(20)
    fusion = ln.network.module.Fusion(uut, (3, 1)).to('cuda')
    it = input_tensor(uut.inner_stride, channels=4, batch=2).to('cuda')

    output_tensor = fusion(it)
    if isinstance(output_tensor, torch.Tensor):
        assert output_tensor.dim() == 4
        assert output_tensor.shape[0] == it.shape[0]
        assert output_tensor.shape[1] == uut.anchors.num_anchors * (5 + uut.num_classes)
        assert output_tensor.shape[2] == it.shape[2] // uut.stride
        assert output_tensor.shape[3] == it.shape[3] // uut.stride
    else:
        for i, tensor in enumerate(output_tensor):
            assert tensor.dim() == 4
            assert tensor.shape[0] == it.shape[0]
            assert tensor.shape[1] == uut.anchors.get_scale(i).num_anchors * (5 + uut.num_classes)
            assert tensor.shape[2] == it.shape[2] // uut.stride[i]
            assert tensor.shape[3] == it.shape[3] // uut.stride[i]
