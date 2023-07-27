from pytube import YouTube
class Download:
    """Download youtube videos."""
    def __init__(self, res,link):
        self.link=link
        self.res=res
        global lis
        #res 18=360,22=720, 137=1080p
        lis={1:18,2:22,3:137}
        
    def run(self):
         """Run tube"""
         if int(self.res) in lis:
            yt = YouTube(self.link)
            yt.streams.filter(file_extension='mp4')
            stream = yt.streams.get_by_itag(lis[int(self.res)]) #res type
            stream.download()
       
        
        
        
        
        


if __name__ == '__main__':
        print('Select resolution 1-360p 2-720p 3-1080p')
        res=input() 
        print('Enter link' )
        link=input()
        dow=Download(res,link)
        dow.run()
       
        
    