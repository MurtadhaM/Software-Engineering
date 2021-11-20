from monkeylearn import MonkeyLearn# Instantiate the client Using your API key
from monkeylearn.exceptions import PlanQueryLimitError
from monkeylearn.exceptions import PlanQueryLimitError, MonkeyLearnException

ml = MonkeyLearn('0322b5749676f3fb91e8c3a6357d81228d61889f')

data = []
with open('/Users/m/Documents/GitHub/Data_Mining/text_data.json', 'r') as f:
    data.append(f.readline())
    
    

def analyze():
    try:
        lim
        response = ml.classifiers.classify('cl_oJNMkt2V', data=data, batch_size=10)
    except PlanQueryLimitError as e:
        # No monthly queries left
        # e.response contains the MonkeyLearnResponse object
        print(e.error_code, e.detail)
        return response
    except MonkeyLearnException:
        raise





 


print(analyze())