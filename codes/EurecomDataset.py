class EurecomDataset(Dataset):
    
    def __init__(self,domain,variation,training_dir=None,transform=None):
        self.transform = transform
        self.training_dir = training_dir
        # For each variant keep a list
        self.thermal_illu = []
        self.thermal_exp  = []
        self.thermal_pose = []
        self.thermal_occ  = []

        self.visible_illu = []
        self.visible_exp  = []
        self.visible_pose = []
        self.visible_occ  = []

        # Get all subject directories
        subjects = [subject for subject in os.listdir(training_dir)]
        self.num_classes = len(subjects)
        
        for sub in subjects:
            sub_p = os.path.join(training_dir,sub)
            visible_pth = os.path.join(sub_p,"VIS")
            thermal_pth = os.path.join(sub_p,"TH")
            
            self.visible_illu.extend([ (os.path.join(visible_pth,x),int(x[4:7])-1) for x in os.listdir(visible_pth) if "_L" in x ])
            self.visible_exp.extend([ (os.path.join(visible_pth,x) ,int(x[4:7])-1) for x in os.listdir(visible_pth) if "_N" in x or "_E" in x ]) 
            self.visible_pose.extend([ (os.path.join(visible_pth,x),int(x[4:7])-1) for x in os.listdir(visible_pth) if "_P" in x ])
            self.visible_occ.extend([ (os.path.join(visible_pth,x) ,int(x[4:7])-1) for x in os.listdir(visible_pth) if "_O" in x ])

            
            self.thermal_illu.extend([ (os.path.join(thermal_pth,x),int(x[3:6])-1) for x in os.listdir(thermal_pth) if "_L" in x  ])
            self.thermal_exp.extend([ (os.path.join(thermal_pth,x) ,int(x[3:6])-1) for x in os.listdir(thermal_pth) if "_N" in x or "_E" in x ])
            self.thermal_pose.extend([ (os.path.join(thermal_pth,x),int(x[3:6])-1) for x in os.listdir(thermal_pth) if "_P" in x ])
            self.thermal_occ.extend([ (os.path.join(thermal_pth,x) ,int(x[3:6])-1) for x in os.listdir(thermal_pth) if "_O" in x ])
        
        # Set dataset to intented domain
        if domain == "thermal":
            if variation == "illu":
                self.dataset = self.thermal_illu
            elif variation == "exp":
                self.dataset = self.thermal_exp
            elif variation == "pose":
                self.dataset = self.thermal_pose
            else:
                self.dataset = self.thermal_occ
                
        else:
            if variation == "illu":
                self.dataset = self.visible_illu
            elif variation == "exp":
                self.dataset = self.visible_exp
            elif variation == "pose":
                self.dataset = self.visible_pose
            else:
                self.dataset = self.visible_occ
            
        
        self.count = len(self.dataset)
        
    def __getitem__(self, index):
        image,label = self.dataset[index]
        img_a = Image.open(image).convert('RGB')
        if self.transform is not None:
            img_a = self.transform(img_a)
        # return image and label
        return img_a,label

    def __len__(self):
        return self.count 