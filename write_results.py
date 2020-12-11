import csv

# write the results from i_dt to a csv file
def writeResult(subject_id, results):
    file_name = f'{subject_id}_results.csv'
    with open(file_name, mode="w", newline='') as subject_data:
        csv_writer = csv.writer(subject_data, delimiter=',')
        csv_writer.writerow(['known','centroid_x', 'centroid_y', 'fix_dur'])
        for result in results:
            row_i = 0
            for row in result[1]:
                csv_writer.writerow([result[0], row[0], row[1], result[2][row_i]])
                row_i += 1
            csv_writer.writerow([])