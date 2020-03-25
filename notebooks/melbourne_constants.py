
MAX_CATEGORICAL_FEATURE_VALUES = [303, 3, 5, 10, 32, 8]

CATEGORICAL_FEATURE_KEYS = [
    'Suburb',
    'Address',
    'Type',
    'Method',
    'SellerG', 
    'Date',
    'CouncilArea',
    'Regionname'
]

# Numerical features
DENSE_FLOAT_FEATURE_KEYS = ['Rooms',
                            'Price',
                            'Distance',
                            'Postcode',
                            'Bedroom2',
                            'Bathroom',
                            'Car']
#                            'Landsize',
#                            'BuildingArea',
#                            'YearBuilt']

# Number of buckets used by tf.transform for encoding numerical features into a bucket generaliation
FEATURE_BUCKET_COUNT = 100

BUCKET_FEATURE_KEYS = []
#    'Lattitude', 
#    'Longtitude'
#]
