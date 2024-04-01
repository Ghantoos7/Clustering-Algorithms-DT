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


def getAnswers():
    answers = [
        Answer(QUESTIONS["Data Characteristics"], QUESTIONS["Data Type"], description="This is the start of the tree", response=""),

        Answer(QUESTIONS["Data Type"], QUESTIONS["Dataset Size"], description="Proceed if your dataset consists entirely of numerical values.", response="Numeric"),
        Answer(QUESTIONS["Data Type"], QUESTIONS["Data Transformation (If Categorical or Mixed)"], description="Proceed if your dataset includes non-numeric, categorical data or a mix of both.", response="Categorical or Mixed"),

        Answer(QUESTIONS["Data Transformation (If Categorical or Mixed)"], QUESTIONS["Data Type"], description="Once the data is transformed to numeric, consider its size.", response="Transformation Done"),

        Answer(QUESTIONS["Dataset Size"], QUESTIONS["Cluster Shape and Noise"], description="For small to medium datasets, assess the shape and noise level of your data.", response="Small to Medium"),
        Answer(QUESTIONS["Dataset Size"], QUESTIONS["Specific Requirements"], description="For large datasets, consider algorithms that can handle large volumes efficiently.", response="Large"),

        Answer(QUESTIONS["Cluster Shape and Noise"], QUESTIONS["K-means or Gaussian Mixture Model"], description="If clusters are circular with low noise, consider K-means or Gaussian Mixture Model.", response="Circular, Low Noise"),
        Answer(QUESTIONS["Cluster Shape and Noise"], QUESTIONS["DBSCAN, OPTICS, or Gaussian Mixture Model"], description="For non-circular clusters or when there's low to moderate noise, consider DBSCAN, OPTICS, or Gaussian Mixture Model.", response="Non-Circular, Low-Moderate Noise"),
        Answer(QUESTIONS["Cluster Shape and Noise"], QUESTIONS["DBSCAN or OPTICS"], description="For high noise levels and outlier detection, DBSCAN or OPTICS is suitable.", response="High Noise, Outliers"),

        Answer(QUESTIONS["Specific Requirements"], QUESTIONS["DBSCAN, OPTICS, or Mean-Shift"], description="When the number of clusters is unknown, choose between DBSCAN, OPTICS, or Mean-Shift.", response="Unknown Clusters"),
        Answer(QUESTIONS["Specific Requirements"], QUESTIONS["DBSCAN or OPTICS"], description="For outlier detection between high-density clusters, consider DBSCAN or OPTICS.", response="Outlier Detection"),
        Answer(QUESTIONS["Specific Requirements"], QUESTIONS["Hierarchical Clustering"], description="To find relationships between items, Hierarchical Clustering is a good choice.", response="Relationships Between Items"),
    ]
    
    return answers
