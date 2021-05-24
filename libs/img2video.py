import cv2, os, imageio


class Main():

    def run(self, File, FPS, SIZE, FORMAT, Back_progreBar, Back_Label):
        self.FPS = float(FPS)
        self.SIZE = [int(i) for  i in SIZE.split("x")]
        self.File = File
        self.Back_progreBar = Back_progreBar
        self.Back_Label = Back_Label
        print("\n\nSize is here \n\n", SIZE)
        if FORMAT == "gif":
            self.Image2Gif()
        elif FORMAT == "avi":
            self.Image2Video()

    def Image2Gif(self):
        List = os.listdir(self.File)
        print(List)
        frames = []
        Num = 0
        for file in List:
            Num += 1
            self.Back_progreBar.value = Num
            file = os.path.join(self.File, file)
            print(file)
            img = cv2.imread(file, 1)
            img = cv2.resize(img, self.SIZE)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            frames.append(img)

        OUTPUT = "/".join(self.File.split("/")[:-1]) + "/OUT.gif"
        print(OUTPUT)
        gif=imageio.mimsave(OUTPUT,frames,'GIF',duration=1/self.FPS)
        self.Back_Label.text = "Task done: " + OUTPUT

    def Image2Video(self):
        OUTPUT = "/".join(self.File.split("/")[:-1]) + "/OUT.avi"
        List = os.listdir(self.File)
        img = cv2.imread(self.File +"/"+List[0])
        fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        print('1', OUTPUT)
        videowriter = cv2.VideoWriter(OUTPUT,fourcc,self.FPS,self.SIZE)
        Num = 0
        for i in List:
            Num += 1
            self.Back_progreBar.value = Num
            file = os.path.join(self.File, i)
            print(file)
            img = cv2.imread(file, 1)
            img = cv2.resize(img, self.SIZE)
            videowriter.write(img)
        videowriter.release()
        self.Back_Label.text = "Task done: " + OUTPUT
