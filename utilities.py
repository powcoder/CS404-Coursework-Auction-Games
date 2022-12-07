https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
import csv
 
 
def export_to_csv(output_csv_file, data_list):
 
    with open(output_csv_file, 'a', newline='') as fp:
        a = csv.writer(fp, delimiter=';')
        data = [data_list]
        a.writerows(data)