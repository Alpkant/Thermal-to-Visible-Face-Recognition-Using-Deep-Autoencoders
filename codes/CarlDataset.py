import os
from PIL import Image
from torch.utils.data.dataset import Dataset
from torchvision import transforms 

class CarlDataset(Dataset):
    def __init__(self, root, transforms):
        self.transforms = transforms
        
        self.files = []
        self.files_dict = {}
        # Get all subject directories in root directory
        subjects = [subject for subject in os.listdir(root)]
        for sub in subjects:
            sub_p = os.path.join(root,sub)
            sessions = os.listdir(sub_p)
            for ses in sessions:
                ses_p = os.path.join(sub_p,ses)
                visible_p = os.path.join(ses_p,"classic")
                thermal_p = os.path.join(ses_p,"thermal_bmp")
                for item in os.listdir(visible_p):
                    item_t = item[:4] + 'B' + item[5:]
                    if os.path.isfile(os.path.join(visible_p,item)) and os.path.isfile(os.path.join(thermal_p,item_t)):
                        file = os.path.join(visible_p,item)
                        self.files.append(os.path.abspath(file))
                        self.files_dict[os.path.abspath(file)] = os.path.abspath(os.path.join(thermal_p,item_t))

        self.count = len(self.files)
        
    def __getitem__(self, index):
        img = Image.open(self.files[index]).convert('RGB')
        img = self.transforms(img)
        img_thermal = Image.open(self.files_dict[self.files[index]]).convert('RGB')
        img_thermal = self.transforms(img_thermal)
        # return rgb,thermal images
        return (img, img_thermal)

    def __len__(self):
        return self.count 


