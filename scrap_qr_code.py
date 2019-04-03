from utils import get_pattern


url = "https://smiley.codes/qrcode/qrcode.php"

data = {
    'inputstring': 'string',
    'version': '1',
    'maskpattern': '-1',
    'ecc': 'L',
    'quietzonesize': '4',
    'output_type': 'text',
    'scale': '5',
    'm_finder_light': 'FFFFFF',
    'm_finder_dark': 'FFFFFF',
    'm_alignment_light': 'FFFFFF',
    'm_alignment_dark': 'FFFFFF',
    'm_timing_light': 'FFFFFF',
    'm_timing_dark': 'FFFFFF',
    'm_format_light': 'FFFFFF',
    'm_format_dark': 'FFFFFF',
    'm_version_light': 'FFFFFF',
    'm_version_dark': 'FFFFFF',
    'm_data_light': 'FFFFFF',
    'm_data_dark': 'FFFFFF',
    'm_darkmodule_dark': 'FFFFFF',
    'm_separator_light': 'FFFFFF',
    'm_quietzone_light': 'FFFFFF'
}


for version in range(1, 41):
    get_pattern("finder", version, data, url)
    get_pattern("alignment", version, data, url)
    get_pattern("timing", version, data, url)
    data['m_version_dark'] = '000000'
    get_pattern("format", version, data, url)
    data['m_version_dark'] = 'FFFFFF'
    get_pattern("darkmodule", version, data, url)
    get_pattern("separator", version, data, url)
