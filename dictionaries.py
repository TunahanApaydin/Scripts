def getDictionary(dict):

    if dict == "pre_dict":
        predefined_dictionary = {
                    "11" : "0", # 2021 dataset için düzenlenecek
                    "10" : "1",
                    #" " : "2",
                    "15" : "3",
                    "14" : "4",
                    "8" : "5",
                    "9" : "6",
                    "2" : "7",
                    "4" : "8",
                    "7" : "9",
                    "0" : "10",
                    "13" : "11",
                    "3" : "12",
                    "6" : "13",
                    "16" : "14",
                    "5" : "15",
                    #" " : "16",
                    #" " : "17",
                    #" " : "18",
                    #" " : "19",
                    "17" : "20",
                    "1" : "21"
                }
        
        return predefined_dictionary
    
    else:
        other_dict = {
            "5" : "4",
            "4" : "8",
            "6" : "10",
            "10" : "2",
            "11" : "1",
            "3" : "5",
            "8" : "6",
            "0" : "18",
            "1" : "9",
            "7" : "3",
            "2" : "20",
            "9" : "0"
        }

        return other_dict