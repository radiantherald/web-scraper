# web-scraper
## Program to web-scrape images from Google/Pinterest to build your own dataset.

This program comes in handy to create datasets for your ML/DL models. Just specify the link from where you want to scrape, the resultant folder, the image size required for the model and the split ratio.
It comes in-built with image resizing features and option to split the scraped images into training and test set.


Required Inputs -   

url = website link. <br />
folder = resultant folder. <br />
size = image resize dimensions (expected list). <br />
split_ratio = ratio to split training and test sets (expected list). <br />


Required Libraries/Packages 

os (https://pypi.org/project/os-sys/).   <br />
requests (https://pypi.org/project/requests/).   <br />
splitfolders (https://pypi.org/project/split-folders/).   <br />
bs4/Beautiful Soup (https://pypi.org/project/beautifulsoup4/).   <br />
PIL/Image (https://pypi.org/project/Pillow/).   <br />
