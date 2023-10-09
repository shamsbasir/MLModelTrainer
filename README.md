# MLModelTrainer

This is a Python project for training a simple machine learning model using scikit-learn. It also includes GitHub Actions for automation.

## File Structure

```
MLModelTrainer/
│-- .github/
│   │-- workflows/
│   │   │-- python-ci.yml
│-- src/
│   │-- __init__.py
│   │-- train.py
│-- pyproject.toml
```

- `.github/`: GitHub Actions directory.
  - `workflows/`: Contains GitHub Actions workflow configuration.
    - `python-ci.yml`: GitHub Actions workflow YAML file for Python CI.
- `src/`: Package directory for the project.
  - `__init__.py`: Initialization file for the package.
  - `train.py`: Python script for training the machine learning model.
- `pyproject.toml`: Poetry configuration file for managing project dependencies.
- `README.md`: This readme file.

## Project Setup and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/MLModelTrainer.git
   ```

2. Set up a virtual environment and install dependencies using Poetry:

   ```bash
   cd MLModelTrainer
   poetry install
   ```

3. Train the machine learning model:

   ```bash
   poetry run python src/train.py
   ```

4. Customize the project as needed and add your machine learning code to `train_model.py`.

## GitHub Actions

GitHub Actions have been set up to automate testing and other workflows. Check the `.github/workflows/python-ci.yml` file for configuration details.


