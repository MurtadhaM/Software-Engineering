from monkeylearn import MonkeyLearn# Instantiate the client Using your API key
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

