import json
import os
import requests

from SubProcessInputOutputHandler import SubProcessInputOutputHandler
from DataModels import ConnectorResult
from datetime import datetime



def main():

    apiKey = "8b2c15fe5bb3d95439009f5d0d36cf5654f70bb815b66425698ed8c315c3464c"
    io_mgr = SubProcessInputOutputHandler()
    connector_params = io_mgr.connector_params

    # #TODO - delete this:
    # connector_params.source_folder_path="/home/yarink3/Desktop/Siemplify-YarinKagal/domains_folder"
    
    while(True):
        try:
            connector_result = ConnectorResult()
            url_data_to_result={}
            all_results={}
            url = 'https://www.virustotal.com/vtapi/v2/domain/report'

            # for each line in each in the domains files directory:
            # send an API request to the service and check for detected viruses the domain (line).
            keepRunning=False
            for filename in os.listdir(connector_params.source_folder_path):
                keepRunning=True
                counter=0
                with open(os.path.join(connector_params.source_folder_path, filename), 'r') as file:
                    if(counter > connector_params.iteration_entities_count):
                        break

                    if (file.name[-5:len(file.name)] != ".done"):
                        for domain in file:
                            if(counter < connector_params.iteration_entities_count):

                                indexN=domain.find("\n")
                                if(indexN != -1):
                                    domain=domain[0:len(domain)-1]
                                params = {'apikey': apiKey, 'domain': domain}

                                response = requests.get(url, params=params)

                                json_response = response.json()
                                detected_urls=json_response['detected_urls']
                                all_results[domain] = detected_urls
                                positives = sum(url_dict.get('positives', 0) for url_dict in detected_urls)
                                total = sum(url_dict.get('total', 0) for url_dict in detected_urls)

                                if(positives>0):
                                    url_data_to_result[domain]=\
                                        f"""We detected {positives} optional viruses out of {total} checks in the domain {domain}  """


                                else:
                                    url_data_to_result[domain] = "Not Suspicious"


                                counter +=1
                    if (file.name[-5:len(file.name)] != ".done"):
                        os.rename(file.name, file.name+".done")

            if(not keepRunning):
                break  

            connector_result.alerts=url_data_to_result
            print("Connector completed successfuly")

        except:
            print("Connector failed")

        now = datetime.now()  # current date and time
        date_time = now.strftime("%m-%d-%Y_%H_%M_%S")
        name='Output_Folder/results'+date_time+'.json'

        with open(name, 'w') as fp:
            json.dump(all_results, fp)
        name='Output_Folder/short_results' + date_time + '.json'

        with open(name, 'w') as fp:
            json.dump(url_data_to_result, fp)




        io_mgr.end(connector_result)

if __name__ == "__main__":
    main()