import methods


def test_parse_cg_file(tmp_path):
    cg_code = """uniform float4 color\nuniform float4x4 matrix\nuniform texobj texture\nuniform float2 uv [branch]\n"""
    file_path = tmp_path / "shader.cg"
    file_path.write_text(cg_code)

    uniforms = []
    sizes = []
    conditionals = []
    methods.parse_cg_file(str(file_path), uniforms, sizes, conditionals)

    assert uniforms == ["color", "matrix", "texture", "uv"]
    assert sizes == [4, 16, 1, 2]
    assert conditionals == ["uv"]

