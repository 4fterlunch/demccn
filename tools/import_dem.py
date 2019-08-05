# tools for importing dem
# Michael Holmes 2019
# mkhlib@outlook.com

import georasters as gr

# load a raster file and return as a pandas data frame
def load_to_pandas(ras):
    if ras is not None:
        data = gr.from_file(ras)
        df = data.to_pandas()
        return df

def load_raster(ras):
    if ras is not None:
        return  gr.from_file(ras)

def
