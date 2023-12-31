import os


def generate_report(temp_path,report_path):
    os.system(f'allure generate {temp_path} -o {report_path} --clean')
    os.system(f'allure open -h 127.0.0.1 -p 8883 {report_path}')