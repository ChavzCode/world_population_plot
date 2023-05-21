import csv
import utils.logs as logs

def get_dataset(path):
    try:
        with open(path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            header = next(reader)
            dataset = []
        
            for r in reader:
                row_zipped = zip(header, r)
                row = {key: value for key, value in row_zipped}
                dataset.append(row)   

            return dataset  

    except Exception as error:
        print("Oops... Something went wrong")
        logs.log_error("./logs.txt", error)
    

def get_population_by_country(country_query, dataset):
    filtered_country = list(filter(lambda x: x["Country/Territory"] == country_query, dataset))
    country_population = {key[0:4]: int(value) for key, value in filtered_country[0].items() if "Population" in key and "World" not in key}
    sorted_population = dict(sorted(country_population.items()))
    result = (list(sorted_population.keys()), list(sorted_population.values()) )
    return result

def get_global_population(dataset, limit=10):
    population_percentage_per_country = {}
    for row in dataset:
        population_percentage_per_country[row['Country/Territory']] = float(row['World Population Percentage'])
    sorted_population_percentage = dict(sorted(population_percentage_per_country.items(), key=lambda x:x[1], reverse=True))    
    limited_dataset = dict(list(sorted_population_percentage.items())[0:limit])
    limited_dataset['Others'] = sum(list(sorted_population_percentage.values())[limit:])

    result = (limited_dataset.keys(), limited_dataset.values())
    return result