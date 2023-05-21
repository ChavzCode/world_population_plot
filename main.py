import utils.data as data_functions
import utils.charts as charts
import utils.logs as logs

def country_selection():
    try:
        country_choice = input("What country population would you like to see? => ")

        if(country_choice == ''):
            raise Exception("Country Cannot be empty")
        if(country_choice.isdigit()):
            raise Exception("Country Cannot be a digit")
            
        return str(country_choice).capitalize()
    
    except Exception as error:
        logs.log_error("./logs.txt", error)
        return False
    

def display_country_population():
    try:
        country_choice = country_selection() 
        dataset = data_functions.get_dataset("./data.csv")
        labels, values = data_functions.get_population_by_country(country_choice, dataset)
        charts.show_bar_chart(labels, values)
        charts.show_plot_chart(labels, values, country_choice)

    except Exception as error:
        logs.log_error("./logs.txt", error)
    
    
def display_global_population():
    dataset = data_functions.get_dataset("./data.csv");
    labels, values = data_functions.get_global_population(dataset, 10)
    charts.show_pie_chart(labels, values)

def run():
    display_country_population()
    display_global_population()

if __name__ == "__main__":
    run()