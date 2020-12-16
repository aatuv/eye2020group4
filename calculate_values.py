import csv, math, statistics
import os
from fixation_detection import unitsToVisualDegrees

def distance(x2, x1, y2, y1):
    dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return dist

def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

def calculateMFL_MSA(filename, subject_name, subject_results):
    with open(f'{filename}.csv', mode="a", newline='') as calc_data:
        csv_writer = csv.writer(calc_data, delimiter=',')
        try: # first row 
            if os.path.getsize(f'{filename}.csv') == 0:
                csv_writer.writerow(['subject_id', 'MFD_true', 'MFD_SD_true', 'MFD_false', 'MFD_SD_false', 'MSA_true', 'MSA_SD_true', 'MSA_false', 'MSA_SD_false', 'MFD_overall', 'MFD_overall_SD', 'MSA_overall', 'MSA_overall_SD'])
        except OSError as e:
            print(e.strerror)

        sa_total_f = [] # saccade amplitudes for known=false
        fd_total_f = [] # fixation durations for known=false
        fd_count_f = 0 # fixation duration result count for known=false
        sa_count_f = 0 # saccade amplitude result count for known=false
        sa_total_t = [] # saccade amplitude summed total for known=true
        fd_total_t = [] # fixation duration summed total for known=true
        fd_count_t = 0 # fixation duration row count for known=true
        sa_count_t = 0 # saccade amplitude row count for known=true
        i = 0
        # run through each sample for the results given by the i-dt algorithm
        for sample_result in subject_results:
            known = sample_result[0]
            j = 0
            # take the result from i_dt for a sample and process it further
            for fd in sample_result[2]:
                if known == 'true':
                    fd_total_t.append(fd)
                    fd_count_t += 1
                    if j > 0: # start calculating saccade amplitudes with the second processed value
                        last_cntr = sample_result[1][j - 1]
                        cur_cntr = sample_result[1][j]
                        sa_total_t.append(distance(cur_cntr[0], last_cntr[0], cur_cntr[1], last_cntr[1]))
                        sa_count_t += 1
                else: # known is false
                    fd_total_f.append(fd)
                    fd_count_f += 1
                    if j > 0:
                        last_cntr = sample_result[1][j - 1]
                        cur_cntr = sample_result[1][j]
                        sa_total_f.append(distance(cur_cntr[0], last_cntr[0], cur_cntr[1], last_cntr[1]))
                        sa_count_f += 1
                j += 1
            i += 1
        # finally calculate all needed values and add a new result to calculations.csv for this subject
        mfd_true = sum(fd_total_t)/ fd_count_t
        mfd_sd_true = stdev(fd_total_t)
        mfd_false = sum(fd_total_f)/ fd_count_f
        mfd_sd_false = stdev(fd_total_f)
        msa_true = unitsToVisualDegrees(sum(sa_total_t) / sa_count_t)
        msa_sd_true = unitsToVisualDegrees(stdev(sa_total_t))
        msa_false = unitsToVisualDegrees(sum(sa_total_f) / sa_count_f)
        msa_sd_false = unitsToVisualDegrees(stdev(sa_total_f))
        mfd_overall = (sum(fd_total_t) + sum(fd_total_f)) / (fd_count_t + fd_count_f)
        fd_total_f.extend(fd_total_t)
        mfd_overall_sd = stdev(fd_total_f)
        msa_overall = unitsToVisualDegrees((sum(sa_total_t) + sum(sa_total_f)) / (sa_count_t + sa_count_f))
        fd_total_f.extend(fd_total_t)
        msa_overall_sd = unitsToVisualDegrees(stdev(sa_total_f))
        # write a row for this subject
        csv_writer.writerow([subject_name, mfd_true, mfd_sd_true, mfd_false, mfd_sd_false, msa_true, msa_sd_true, msa_false, msa_sd_false, mfd_overall, mfd_overall_sd, msa_overall, msa_overall_sd])