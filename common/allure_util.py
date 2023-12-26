import os

temp_path = r'C:\Users\CAI\Documents\swtest\temp'
report_path = r'C:\Users\CAI\Documents\swtest\report'

def generate_report():
    os.system(f'allure generate {temp_path} -o {report_path} --clean')
    os.system(f'allure open -h 127.0.0.1 -p 8883 {report_path}')