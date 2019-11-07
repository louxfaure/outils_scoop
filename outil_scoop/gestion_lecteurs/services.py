import os
from collections import OrderedDict
from Alma_Apis_Interface import Alma_Apis_Users

# INSTITUTIONS_LIST = ['NETWORK','UB','UBM','IEP','INP','BXSA']
INSTITUTIONS_LIST = ['NETWORK','UB','BXSA']

class User(object):
    """Retourne la liste des institutions où le compte du lecteur est présent. Pour chaque institution retourne le nombre de prêt
    
    Arguments:
        user_id {str} -- identifiant du lecteur
    """
    def __init__(self,user_id):
        self.error = False
        self.error_institution = ""
        self.error_message =""
        self.user_data = OrderedDict()
        self.nb_prets = 0
        self.nb_demandes = 0
        for institution in INSTITUTIONS_LIST :
            # api_key = os.getenv("PROD_{}_USER_API".format(institution))
            api_key = os.getenv("TEST_{}_API".format(institution))
            api = Alma_Apis_Users.AlmaUsers(apikey=api_key, region='EU', service='test')
            status, response = api.retrieve_user_by_id(user_id, accept='json')
            # print("{} --> {} : {}".format(institution,status,response))
            if status == "Success":
                total_record_count = response['total_record_count']
                if total_record_count == 1 :
                    # user_institutions_list.append(institution)
                    status,user = api.get_user(user_id,accept='json')
                    self.user_data[institution]=user
                    # self.user_data[institution]={}
                    # self.user_data[institution]["user_group"] = user["user_group"]["value"]
                    # self.user_data[institution]["account_type"] = user["account_type"]["value"]
                    # self.user_data[institution]["loans"] = user["loans"]["value"]
                    # self.user_data[institution]["requests"] = user["requests"]["value"]
                    # self.user_data[institution]["record_type"] = user["record_type"]
                    # self.user_data[institution]["full_name"] = user["full_name"]
                    # self.user_data[institution]["job_category"] = user["job_category"]
                    # self.user_data[institution]["expiry_date"] = user["expiry_date"]
                    self.nb_prets += user["loans"]["value"]
                    self.nb_demandes += user["requests"]["value"]
            else:
                self.error = True
                self.error_institution = institution
                self.error_message = response
                break

    @property
    def get_error_status(self):
        return self.error

    def get_error_message(self):
        return self.error_message

    def ckeck_if_unknowed_user(self):
        if len(self.user_data) == 0:
            return True
        else:
            return False 
    
    def is_not_deletable(self):
        if (self.nb_demandes + self.nb_prets) == 0:
            return "false"
        else:
            return "true"

    def get_user_institutions_string(self):
        return ",".join(self.user_data.keys())

    def get_user_data_in_table(self,datas):
        user_data_in_table=OrderedDict()
        for data in datas:
            user_data_in_table[data] = []
            for inst in self.user_data:
                if isinstance(self.user_data[inst][data], dict):
                    user_data_in_table[data].append(self.user_data[inst][data]["value"])
                else:
                    user_data_in_table[data].append(self.user_data[inst][data])
        return user_data_in_table
            


            
