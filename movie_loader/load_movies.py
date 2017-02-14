import requests
import sys


def POST_csv_data_to_db(csv_path):

    """
    loads csv movie data and makes post requests for each line in csv_file.
    """
    with open(csv_path, "r") as csv_file:
        
        # make list of headers off first line in csv
        headers = csv_file.readline().strip().lower().split(",")

        # need to skip data type line in csv 
        _ = csv_file.readline()
    
        for line in csv_file:
            # turns headers and line values into "header:line_value" dict used in POST
            POST_data = dict(zip(headers, line.strip().split(",")))

            r = requests.post("http://localhost:8000/movies/", data=POST_data)

            # raises error in script if request returns 400s or 500s  
            r.raise_for_status()    

        return


def interface(csv_path):
    """
    interface function allows this file to easily be included and run in another
    script if needed.
    """

    print("loading data into db through POST endpoint")
    POST_csv_data_to_db(csv_path)
    print("data in db")

    return 


def cli_interface():
    """
    wrapper_cli method that interfaces from commandline to function space.
    call the script with: 
    python load_movies.py <path to csv> 
    """
    try:
        # grabs csv file path passed in as command line arg
        csv_path = sys.argv[1]

    except:
        print("usage: {} <csv_file_path>".format(sys.argv[0]))
        sys.exit(1)
    interface(csv_path)


if __name__ == "__main__":
    cli_interface()