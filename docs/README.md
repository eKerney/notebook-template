# Python Prototyping Project Template

## Overview
This project is a python prototyping environment for testing and developing Python functions using Jupyter notebooks. It focuses on exploratory data analysis, function prototyping, and reproducible workflows, primarily for `arcpy, arcgis python api, and other geospatial data processes.`

## Installation
To set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/eKerney/notebook-template.git
   cd my-repo
   ```

2. **Create a virtual environment**:
   ```bash
   cd src 
   uv init
   source .venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

## Usage
To start prototyping:

1. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```
   This opens the Jupyter interface in your browser. Navigate to the `notebooks/` directory to open or create notebooks.

2. **Example Workflow**:
   - Create a new notebook in `notebooks/` or use an existing one (e.g., `notebooks/explore_data.ipynb`).
   - Import and test functions from `src/`:
     ```python
     from src.my_functions import my_data_function
     result = my_data_function(sample_data)
     print(result)
     ```

## Project Structure
- `src/`: Python modules with reusable functions (e.g., data processing, analysis).
- `notebooks/`: Jupyter notebooks for prototyping and testing functions.
- `data/`: Sample datasets or scripts to fetch data.
- `tests/`: Unit tests for functions in `src/`.
- `docs/`: Documentation files (see below for details).
- `requirements.txt`: Python dependencies for the project.
- `README.md`: Project overview (this file).
- `LICENSE`: License file (e.g., MIT).

## Documentation
The `docs/` folder contains detailed documentation for the project:

- `docs/api.md`: Auto-generated or manually written documentation for functions in `src/`.
- `docs/workflow.md`: Guide to the prototyping workflow, including how to structure notebooks and organize experiments.
- `docs/data.md`: Description of datasets in `data/` and how to use them.
- `docs/setup.md`: Detailed setup instructions for different environments.

To generate API documentation (optional):
```bash
pip install sphinx
sphinx-apidoc -o docs src/
cd docs && make html
```

## Development
To contribute or extend the project:

1. **Add functions** to `src/` with clear docstrings.
2. **Prototype in notebooks** under `notebooks/` to test functions.
3. **Run tests**:
   ```bash
   pytest tests/
   ```

4. **Lint and format code**:
   ```bash
   black src/ notebooks/
   flake8 src/ notebooks/
   ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
