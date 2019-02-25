import csv


def nested_list_to_csv(my_list, out_file):
    with open(out_file, 'w', newline='') as f:
        w = csv.writer(f)
        fieldnames = my_list[0].keys()  # solve the problem to automatically write the header

        w.writerow(fieldnames)
        for row in my_list:
            w.writerow(row.values())


def test():
    print("test")
