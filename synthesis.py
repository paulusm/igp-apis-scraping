# This follows the example notebook at
# https://colab.research.google.com/drive/1MCTkTj9-93Ei-cLDQoj9AXaqPhpue7a3?usp=sharing#scrollTo=4MSVT6SdGBqY

from sdv.single_table import GaussianCopulaSynthesizer
from sdv.lite import SingleTablePreset
from sdv.metadata import SingleTableMetadata
import pprint

#from ollamagen import startupGenerator
import pandas as pd
import warnings

metadata = SingleTableMetadata()

# Supress warnings in output
warnings.filterwarnings('ignore')

# Load our scraped startup data and detect column types (the metadata)
dfStartUpsReal = pd.read_csv("data/startups.csv")
metadata.detect_from_dataframe(data=dfStartUpsReal)
# Tweak metadata


metadata.update_column(column_name="title",sdtype='text')
metadata.update_column(column_name="description",sdtype='text')
metadata.update_column(column_name="fundingtype",sdtype='categorical')
metadata.update_column(column_name="industry",sdtype='categorical')

pprint.pprint(metadata.to_dict())
print()

# Use a basic synthesis method
#synthesizer = SingleTablePreset(metadata, name='FAST_ML')
synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(dfStartUpsReal)

# Create samples
nRows = 10
synthetic_data = synthesizer.sample(num_rows=nRows)

# Use Llama model for startup title and description. Map the function to industry in the dataset

# for i in range(nRows):
#     llamaGen = startupGenerator(synthetic_data['industry'][i])
#     print(llamaGen)
#     synthetic_data['title'][i] = llamaGen["name"]
#     synthetic_data['description'][i] = llamaGen["description"]


print(synthetic_data.head(10) )

# TODO Synthetic Data Validation!!
