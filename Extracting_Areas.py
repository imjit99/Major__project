import csv
data_list= []
def Extraction(start, dest):
    with open("mta_1706.csv", newline='') as csvfile:
    
        dataset = csv.DictReader(csvfile)
        for row in dataset: 
            """it will try to match the below given values from the dataset, i.e. 'mta_1706.csv'. if it matches then it will rewrite into a new dataset"""
            if row['OriginName']== start and row['DestinationName']==dest:
                data = (row['OriginName'], row['DestinationName'], row['RecordedAtTime'], row['VehicleLocation.Latitude'], row['VehicleLocation.Longitude'])
                data_list.append(data)
    # print(data_list)

    fields = ['OriginName', 'DestinationName', 'RecordedAtTime', 'VehicleLocation.Latitude', 'VehicleLocation.Longitude'] 
        
    # data rows of csv file 
    rows = data_list

    # assigning the name of thecsv file
    filename = "Bus_records54.csv"

    # writing to csv file 
    with open(filename, 'w', newline='') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
            
        # writing the fields 
        csvwriter.writerow(fields) 
            
        # writing the data rows 
        csvwriter.writerows(rows)
        
# Extraction("VALENTINE AV/E 192 ST", "CO-OP CITY EARHART LA via GUNHILL")


"""# if row['OriginName']=="4 AV/95 ST" and row['DestinationName']== "BROWNSVILLE ROCKAWAY AV" : #Bus_records00.csv
# if row['OriginName']=="TEARDROP/LAYOVER" and row['DestinationName']== "ROSEDALE LIRR STA via MERRICK" : #Bus_records01.csv
# if row['OriginName']=="SOUNDVIEW AV/STEPHENS AV" and row['DestinationName']== "WAKEFIELD 241 ST via WHITE PLS RD" : #Bus_records02.csv
# if row['OriginName']=="FLATBUSH AV/E 31 ST" and row['DestinationName']== "SUNSET PARK 1 AV - 58 ST" : #Bus_records03.csv
# if row['OriginName']=="VALENTINE AV/E 192 ST" and row['DestinationName']== "CO-OP CITY EARHART LA via GUNHILL" : #Bus_records04.csv
        """    