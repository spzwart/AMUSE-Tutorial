import csv
import numpy as np

def new_option_parser():
    from optparse import OptionParser
    result = OptionParser()
    result.add_option("-f", dest="input_filename", 
                      default = "../Scores/Group_1_scores.csv",
                      help="input filename [%default]")
    return result
    
if __name__ in ('__main__', '__plot__'):
    o, arguments  = new_option_parser().parse_args()

    rows = []
    with open(o.input_filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        presentation = []
        gitusage = []
        report = []
        for row in reader:
            rows.append({
                "category": row["category"],
                "item": row["item"],
                "value": float(row["value"])
            })
            if row["category"]=="participation":
                presentation.append(float(row["value"]))
            elif row["category"]=="git usage":
                gitusage.append(float(row["value"]))
            elif row["category"]=="report":
                report.append(float(row["value"]))
            print(row)
    print(f"{np.mean(presentation)} +/- {np.std(presentation)}")
    print(f"{np.mean(gitusage)} +/- {np.std(gitusage)}")
    print(f"{np.mean(report)} +/- {np.std(report)}")

