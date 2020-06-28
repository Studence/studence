import os
import tempfile

import clevercsv as csv


class CSVUtility:
    m_file_path = None

    def createCSVFile(self, fileName):
        self.m_file_path = os.path.join(tempfile.gettempdir(), fileName + '.csv')
        return csv.writer(open(self.m_file_path, "w"), delimiter=',', quoting=csv.QUOTE_ALL)

    def writeFile(self, file, row):
        file.writerow(row)

    def writeMultipleRowsFile(self, file, rows):
        file.writerows(rows)

    def csvFilePath(self):
        return self.m_file_path

    def removeFile(self):
        os.remove(self.m_file_path)
