# This follows the example notebook at
# https://colab.research.google.com/drive/1MCTkTj9-93Ei-cLDQoj9AXaqPhpue7a3?usp=sharing#scrollTo=4MSVT6SdGBqY

from sdv.single_table import GaussianCopulaSynthesizer
from sdv.lite import SingleTablePreset

from sdv.metadata import SingleTableMetadata
import pprint

metadata = SingleTableMetadata()
import pandas as pd
import warnings

# Supress warnings in output
warnings.filterwarnings('ignore')

# Load our scraped startup data and detect column types (the metadata)
dfStartUpsReal = pd.read_csv("data/startups.csv")
metadata.detect_from_dataframe(data=dfStartUpsReal)
# Tweak metadata
metadata.update_column(column_name="industry",sdtype='categorical')
pprint.pprint(metadata.to_dict())
print()

# Use a basic synthesis method
synthesizer = SingleTablePreset(metadata, name='FAST_ML')
synthesizer.fit(dfStartUpsReal)

# Create samples
synthetic_data = synthesizer.sample(num_rows=10)
print(synthetic_data.head(10) )

# TODO Synthetic Data Validation!!

