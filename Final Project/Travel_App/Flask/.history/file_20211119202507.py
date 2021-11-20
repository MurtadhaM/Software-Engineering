from monkeylearn import MonkeyLearn# Instantiate the client Using your API key
from monkeylearn.exceptions import PlanQueryLimitError

ml = MonkeyLearn('0322b5749676f3fb91e8c3a6357d81228d61889f')

data = []
with open('/Users/m/Documents/GitHub/Data_Mining/text_data.json', 'r') as f:
    data.append(f.readline())
    
    from monkeylearn.exceptions import PlanQueryLimitError, MonkeyLearnException

try:
    response = ml.classifiers.classify('cl_oJNMkt2V', data=['My text'])
except PlanQueryLimitError as e:
    # No monthly queries left
    # e.response contains the MonkeyLearnResponse object
    print(e.error_code, e.detail)
except MonkeyLearnException:
    raise


response =  MonkeyLearn.classifiers('cl_oJNMkt2V', data, production_model=False, batch_size=200,
                                     auto_batch=True, retry_if_throttled=True)
            



 


batch_size = 200

def test_data():
    try:
        response = ml.classifiers.classify('cl_oJNMkt2V', data, batch_size=batch_size)
    except PlanQueryLimitError as e:
        partial_predictions = e.response.body  # The body of the successful responses
        non_2xx_raw_responses = r.response.failed_raw_responses  # List of requests responses objects
        print(e)
    else:
        predictions = response.body
        print(predictions)
        
        print(response.body)

print(response.plan_queries_allowed)
