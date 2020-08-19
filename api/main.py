from typing import List

from fastapi import FastAPI, Query
from mangum import Mangum
import scipy.stats as stats

app = FastAPI(openapi_prefix="/prod")


@app.get("/simple")
def read_root():
    return {"Hello": "World"}


@app.get('/stats/')
def stats_describe(numbers: List[float] = Query(
    default=None,
    title='Numbers',
    description='A set of numbers you wish to calculate statistics from.')):
    description = stats.describe(numbers)
    result = {
        "nobs": description.nobs,
        "mean": description.mean,
        "minmax": [int(num) for num in description.minmax],
        "skewness": description.skewness,
        "variance": description.variance,
        "kurtosis": description.kurtosis
    }
    return result


handler = Mangum(app, enable_lifespan=False)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
