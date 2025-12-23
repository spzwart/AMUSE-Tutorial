import csv
import numpy as np

def new_option_parser():
    from optparse import OptionParser
    result = OptionParser()
    result.add_option("-f", dest="input_filename", 
                      default = "../Scores/Group_1_scores.csv",
                      help="input filename [%default]")
    result.add_option("--verbose", dest="verbose", 
                      default = "0", type = "int", 
                      help="verbosity [%default]")
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
            if o.verbose:
                print(row)
    group = o.input_filename.split("/")[-1]
    print(f"\nVerdict for the course in Simulation and Modeling in Astrophyiscs for group {group}")
    print(f"Presentation: {np.mean(presentation)} +/- {np.std(presentation)}")
    print(f"Git usage: {np.mean(gitusage)} +/- {np.std(gitusage)}")
    print(f"Report: {np.mean(report)} +/- {np.std(report)}")

    verdict_score = (np.mean(presentation) + np.mean(gitusage) + np.mean(report))/3.0
    verdict_disp  = np.sqrt(np.std(presentation)**2 + np.std(gitusage)**2 + np.std(report)**2)/3.0
    print(f"Final score = {verdict_score:0.1f} +/- {verdict_disp:0.1f}")
