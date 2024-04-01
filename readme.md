# Clustering Algorithm Decision Tree Visualization

This project provides an interactive visualization tool for understanding decision paths in selecting appropriate clustering algorithms based on dataset characteristics. It utilizes Pyvis, a Python library for visualizing networks, and NetworkX for managing the underlying graph structure.



Live: https://clustering-algorithms-dt.vercel.app/

## Overview

The tool guides users through a series of questions about their dataset, such as data type, size, and specific requirements, to suggest the most suitable clustering algorithms. It visualizes decision trees where nodes represent questions or algorithm suggestions, and edges denote decision paths based on answers.

## Features

- **Interactive Visualization**: Explore decision paths by clicking through the interactive network diagram.
- **Custom Highlighting and Filtering**: Nodes and edges highlight and filter based on user interactions to emphasize relevant paths and decisions.
- **Responsive Design**: Adapts to different screen sizes for ease of use on any device.
- **Dynamic Data Integration**: Easily update decision trees by modifying the source data without needing to adjust the visualization code.

## Installation

To run this project locally, you'll need Python installed on your machine. It's recommended to use a virtual environment:


### Clone the repository
git clone https://github.com/Ghantoos7/Clustering-Algorithms-DT.git

### Navigate into the project directory
```
cd clustering-decision-tree-visualization
```
### Create a virtual environment (optional)
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
## Install the requirements
```
pip install -r requirements.txt
```

## Usage

To start visualizing the decision tree, run:

```bash
python app.py
```

This will generate an HTML file (`index.html`) that you can open in your web browser to view the interactive visualization.

## Contributing

Contributions to enhance the visualization tool are welcome. Please feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

