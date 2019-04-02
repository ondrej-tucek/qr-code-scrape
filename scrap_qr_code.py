from pipetools import pipe

from utils import download_qr_code, hex_to_qr_matrix, save_to_csv


url = "https://smiley.codes/qrcode/qrcode.php"

data = {
  'inputstring': 'sud3kjMyFwClBcBoAVBaAIwWAKUFwGgBUFoAjBYApQXAaAFQWgCMFgClBcBoAVBaAIwWAK',
  'version': '5',
  'maskpattern': '-1',
  'ecc': 'L',
  'quietzonesize': '4',
  'output_type': 'text',
  'scale': '5',
  'm_finder_light': 'FFFFFF',
  'm_finder_dark': '000000',
  'm_alignment_light': 'FFFFFF',
  'm_alignment_dark': '000000',
  'm_timing_light': 'FFFFFF',
  'm_timing_dark': '000000',
  'm_format_light': 'FFFFFF',
  'm_format_dark': '000000',
  'm_version_light': 'FFFFFF',
  'm_version_dark': '000000',
  'm_data_light': 'FFFFFF',
  'm_data_dark': '000000',
  'm_darkmodule_dark': '000000',
  'm_separator_light': 'FFFFFF',
  'm_quietzone_light': 'FFFFFF'
}



(url, data) > pipe\
    | (lambda x: download_qr_code(x[0], x[1]))\
    | hex_to_qr_matrix\
    | (lambda x: save_to_csv(x, "name"))
