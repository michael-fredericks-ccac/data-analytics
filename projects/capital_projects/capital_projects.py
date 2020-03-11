import csv
import json

def get_data(file_path):
    with open(file_path, newline = '') as data_file:
        data = csv.DictReader(data_file)
        project_list = []
        for p in data:
            project_list.append(p)
    return project_list

def get_filter(json_file_path):
    with open(json_file_path) as json_file:
        json_data = json.load(json_file)
        filter = {}
        for j in json_data:
            if json_data[j] != '':
                filter.update( {j : json_data[j]} )
    return filter

def filter_projects(project_list, filter):
    filtered_projects = []
    for p in project_list:
        count = 0
        jcount = len(filter)
        for j in filter:
            if filter[j] == p[j]:
                count += 1
        if count == jcount:
            filtered_projects.append(p)
    return filtered_projects

def export_projects(filtered_projects):
    with open('capital_projects_filtered.csv', 'w', newline = '') as csv_file:
        sample_dict = filtered_projects[0]
        fieldnames = []
        for key in sample_dict:
            fieldnames.append(key)
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for p in filtered_projects:
            writer.writerow(p)
    print("A new csv file has been created with the filtered criteria.")

def main():
    project_list = get_data('capital_projects.csv')
    filter = get_filter('capital_projects.json')
    filtered_projects = filter_projects(project_list, filter)
    export_projects(filtered_projects)

main()