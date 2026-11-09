from openpyxl import load_workbook
import os


class ExcelUtils:

    @staticmethod
    def get_test_data(file_name, sheet_name="Sheet1"):

        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "Data",
            file_name
        )

        workbook = load_workbook(file_path, data_only=True)
        sheet = workbook[sheet_name]

        test_data = []

        # Start from row 2 because row 1 contains headers
        for row in sheet.iter_rows(min_row=2, values_only=True):

            if not any(value is not None for value in row):
                continue

            test_data.append(row)

        workbook.close()

        return test_data