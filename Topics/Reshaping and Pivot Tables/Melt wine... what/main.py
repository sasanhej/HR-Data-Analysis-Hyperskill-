import pandas as pd

wine_sample = {'variety': {0: 'Bordeaux-style Red Blend', 1: 'Cabernet Sauvignon', 2: 'Chardonnay', 3: 'Merlot',
                           4: 'Pinot Noir', 5: 'Red Blend', 6: 'Rosé', 7: 'Sauvignon Blanc', 8: 'Syrah', 9: 'White Blend'},
               'Argentina': {0: 79, 1: 391, 2: 204, 3: 34, 4: 68, 5: 209, 6: 30, 7: 52, 8: 46, 9: 30},
               'Australia': {0: 28, 1: 155, 2: 206, 3: 7, 4: 72, 5: 60, 6: 18, 7: 19, 8: 15, 9: 12},
               'Canada': {0: 15, 1: 3, 2: 14, 3: 4, 4: 14, 5: 5, 6: 2, 7: 4, 8: 9, 9: 5},
               'France': {0: 862, 1: 30, 2: 1587, 3: 67, 4: 1121, 5: 218, 6: 1120, 7: 616, 8: 110, 9: 167},
               'Italy': {0: 2, 1: 29, 2: 110, 3: 47, 4: 1, 5: 1605, 6: 4, 7: 18, 8: 49, 9: 295},
               'Spain': {0: 6, 1: 42, 2: 37, 3: 11, 4: 11, 5: 683, 6: 106, 7: 16, 8: 27, 9: 236},
               'US': {0: 1235, 1: 2463, 2: 2778, 3: 703, 4: 5449, 5: 1985, 6: 510, 7: 669, 8: 1728, 9: 410}}

df = pd.DataFrame(wine_sample)

# your code here
df_long = ...