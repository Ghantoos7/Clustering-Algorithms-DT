class Question:
    def __init__(self, question, description):
        self.question = question
        self.description = description
        
class Answer:
    def __init__(self,source : Question, target : Question, description : str = None, response : str = None):
        self.source = source
        self.target = target
        self.description = description
        self.response = response
        


QUESTIONS = {}


QUESTIONS["Data Characteristics"] = Question(
    "Data Characteristics", 
    "Start by assessing the primary characteristics of your data set."
)

QUESTIONS["Data Type"] = Question(
    "Data Type",
    "Identify whether the data is numeric, categorical, or a mix."
)

QUESTIONS["Data Transformation (If Categorical or Mixed)"] = Question(
    "Data Preprocessing",
    "Transform categorical or mixed data types into a numerical format."
)

QUESTIONS["Dataset Size"] = Question(
    "Dataset Size",
    "Consider whether the dataset is small-to-medium or large in size."
)

QUESTIONS["Cluster Shape and Noise"] = Question(
    "Cluster Shape and Noise",
    "Assess the cluster shapes and noise level in the data."
)

QUESTIONS["Specific Requirements"] = Question(
    "Specific Requirements",
    "Identify any specific requirements that may influence algorithm choice, such as the need for scalability or handling of outliers."
)

