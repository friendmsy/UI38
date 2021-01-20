cd E:\software\Python3.8.3\UiAuto\report
python38 -m pytest --tests-per-worker 2 E:/software/Python3.8.3/UiAuto/bin/run.py --alluredir=E:/software/Python3.8.3/UiAuto/report-allure
cd E:\software\Python3.8.3\UiAuto\common\allure-2.13.6\bin
cmd /c allure generate E:/software/Python3.8.3/UiAuto/report-allure -o E:/software/Python3.8.3/UiAuto/report --clean
cd E:\software\Python3.8.3\UiAuto\common
ding.py