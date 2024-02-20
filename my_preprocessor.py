import logging # Documentation: https://docs.python.org/3/library/logging.html#module-logging
import pandas as pd # Documentation: https://pandas.pydata.org/docs/reference/index.html

logger = logging.getLogger(__name__)

class MyPreprocessor:
    '''
    This class provides the following methods for preprocessing data:

    create_df()
    Either Creates a data frame from a dictionary or
    reads a csv file or an Excel file into a data frame.

    ~~~~~
    save_df()
    Writes a data frame either to a csv file (default) or an Excel sheet.

    ~~~~~
    drop_cols()
    Drops user-defined columns.

    ~~~~~
    rename_cols()
    User-defined renaming of columns.

    ~~~~~
    drop_rows()
    Drops duplicate rows, rows containing missing values, or user-defined rows.

    ~~~~~
    recode()
    Automatically or user-defined recoding of a selected column.
    '''

    def __init__(self) -> None:
        logger.info("MyPreprocessor class instance created.")

        self.my_df = pd.DataFrame()
        self.my_df_rows = self.my_df.shape[0]


    def create_df(self, *, dictionary: dict = False, path: str = False) -> None:
        '''
        Either creates a data frame from a dictionary or
        reads a csv file or an Excel file into a data frame.
        Other file extensions are not supported.

        Keyword arguments:

        dictionary
            Whether to create a data frame from a dictionary; False by default.
            Pass a dictionary. Keys of the dictionary become columns.
        
        path
            Whether to read a file into a data frame; False by default.
            Pass a string that specifies the directory.
        '''
        logger.info("Method 'create_df' invoked.")
        
        # Check whether kwargs where used correctly
        if not dictionary and not path:
            logger.error(f"No data import scheme specified.")
        elif dictionary and path:
            logger.error(f"Too many data import schemes specified.")
        else:
            # Procedure for creating data frame from a dictionary
            if dictionary:
                logger.debug(f"Dictionary was passed.")
                
                self.my_df = pd.DataFrame.from_dict(dictionary)
                logger.info(f"Created data frame from dictionary.")
            
            # Procedure for reading csv file or Excel file into data frame
            if path:
                # Identify file extension
                file_extension = path.rsplit(".")[-1]

                # Apply the appropriate command
                if file_extension == "csv":
                    logger.debug(f"File extension '.{file_extension}' was identified.")
                    
                    self.my_df = pd.read_csv(path)
                    logger.info(f"csv file read into data frame.")
                
                elif file_extension == "xlsx":
                    logger.debug(f"File extension '.{file_extension}' was identified.")
                    
                    self.my_df = pd.read_excel(path)
                    logger.info(f"Excel file read into data frame.")
                
                else:
                    logger.error(f"File extension '.{file_extension}' is not supported.")


    def save_df(self, *, path: str = "./my_data.csv") -> None:
        '''
        Writes a data frame either to a csv file (default) or an Excel sheet.
        Other file extensions are not supported.

        Keyword argument:
        
        path
            Pass a string that specifies the target directory.
            By default, the data frame is written to "./my_data.csv".
        '''
        logger.info("Method 'save_df' invoked.")

        # Identify file extension
        file_extension = path.rsplit(".")[-1]

        # Apply the appropriate command
        if file_extension == "csv":
            logger.debug(f"File extension '.{file_extension}' was identified.")

            self.my_df.to_csv(path)
            logger.info(f"Data frame saved to '{path}'.")

        elif file_extension == "xlsx":
            logger.debug(f"File extension '.{file_extension}' was identified.")

            self.my_df.to_excel(path)
            logger.info(f"Data frame saved to '{path}'.")

        else:
            logger.error(f"File extension '.{file_extension}' is not supported.")


    def drop_cols(self, *, labels: list) -> None:
        '''
        Drops user-defined columns.

        Keyword argument:

        labels
            Pass a list of column labels.
        '''
        logger.info("Method 'drop_cols' invoked.")
        # Check whether labels exist
        for label in labels:
            if label in self.my_df.columns:
                logger.debug(f"Column '{label}' is existent.")

                # Procedure for dropping columns
                self.my_df.drop(columns = label, inplace = True)
                logger.info(f"Dropped column '{label}'.")
            else:
                logger.error(f"Column '{label}' is non-existent.")


    def rename_cols(self, *, labels: dict) -> None:
        '''
        User-defined renaming of columns.

        Keyword argument:

        labels
            Pass a dictionary with existing column label and replacement label pairs.
        '''
        logger.info("Method 'rename_cols' invoked.")
        # Check whether labels exist
        for key in labels:
            if key in self.my_df.columns:
                logger.debug(f"Column '{key}' is existent.")

                # Procedure for renaming columns
                self.my_df.rename(columns = {key: labels[key]}, inplace = True)
                logger.info(f"Renamed column '{key}' to '{labels[key]}'.")
            else:
                logger.error(f"Column '{key}' is non-existent.")


    def drop_rows(self, *, dupl: bool = False, na: bool = False, labels: list = False) -> None:
        '''
        Drops duplicate rows, rows containing missing values, or user-defined rows.

        Keyword arguments:

        dupl
            Whether to drop duplicate rows; False by default.
            If set to True:
                All columns are considered for identifying duplicates.
                All duplicates are dropped except for the first occurrence.
                Row labels are not reset.
        na
            Whether to drop rows containing missing values; False by default.
            If set to True:
                Rows are dropped, if any missing values are present.
                Row labels are not reset.
        labels
            Whether to drop user-defined rows; False by default.
            Pass a list of row labels.
        '''
        logger.info("Method 'drop_rows' invoked.")

        # Procedure for removing duplicate rows
        if dupl:
            self.my_df.drop_duplicates(inplace = True, ignore_index = True)
            logger.info(f"Duplicate rows dropped: {self.my_df_rows - self.my_df.shape[0]}.")

            self.my_df_rows -= self.my_df_rows - self.my_df.shape[0]
            logger.info(f"Remaining rows: {self.my_df_rows}.")
        
        # Procedure for removing rows containing missing values
        if na:
            self.my_df.dropna(inplace = True, ignore_index = True)
            logger.info(f"Rows containing missing values dropped: {self.my_df_rows - self.my_df.shape[0]}.")

            self.my_df_rows -= self.my_df_rows - self.my_df.shape[0]
            logger.info(f"Remaining rows: {self.my_df_rows}.")
        
        if labels:
            # Check whether labels exist
            for label in labels:
                if label in self.my_df.index:
                    logger.debug(f"Label '{label}' is existent.")

                    # Procedure for removing user-defined rows
                    self.my_df.drop(index = label, inplace = True)
                    logger.info(f"Dropped row '{label}'.")
                else:
                    logger.error(f"Row '{label}' is non-existent.")
            
            logger.info(f"user-defined rows dropped: {self.my_df_rows - self.my_df.shape[0]}.")

            self.my_df_rows -= self.my_df_rows - self.my_df.shape[0]
            logger.info(f"Remaining rows: {self.my_df_rows}.")


    def recode(self, *, col_name: str, auto: bool = False, customized: dict = False) -> None:
        '''
        Automatically or user-defined recoding of a selected column.
        
        Keyword arguments:
        
        col_name
            Pass the label of the column to be recoded.
        auto
            Whether to automatically recode a selected column; False by default.
            If set to True:
            All unique values are replaced with integers in ascending order starting at zero.
        customized
            Whether to recode user-defined a selected column; False by default.
            Pass a dictionary with existing value and replacement value pairs.
        '''
        logger.info("Method 'recode' invoked.")

        # Check whether col_name is an existing column label
        if col_name in self.my_df.columns:
            logger.debug(f"Column '{col_name}' is existent.")

            # Check whether other kwargs where used correctly
            if not customized and not auto:
                logger.error(f"No recoding scheme specified.")
            elif customized and auto:
                logger.error(f"Too many recoding schemes specified.")
            else:
                # Procedure for automatically recoding of a selected column
                if auto:
                    logger.debug(f"Unique values in column '{col_name}': {len(pd.unique(self.my_df[col_name]))}.")
                    
                    auto_dict = {}
                    my_counter = 0

                    for value in pd.unique(self.my_df[col_name]):
                        auto_dict[value] = my_counter
                        my_counter += 1
                    
                    self.my_df.replace(to_replace = {col_name: auto_dict}, inplace = True)
                    logger.debug(f"Unique values in column '{col_name}' auto recoded: {my_counter}.")
                    logger.info(f"Coding plan: {auto_dict}")
                
                if customized:
                    logger.debug(f"Unique values in column '{col_name}': {len(pd.unique(self.my_df[col_name]))}.")
                    
                    corr_dict = {}
                    my_counter = 0
                    
                    # Check for existence of unique values to be replaced
                    for key in customized.keys():
                        if key in pd.unique(self.my_df[col_name]):
                            logger.debug(f"Unique value '{key}' is existent.")

                            corr_dict[key] = customized[key]
                            my_counter += 1

                        else:
                            logger.error(f"Unique value '{key}' is non-existent.")
                    
                    # Procedure for user-defined recoding of a selected column
                    self.my_df.replace(to_replace = {col_name: corr_dict}, inplace = True)
                    logger.debug(f"Unique values in column '{col_name}' user user-defined recoded: {my_counter}.")
                    logger.info(f"Coding plan: {corr_dict}")
        else:
            logger.error(f"Column '{col_name}' is non-existent.")