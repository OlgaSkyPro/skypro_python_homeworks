# skypro_python_homeworks
Для правильной работы с Allure в Lesson10 необходимо:

1. Установить с сайта pypi, раздел allure-pytest
    
2. Чтобы терминал распознал команду Allure необходимо установить Allure Report
    
3. Для запуска теста test_form.py используем команду: pytest test_form.py --alluredir allur-result-form
4. Для просмотра сформированного отчета для теста test_form.py используем команду: allure serve allur-result-form

5. Для запуска теста test_calc.py используем команду: pytest test_calc.py --alluredir allur-result-calc
6. Для просмотра сформированного отчета для теста test_calc.py используем команду: allure serve allur-result-calc

7. Для запуска теста test_shop.py используем команду: pytest test_shop.py --alluredir allur-result-shop
8. Для просмотра сформированного отчета для теста test_shop.py используем команду: allure serve Sallur-result-shop
