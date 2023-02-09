import pandas as pd
img_df = {'link': ['https://cdn.pixabay.com/photo/2017/10/10/07/48/hills-2836301__480.jpg',
                   'https://cdn.pixabay.com/photo/2018/02/13/23/41/nature-3151869__480.jpg']}
img_df = pd.DataFrame(img_df)

for idx, url in enumerate(img_df['link']):
    print(idx, url)