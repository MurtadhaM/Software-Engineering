from monkeylearn import MonkeyLearn# Instantiate the client Using your API key
ml = MonkeyLearn('0322b5749676f3fb91e8c3a6357d81228d61889f')

lines = []
with open('/Users/m/Documents/GitHub/Data_Mining/text_data.json', 'r') as f:
    lines.append(f.readline())
    
    
response = ml.classifiers.classify(
    model_id='cl_Jx8qzYJh',
    data=[
        'Great hotel with excellent location',
        'This is the worst hotel ever.'
    ]
)

print(response.body)

print(response.plan_queries_allowed)

