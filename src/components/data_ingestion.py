from pathlib import Path
import shutil
import yaml


class DataIngestion:
    def __init__(self,config_path:Path):
        
        self.base=Path(__file__).resolve().parents[2]
        with open(config_path,'r') as f:
            config=yaml.safe_load(f)
        self.src=config['data_ingestion']['source_file']
        self.dst=config['data_ingestion']['destination_file']
    def ingestdata(self):
        shutil.copy(self.src,self.dst)
        