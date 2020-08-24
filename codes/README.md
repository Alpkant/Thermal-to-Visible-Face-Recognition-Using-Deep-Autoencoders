This directory contains dataset and model files. Below, you can see some examples how to use these Dataset classes.

 
```python
eurocom_dataset = EurocomDataset("thermal","illu",training_dir=Config.directory,transform=Config.transform)
```
```python
carl_dataset = CarlDataset(training_dir=Config.carl_directory,transform=Config.transform)
```
