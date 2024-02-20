import logging # Documentation: https://docs.python.org/3/library/logging.html#module-logging
import requests # Documentation: http://requests.readthedocs.io

logger = logging.getLogger(__name__)

class WebAPI:
    '''
    This class connects to web APIs and provides a method for data import.


    Keyword arguments:
        
    url
        Pass a string representing the URL you wish to connect to.
    
    headers
        Pass a dictionary providing the access key.
    
    ~~~~~
    data_import()
    Returns data in json format.
    '''

    def __init__(self, *, url: str, headers: str) -> None:
        logger.info("WebAPI class instance created.")

        self.my_data = requests.get(url, headers = headers)
    

    def data_import(self) -> dict:
        '''
        Returns data in json format.
        '''
        logger.info("Method 'data_import' invoked.")

        try:

            # Exception is raised if connection fails
            if self.my_data.status_code != 200:
                logger.debug("Connection failed.")
                raise Exception
            
            # Returns json if connection succeeds
            else:                
                logger.debug("Connection succeeded.")
                return self.my_data.json()
            
        except Exception:
            # Reason for connection failure            
            logger.error(f"Code of responded HTTP Status: {self.my_data.status_code}")
            logger.error(f"Reason of responded HTTP Status: {self.my_data.reason}")