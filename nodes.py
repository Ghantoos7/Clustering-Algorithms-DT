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

QUESTIONS["K-means or Gaussian Mixture Model"] = Question(
    "K-means or Gaussian Mixture Model",
    "Decide between using K-means for clear, spherical clusters or Gaussian Mixture Models for more complex distributions."
)

QUESTIONS["DBSCAN, OPTICS, or Gaussian Mixture Model"] = Question(
    "DBSCAN, OPTICS, or Gaussian Mixture Model",
    "Choose between density-based algorithms like DBSCAN and OPTICS or Gaussian Mixture Models for varied density and shape clusters."
)

QUESTIONS["DBSCAN or OPTICS"] = Question(
    "DBSCAN or OPTICS",
    "Opt for DBSCAN or OPTICS when dealing with noise and the need for outlier detection."
)

QUESTIONS["DBSCAN, OPTICS, or Mean-Shift"] = Question(
    "DBSCAN, OPTICS, or Mean-Shift",
    "Select between DBSCAN, OPTICS, or Mean-Shift based on cluster density variance."
)

QUESTIONS["Hierarchical Clustering"] = Question(
    "Hierarchical Clustering",
    "Use Hierarchical Clustering to find nested clusters and understand data hierarchy."
)

