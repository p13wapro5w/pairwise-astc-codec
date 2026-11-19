"""第 58 批：同一张法线贴图在手机上正常，切到 PC 后金属表面出现一块块方格..."""

def astc_block_size(width, height):
    """按纹理形状返回 ASTC 块尺寸。"""
    raise NotImplementedError("TODO: astc_block_size")

def channel_scale(value, bits):
    """按通道位数量化。"""
    raise NotImplementedError("TODO: channel_scale")

def decode_mode(is_srgb):
    """返回解码色彩空间。"""
    raise NotImplementedError("TODO: decode_mode")

def alpha_value(alpha, cutoff):
    """按 alpha 裁剪阈值返回。"""
    raise NotImplementedError("TODO: alpha_value")

def normalize_normal(normal):
    """归一化法线。"""
    raise NotImplementedError("TODO: normalize_normal")

def mip_count_for(resolution):
    """按分辨率返回 mip 数。"""
    raise NotImplementedError("TODO: mip_count_for")

def edge_fade(x, block):
    """返回块边界衰减。"""
    raise NotImplementedError("TODO: edge_fade")

def asset_key(path, version):
    """返回压缩缓存键。"""
    raise NotImplementedError("TODO: asset_key")

def array_layer_key(layer, slice_index):
    """返回纹理数组层键。"""
    raise NotImplementedError("TODO: array_layer_key")

def hdr_endpoint(value, max_value):
    """压缩 HDR 端点。"""
    raise NotImplementedError("TODO: hdr_endpoint")
