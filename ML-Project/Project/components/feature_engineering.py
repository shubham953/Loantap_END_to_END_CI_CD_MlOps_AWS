import sys
sys.path.append('D:\Desktop\Loantap_END_to_END_CI_CD_MlOps_AWS\ML-Project')
import os
from Project import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from Project.entity.config_entity import Datafeature_engineeringConfig


class Feature_Engineering:
    def __init__(self, config: Datafeature_engineeringConfig):
        self.config = config    
    def pub_rec(number):
        if number == 0.0:
            return 0
        else:
            return 1
    def mort_acc(number):
        if number == 0.0:
            return 0
        elif number >= 1.0:
            return 1
        else:
            return number
    def pub_rec_bankruptcies(number):
        if number == 0.0:
            return 0
        elif number >= 1.0:
            return 1
        else:
            return number

    def get_data(self) :
        data = pd.read_csv(self.config.data_path)
        data['mort_acc'] = data.mort_acc.apply(mort_acc)
        data['pub_rec_bankruptcies'] = data.pub_rec_bankruptcies.apply(pub_rec)
            #maping of target variable
        data['loan_status'] = data.loan_status.map({'Fully Paid':0, 'Charged Off':1})
        data.to_csv(os.path.join(self.config.root_dir, "featured_data.csv"),index = False)

            