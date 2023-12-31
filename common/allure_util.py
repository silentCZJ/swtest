import os

temp_path = '../temp'
report_path = '../report'

def generate_report():
    os.system(f'allure generate {temp_path} -o {report_path} --clean')
    os.system(f'allure open -h 127.0.0.1 -p 8883 {report_path}')