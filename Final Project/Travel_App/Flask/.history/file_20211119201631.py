from monkeylearn import MonkeyLearn# Instantiate the client Using your API key
from monkeylearn.exceptions import PlanQueryLimitError

ml = MonkeyLearn('0322b5749676f3fb91e8c3a6357d81228d61889f')

data = []
with open('/Users/m/Documents/GitHub/Data_Mining/text_data.json', 'r') as f:
    data.append(f.readline())
    
    print(len(data))
response = ml.classifiers.classify(
    model_id='cl_Jx8qzYJh', data=data
    
)


print(response.body)

print(response.plan_queries_allowed)


data = ['Text to classify'] * 300
batch_size = 200

try:
    except PlanQueryLimitError as e:
        partial_predictions = e.response.body  # The body of the successful responses
        non_2xx_raw_responses = r.response.failed_raw_responses  # List of requests responses objects
else:
    predictions = response.body