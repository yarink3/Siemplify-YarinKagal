from DataModels import ConnectorParams
import os
class SubProcessInputOutputHandler(object):
    @property
    def connector_params(self):
        result = ConnectorParams()
        result.source_folder_path = (input("Please type the source folder path\n"))

        result.iteration_entities_count = int((input("Please type the iteration entities count\n")))

        return result

    def end(self, connector_result):
        """ connector_result is of type ConnectorResult"""

        for key in connector_result.alerts:
            print( key + " : " +connector_result.alerts[key])

        print( '\nYou can find all results details in Output_Folder/results <timestamp>.json\n')

        os. kill(os.getpid(),9)