reports = {}


def report_format(format_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if format_type not in reports:
                reports[format_type] = {}
            reports[format_type] = (func(*args, **kwargs))

        return wrapper

    return decorator


# Пример использования
@report_format('PDF')
def generate_pdf_report(data):
    # Генерация отчета в формате PDF
    return data


@report_format('Excel')
def generate_excel_report(data):
    # Генерация отчета в формате Excel
    return data


@report_format('JSON')
def generate_json_report(data):
    # Генерация отчета в формате JSON
    return data


# Генерация отчетов для организации
data = {'organization_id': 1, 'year': 2021, 'expenses': 100000}
generate_pdf_report(data)
generate_excel_report(data)
generate_json_report(data)

# Вывод отчетов для определенной организации в указанном формате
print(reports)
print(reports['PDF'])
print(reports['Excel'])
print(reports['JSON'])
