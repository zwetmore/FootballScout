"""
This is the file that processes the csv files and creates the raw_data.csv file, 
it then cleans the data and creates the cleaned_data.csv file
"""
import pandas as pd
import os 
import re
import glob
import constants

class GameCSVSerializer:

    def create_folders_if_not_exist(self) -> None:
        """
        Creates the folders if they do not exist
        """
        if not os.path.exists(constants.PATH_TO_DATA_FOLDER):
            os.makedirs(constants.PATH_TO_DATA_FOLDER)
        if not os.path.exists(constants.PATH_TO_CSV_FOLDER):
            os.makedirs(constants.PATH_TO_CSV_FOLDER)
        if not os.path.exists(constants.PATH_TO_TRASH_FOLDER):
            os.makedirs(constants.PATH_TO_TRASH_FOLDER)
        return None
    
    def filepath(self, year, index) -> str | None:
        """
        Returns the filepath to the excel file for the given year and index
        Returns None if the file does not exist
        """
        file_path = f'{constants.PATH_TO_DATA_FOLDER}/PlaylistData_{year}_{index}.xlsx'
        if os.path.exists(file_path):
            return file_path
        else:
            print(f"File {file_path} does not exist.")
            return None

    def read_excel_write_to_csv(self, year, index) -> bool | None:
        """
        Reads the excel file for the given year and index and writes the data to a csv file
        Returns None if the file does not exist
        Returns True if the file is successfully written to csv
        """
        read_file = self.filepath(year, index)
        if read_file == None:
            return None
        
        # reads file, replaces empty strings with --
        df = pd.read_excel(read_file, dtype=str, na_values=[''])
        df.fillna('--', inplace=True)

        # writes to csv
        try:
            df.to_csv(f'{constants.PATH_TO_CSV_FOLDER}/PlaylistData_{year}_{index}.csv', index=False)
            return True
        except Exception as e:
            print(f"Error writing to csv: {e}")
            return None

    def get_years_and_indices(self) -> list[tuple[int, int]] | None:
        """
        Returns a list of tuples, where each tuple contains a year and an index
        Moves all files not named correctly to the trash folder
        """
        return_tuples = []
        try:
            # List all files and directories in the given directory
            file_names = os.listdir(constants.PATH_TO_DATA_FOLDER)

            for file_name in file_names:
                # moves files not named correctly to the trash folder
                if not re.match(r'PlaylistData_\d{4}_\d{1,2}\.xlsx', file_name):
                    new_file_name = f'{constants.PATH_TO_TRASH_FOLDER}/{file_name}'
                    os.rename(f'{constants.PATH_TO_DATA_FOLDER}/{file_name}', new_file_name)
                else:
                    # extracts the year and index from the file name
                    file_name = file_name.replace('.xlsx', '')
                    year = file_name.split('_')[1]
                    index = file_name.split('_')[2]
                    return_tuples.append((year, index))

            # if no files are found, return None
            if len(return_tuples) == 0:
                return None
            
            return return_tuples
        except Exception as e:
            print(f"Error accessing directory {constants.PATH_TO_DATA_FOLDER}: {e}")
            return None

    def read_all_excel_files(self) -> None:
        """
        Reads all the excel files in the data folder and writes the data to csv
        """
        # ensure the folders exist
        self.create_folders_if_not_exist()

        # get the years and indices
        years_and_indices = self.get_years_and_indices()
        if years_and_indices == None:
            return None

        # read the excel files and write the data to csv
        for year, index in years_and_indices:
            if self.read_excel_write_to_csv(year, index) == None:
                print(f"Error reading excel file year:{year} index:{index}")
                return None

        return None

    def empty_trash_folder(self) -> None:
        """
        Empties the trash folder
        """
        for file in os.listdir(constants.PATH_TO_TRASH_FOLDER):
            os.remove(f'{constants.PATH_TO_TRASH_FOLDER}/{file}')
        return None

class CSVConfigurator:

    def create_raw_data_csv(self) -> None:
        """
        Creates the RAW_DATA csv file
        Returns None
        """
        try:
            with open(f'{constants.PATH_TO_RAW_DATA_CSV}', 'a'):
                return None
        except Exception as e:
            print(f"Error creating raw_data csv: {e}")
            return None
    
    def write_csvs_to_raw_data_csv(self) -> None:
        """
        Writes the csv file to the RAW_DATA csv
        Returns None
        """
        try:
            print("Writing csvs to RAW_DATA csv...")
            # Path to the directory containing all CSV files
            csv_files = glob.glob(f'{constants.PATH_TO_CSV_FOLDER}/*.csv')

            # Combine all files in the list
            combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])

            # Export to CSV
            combined_csv.to_csv(f'{constants.PATH_TO_RAW_DATA_CSV}', index=False)

        except Exception as e:
            print(f"Error writing csvs to RAW_DATA csv: {e}")
        finally:    
            print("Done writing csvs to RAW_DATA csv")
            return None

class GameDataProcessor:    


    def process_game_data_1(self) -> None:
        """
        Processes the game data from the RAW_DATA csv
        Returns None

        This will eliminate all defense rows and rows with no data
        """
        print("Processing game data...")
        df = pd.read_csv(constants.PATH_TO_RAW_DATA_CSV)

        # eliminate all none offense rows
        df = df[df['ODK'] == 'O']

        # eliminate all columns with no data (all --)
        df.replace('--', pd.NA, inplace=True)  
        df.dropna(axis=1, how='all', inplace=True)
        df.fillna('--', inplace=True)

        # change all cells to lowercase
        df = df.map(lambda x: str(x).lower())

        # clean up some cells
        df.replace(f'"', '', inplace=True)
        
        # add a columns based on the result
        df['TD_SCORED'] = df['RESULT'].apply(lambda x: 1 if 'td' in x else 0)
        df['SAFETY'] = df['RESULT'].apply(lambda x: 1 if 'safety' in x else 0)
        df['FUMBLE'] = df['RESULT'].apply(lambda x: 1 if 'fumble' in x else 0)
        df['INTERCEPTION'] = df['RESULT'].apply(lambda x: 1 if 'interception' in x else 0)
        df['TURNOVER'] = df['SAFETY'] + df['FUMBLE'] + df['INTERCEPTION']

        # reduce result to the first word
        df['RESULT'] = df['RESULT'].apply(lambda x: x.split(',')[0])

        # remove rows with result == timeout
        df = df[df['RESULT'] != 'timeout']
    
        # map columns to data values
        df['OFF STR'] = df['OFF STR'].astype(str).map(constants.OFF_STR_MAPPING)
        df['PLAY DIR'] = df['PLAY DIR'].astype(str).map(constants.PLAY_DIR_MAPPING)
        df['PLAY TYPE'] = df['PLAY TYPE'].astype(str).map(constants.PLAY_TYPE_MAPPING)
        df['RESULT'] = df['RESULT'].astype(str).map(constants.RESULT_MAPPING)
        df['HASH'] = df['HASH'].astype(str).map(constants.HASH_MAPPING)

        # convert off formation to packages
        df['RB'] = df['OFF FORM'].astype(str).map(lambda x: constants.OFF_FORM_MAPPING[x]['rb'])
        df['TE'] = df['OFF FORM'].astype(str).map(lambda x: constants.OFF_FORM_MAPPING[x]['te'])
        df['WR'] = df['OFF FORM'].astype(str).map(lambda x: constants.OFF_FORM_MAPPING[x]['wr'])

        # remove formation column
        df.drop(columns=['OFF FORM'], inplace=True)

        # map off play names to more general names
        df['OFF PLAY'] = df['OFF PLAY'].astype(str).map(lambda x:
            "counter" if "auburn" in x or "tiger" in x else
            "power" if "wisconsin" in x or "badger" in x else
            "trap" if "minnesota" in x or "gopher" in x else
            "sweep" if "oregon" in x or "duck" in x else
            "wr screen" if "tunnel" in x else
            "rb screen" if "razor" in x else
            "trick play" if "medford" in x else
            "zone" if "michigan" in x or "wolverine" in x else
            "boot" if "boot" in x else
            "--" if "iowa" in x or "hawkeye" in x else
            "sweep/qb run" if "florida" in x or "gator" in x else
            "--" if "--" in x else
            "pass")

        df['OFF PLAY'] = df['OFF PLAY'].astype(str).map(constants.OFF_PLAY_MAPPING)
        # write to cleaned data csv
        df.to_csv(constants.PATH_TO_CLEANED_DATA_CSV, index=False)
        print("Done processing game data")
if __name__ == "__main__":
    # read all excel files
    game_csv_serializer = GameCSVSerializer()
    game_csv_serializer.read_all_excel_files()

    # create RAW_DATA csv   
    csv_configurator = CSVConfigurator()
    csv_configurator.create_raw_data_csv()

    # write csvs to RAW_DATA csv
    csv_configurator.write_csvs_to_raw_data_csv()

    # process game data and create cleaned_data.csv
    game_data_processor = GameDataProcessor()
    game_data_processor.process_game_data_1()

    print("Finished Script")
