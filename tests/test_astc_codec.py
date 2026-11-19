import pytest
from assets import astc_codec as mod

CASES = [
    ("block_square", 'm.astc_block_size(64, 64) == (8, 8)'),
    ("block_small", 'm.astc_block_size(4, 4) == (4, 4)'),
    ("block_wide", 'm.astc_block_size(128, 4) == (8, 4)'),
    ("channel_mid", 'm.channel_scale(0.5, 8) == approx(0.502, rel=1e-3)'),
    ("channel_zero", 'm.channel_scale(0.0, 8) == approx(0.0)'),
    ("decode_srgb", 'm.decode_mode(True) == "srgb"'),
    ("decode_linear", 'm.decode_mode(False) == "linear"'),
    ("alpha_cut", 'm.alpha_value(0.1, 0.5) == approx(0.0)'),
    ("alpha_keep", 'm.alpha_value(0.6, 0.5) == approx(0.6)'),
    ("normal_y", 'm.normalize_normal((0.0, 2.0, 0.0)) == approx((0.0, 1.0, 0.0))'),
    ("mip", 'm.mip_count_for(64) == 7'),
    ("edge", 'm.edge_fade(0.0, 8) == approx(0.0)'),
    ("asset", 'm.asset_key("a", "v1") == "a#v1"'),
    ("layer", 'm.array_layer_key(2, 3) == (2, 3)'),
    ("hdr", 'm.hdr_endpoint(2000, 1000) == 1000')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
